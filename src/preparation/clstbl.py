import pandas as pd
import numpy as np
from db import cx

def get_table(sql_script: str) -> pd.DataFrame:
    query = cx.execute(sql_script)
    cols = [column[0] for column in query.description]
    df = pd.DataFrame.from_records(data=query.fetchall(), columns=cols)
    return df

def data_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    df = df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)
    df = df.dropna()
    for column in df.columns:
        df[column] = df[column].str.replace(r'\W', '', regex=True)
    for column in df.columns:
        df[column] = df[df[column].str.strip().astype(bool)] 
    return df