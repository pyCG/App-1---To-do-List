import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)
            
if __name__== "__main__":
    make_archive(filepaths=["/Users/gui/Documents/Course Python/bonus/bonus16.py", "/Users/gui/Documents/Course Python/bonus/bonus12.py"], dest_dir="/Users/gui/Documents/Course Python/bonus")
