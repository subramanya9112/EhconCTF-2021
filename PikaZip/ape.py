import patoolib
import os

for i in range(1000):
    file = os.listdir("out")[-1]
    print(file)
    if file == "flag.txt":
        break
    patoolib.extract_archive(f"out/{file}", outdir="out")
    os.remove(f"out/{file}")
