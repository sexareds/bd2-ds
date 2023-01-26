get_students_EIU = '''
    SELECT Opcion.titulo AS Respuesta
    FROM Respuesta
    INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
    AND Respuesta.num_opcion = Opcion.num_opcion
    AND Opcion.num_pregunta = 4
'''

get_students_gender = '''
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
'''

get_students_semester = '''
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
'''

get_students_semester_2 = '''
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
        AND Respuesta.num_opcion = 2
    ) T2
    ON T1.num_encuesta = T2.num_encuesta;
'''

get_students_career = '''
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
'''

get_students_career_2 = '''
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
        AND Respuesta.num_opcion = 2
    ) T2
    ON T1.num_encuesta = T2.num_encuesta;
'''