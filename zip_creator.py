import zipfile
import pathlib


def make_zip(filepaths, folder):
    folder_path = pathlib.Path(folder, "compressed.zip")
    with zipfile.ZipFile(folder_path, 'w') as compress:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            compress.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_zip(filepaths=["test1.txt", "test2.txt"], folder="files")