import pandas as pd


df = pd.read_excel(
    "zone_ranges/Carriers_zone_ranges.xlsx",
    sheet_name="UPS zip ranges"
)

limit_list = df["UPS zone ranges"]
for limit in limit_list:
    lowest_limit = limit.replace("-", " ").split(" ")[0]
