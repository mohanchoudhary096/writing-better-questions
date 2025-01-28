import requests
import pandas as pandas
import os
from io import StringIO


url="https://raw.githubusercontent.com/hundredblocks/ml-powered-applications/master/data/writers.csv"

filename=os.path.join("data", "writers.csv")


if not os.path.exists(filename):
    print(f"file not found locally. Fetching from url...")

    response=requests.get(url)
    if response.status_code == 200:
        # csv_data=StringIO(response.text)
        # df=pd.read_csv(csv_data)
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Csv file saved to {filename}")

        df=pd.read_csv(filename)
        print("Csv content loaded into dataFrame")
        print(df.head())
    else:
        print(f"Failed to fetch the Csv file. Status code: {requests.status_code}")
else:
    print(f"File already exists {filename}.Skipping fetch")


url="https://github.com/hundredblocks/ml-powered-applications/raw/refs/heads/master/data/writers_with_features.csv"
file=os.path.join("data", "writers_with_features.csv")

if not os.path.exists(file):
    response=requests.get(url)
    if response.status_code == 200:
        with open(file, "wb") as f:
            f.write(response.content)
        print(f"Csv file saved to : {file}")
    else:
        print(f"Failed to fetch the csv file. Status code : {response.status_code}")
else:
    print(f"File already exists : {file}")

