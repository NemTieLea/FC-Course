import os


if not os.path.exists("run.pid"):
    print("plik run.pid nie istnieje")
else:
    with open("run.pid") as f:
        pid = int(f.read().strip())
    print(f"Killing process {pid}")
