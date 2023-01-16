import preparation.clstbl as ct

def get_qualities() -> None:
    sql_script = """
        SELECT *
        FROM Respuesta
        WHERE num_pregunta = 6;
    """
    df = ct.get_table(sql_script)
    # df = ct.data_cleaning(df)
    return df

def get_students_semester() -> None:
    sql_script = """

    """
    df = ct.get_table(sql_script)
    df = ct.data_cleaning(df)
    return df