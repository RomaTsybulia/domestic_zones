import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "https://www.ups.com/us/en/support/shipping-support/shipping-costs-rates/retail-rates.page"


def get_path_for_xls_files():
    current_dir = os.getcwd()
    final_dir = os.path.join(current_dir, r"xls_files")

    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    return final_dir


def get_files(keys):
    options = Options()
    path_for_saving = get_path_for_xls_files()
    prefs = {
        "download.default_directory": path_for_saving}
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(BASE_URL)

    for key in keys:
        input_field = driver.find_element(By.CLASS_NAME, "ups-form_input")
        input_field.send_keys(key)
        input_field.submit()
        input_field.clear()

    driver.close()


if __name__ == "__main__":
    ups_list = ["0500", "01000"]
    get_files(ups_list)

