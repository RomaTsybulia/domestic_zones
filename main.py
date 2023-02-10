import pandas as pd

from convert import convert_files
from parse import get_files
from zip_unpacker import zip_unpacker


def main():
    df = pd.read_excel(
        "zone_ranges/Carriers_zone_ranges.xlsx",
        sheet_name="UPS zip ranges"
    )

    limit_list = df["UPS zone ranges"]

    formated_limit_list = [
        limit.replace("-", " ").split(" ")[0]
        for limit in limit_list
    ]

    get_files(formated_limit_list)
    convert_files()
    zip_unpacker()



if __name__ == "__main__":
    main()

