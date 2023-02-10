import os
import time

from pathlib import Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

BASE_URL = "https://products.aspose.app/cells/conversion/xls-to-xlsx"


def get_path_for_converted_files():
    current_dir = os.getcwd()
    final_dir = os.path.join(current_dir, r"xlsx_files")

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    return final_dir


def convert_files():
    options = Options()
    path_for_saving = get_path_for_converted_files()
    prefs = {
        "download.default_directory": path_for_saving}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)

    path_for_xls_files = Path.cwd().joinpath("xls_files")
    files = [
        str(path_for_xls_files.joinpath(file.name))
        for file in path_for_xls_files.rglob('*')
        if ".xls" in file.name
    ]

    driver = webdriver.Chrome(options=options)

    while files:
        driver.get(BASE_URL)
        input_field = driver.find_element(By.CLASS_NAME, "upload-file-input")

        if len(files) >= 10:
            for _ in range(10):
                input_field.send_keys(files.pop())
        else:

            for _ in range(len(files)):
                input_field.send_keys(files.pop())

        convert_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "uploadButton"))
        )
        convert_button.click()

        download_link = WebDriverWait(driver, 90).until(
            EC.element_to_be_clickable((By.ID, "DownloadButton"))
        )
        download_link = download_link.get_attribute("href")
        driver.get(download_link)

    driver.close()


if __name__ == "__main__":
    convert_files()
