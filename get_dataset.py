import json
import pandas as pd

def get_mccmnc_dataset():
    url = "https://mcc-mnc.com/"
    # we need to know the number of columns to read them in all as string with converters
    n_columns = pd.read_html(url)[0].shape[1]

    mccmnc = pd.read_html(url, converters={i: str for i in range(n_columns)})[0]
    mccmnc.columns = mccmnc.columns.map(lambda x: x.lower().replace(" ", "_"))
    

    # Fill Wallis and Futuna with MCC 681
    mccmnc.loc[mccmnc['country'] == 'Wallis and Futuna', 'country_code'] = '681'
    mccmnc.fillna("", inplace=True)

    return mccmnc

def test_read_json():
    with open("mccmnc_dataset.json", "r") as f:
        mccmnc = json.load(f)
    print(mccmnc)

def test_no_nulls():
    mccmnc = get_mccmnc_dataset()
    assert mccmnc.isnull().sum().sum() == 0
    

if __name__ == "__main__":
    mccmnc = get_mccmnc_dataset()
    print(mccmnc.head())
    test_no_nulls()
    
    with open("mccmnc_dataset.json", "w") as f:
        json.dump(mccmnc.to_dict(orient="records"), f)
    test_read_json()
