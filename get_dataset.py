import json
import pandas as pd

def get_mccmnc_dataset():
    url = "https://mcc-mnc.com/"
    # we need to know the number of columns to read them in all as string with converters
    n_columns = pd.read_html(url)[0].shape[1]

    mccmnc = pd.read_html(url, converters={i: str for i in range(n_columns)})[0]
    mccmnc.columns = mccmnc.columns.map(lambda x: x.lower().replace(" ", "_"))

    return mccmnc

if __name__ == "__main__":
    mccmnc = get_mccmnc_dataset()
    print(mccmnc.head())
    with open("mccmnc_dataset.json", "w") as f:
        json.dump(mccmnc.to_dict(orient="records"), f)