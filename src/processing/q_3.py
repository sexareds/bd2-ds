import preparation.clstbl as ct

# un metodo para obtener a los 15 estudiantes con mas votos

# del mas votado, obtener:
# ordenar por carrera, por semestre a los votantes.

def get_top_students():
    sql_script = '''
        SELECT respuesta
        FROM Respuesta
        WHERE num_pregunta = 7;
    '''
    df = ct.get_table(sql_script)
    df = ct.data_cleaning(df)
    df = df.value_counts().reset_index(name='votos')
    df = df.set_index('respuesta').head(15)
    return df

def get_students_semester():
    sql_script = '''
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
            AND Respuesta.num_pregunta = 7
        ) T2
        ON T1.num_encuesta = T2.num_encuesta;
    '''
    df = ct.get_table(sql_script)
    df = ct.data_cleaning(df)
    return df

def get_students_career():
    sql_script = '''
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
            AND Respuesta.num_pregunta = 7
        ) T2
        ON T1.num_encuesta = T2.num_encuesta;
    '''
    df = ct.get_table(sql_script)
    df = ct.data_cleaning(df)
    return df