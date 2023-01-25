import preparation.clstbl as ct
import querying.query2 as q2

def get_qualities() -> None:
    df = ct.get_table(q2.get_qualities)
    df = ct.data_cleaning(df)
    return df

# add more functions as needed