import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_dir = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)