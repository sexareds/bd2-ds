import pandas as pd
import numpy as np
from db import cx

def get_table(sql_script: str) -> pd.DataFrame:
    query = cx.execute(sql_script)
    cols = [column[0] for column in query.description]
    df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return df

# TO DO: Add NaN values

def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df = df.dropna()
    for column in df.columns:
        df[column] = df[column].replace(r'\W', '', regex=True)
    df.columns = df.columns.str.strip()
    return df