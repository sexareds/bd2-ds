import preparation.clstbl as ct

def get_students_EIU():
    sql_script = """
        SELECT Opcion.titulo AS Respuesta
        FROM Respuesta
        INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Opcion.num_pregunta = 4
    """
    df = ct.get_table(sql_script)
    return df

def get_students_gender():
    sql_script = """
        SELECT T1.titulo AS Genero
        FROM (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Encuesta
            INNER JOIN Respuesta
            ON Encuesta.num_encuesta = Respuesta.num_encuesta
            AND Respuesta.num_pregunta = 1
            INNER JOIN Opcion
            ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
        ) T1 
        INNER JOIN (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Respuesta
            INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
            AND Respuesta.num_pregunta = 4
            AND Respuesta.num_opcion = 1
        ) T2
        ON T1.num_encuesta = T2.num_encuesta;
    """
    df = ct.get_table(sql_script)
    return df

def get_students_semester():
    sql_script = """
        SELECT T1.num_encuesta, T1.titulo
        FROM (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Encuesta
            INNER JOIN Respuesta
            ON Encuesta.num_encuesta = Respuesta.num_encuesta
            AND Respuesta.num_pregunta = 2
            INNER JOIN Opcion
            ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
        ) T1 
        INNER JOIN (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Respuesta
            INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
            AND Respuesta.num_pregunta = 4
            AND Respuesta.num_opcion = 1
        ) T2
        ON T1.num_encuesta = T2.num_encuesta;
    """
    df = ct.get_table(sql_script)
    return df

def get_students_career():
    sql_script = """
        SELECT T1.num_encuesta, T1.titulo
        FROM (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Encuesta
            INNER JOIN Respuesta
            ON Encuesta.num_encuesta = Respuesta.num_encuesta
            AND Respuesta.num_pregunta = 3
            INNER JOIN Opcion
            ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
        ) T1 
        INNER JOIN (
            SELECT Respuesta.num_encuesta, Opcion.titulo
            FROM Respuesta
            INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
            AND Respuesta.num_opcion = Opcion.num_opcion
            AND Respuesta.num_pregunta = 4
            AND Respuesta.num_opcion = 1
        ) T2
        ON T1.num_encuesta = T2.num_encuesta;
    """
    df = ct.get_table(sql_script)
    return df