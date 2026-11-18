from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'dist'
if OUT.exists():
    shutil.rmtree(OUT)
OUT.mkdir()

for source in ROOT.iterdir():
    if source.name in {'.git', 'dist'}:
        continue
    target = OUT / source.name
    if source.is_dir():
        shutil.copytree(source, target)
    else:
        shutil.copy2(source, target)

print(f'Built static site in {OUT}')
