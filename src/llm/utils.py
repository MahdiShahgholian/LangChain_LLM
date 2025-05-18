import json
import pandas as pd
import os
from typing import Union

class DataLoader:
    def __init__(self, filename: str):
        self.filename = filename
        self.extension = os.path.splitext(filename)[1].lower()

    def load(self)-> Union[dict, list, pd.DataFrame]:
        if self.extension == '.json':
            return self.json_loader()
        elif self.extension == '.csv':
            return self.csv_loader()
        else:
            raise ValueError(f"Unsupported file format: {self.extension}")

    def json_loader(self) -> Union[dict, list, pd.DataFrame]:
        with open(self.filename, 'r', encoding='utf-8') as file:
            return json.load(file)

    def csv_loader(self)-> pd.DataFrame:
        return pd.read_csv(self.filename)