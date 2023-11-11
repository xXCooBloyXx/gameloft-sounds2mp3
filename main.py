import os
import subprocess

folders = ["sounds", "mp3"]

for i in folders:
    if not os.path.exists(f"./{i}"):
        os.makedirs(f"./{i}")

for f in os.listdir("./sounds/"):
    file = os.path.basename(f).split('.')
    extension = file[-1]
    if extension in ["mpc", "wav", "vxn"]:
        filename = file[-2]
        print(f"Converting {filename}.{extension}...")
        if extension == "vxn":
            command = [
                "vgmstream-cli.exe",
                "-o", f"./mp3/{filename}.mp3",
                f"./sounds/{filename}.{extension}"
            ]
        else:
            command = [
                "ffmpeg",
                "-y", "-v", "0",
                "-i", f"./sounds/{filename}.{extension}",
                f"./mp3/{filename}.mp3"
            ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError:
            print(f"Failed to convert {filename}.{extension}")
