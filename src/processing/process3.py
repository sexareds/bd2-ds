import preparation.clstbl as ct
import querying.query3 as q3

def get_top_students():
    df = ct.get_table(q3.get_top_students)
    df = ct.data_cleaning(df)
    df = df.value_counts().reset_index(name='votos')
    df = df.set_index('respuesta').head(15)
    return df

def get_students_semester():
    df = ct.get_table(q3.get_students_semester)
    df = ct.data_cleaning(df)
    return df

def get_students_career():
    df = ct.get_table(q3.get_students_career)
    df = ct.data_cleaning(df)
    return df