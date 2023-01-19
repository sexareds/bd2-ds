import preparation.clstbl as ct

def get_qualities() -> None:
    sql_script = '''
        SELECT respuesta
        FROM Respuesta
        WHERE num_pregunta = 6;
    '''
    df = ct.get_table(sql_script)
    df = ct.data_cleaning(df)
    return df