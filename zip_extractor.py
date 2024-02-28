import zipfile


def extract_zip(zip_path, folder_path):
    with zipfile.ZipFile(zip_path, 'r') as archive:
        archive.extractall(folder_path)


if __name__ == "__main__":
    extract_zip("files/compressed.zip", "files")
