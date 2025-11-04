import json
import pandas as pd

with open("mccmnc_daataset.json", "w") as f:
    json.dump(pd.read_html("https://www.mcc-mnc.com/")[0].to_dict(orient="records"), f)
