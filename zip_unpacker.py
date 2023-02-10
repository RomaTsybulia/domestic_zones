import os
from pathlib import Path
from zipfile import ZipFile



def get_path_for_converted_files():
    current_dir = os.getcwd()
    final_dir = os.path.join(current_dir, r"xlsx_files")

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    return final_dir


def zip_unpacker():
    path_for_zip_dir = Path.cwd().joinpath("zip_files")
    path_for_xlsx_files = get_path_for_converted_files()
    zip_files = [
        str(path_for_zip_dir.joinpath(file.name))
        for file in path_for_zip_dir.rglob('*')
        if ".zip" in file.name
    ]


    for file in zip_files:
        with ZipFile(file, "r") as zipObj:
            print(zipObj.filename)
            zipObj.extractall(path_for_xlsx_files)
            print(zipObj.filename)

zip_unpacker()
