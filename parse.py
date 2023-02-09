import asyncio
import os
import time
from concurrent.futures.thread import ThreadPoolExecutor

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

BASE_URL = "https://www.ups.com/us/en/support/shipping-support/shipping-costs-rates/retail-rates.page"

executor = ThreadPoolExecutor(2)

def get_path_for_xls_files():
    current_dir = os.getcwd()
    final_dir = os.path.join(current_dir, r"xls_files")
    if not os.path.exists(final_dir):
        os.makedirs(final_dir)

    return final_dir


def parse(loop):
    loop.run_in_executor(executor, get_file, BASE_URL)


def get_file(key):
    options = Options()
    prefs = {
        "download.default_directory": r"D:\test_tasks\domestic_zones\xls_files"}
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=options)

    driver.get(BASE_URL)
    input_field = driver.find_element(By.CLASS_NAME, "ups-form_input")
    input_field.send_keys(key)
    input_field.submit()
    time.sleep(1)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    ups_list = ["0500", "01000"]
    get_path_for_xls_files()


