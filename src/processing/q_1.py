import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import preparation.clstbl as ct

# un metodo para saber de los que votaron 'si', cuantos votaron 'no' y cuantos no votaron

# otro para saber de los que votaron 'si':
# su genero
# semestre
# carrera

def get_answers_EIU():
    sql_script = """
        SELECT Opcion.titulo AS Titulo
        FROM Respuesta
        INNER JOIN Opcion ON Respuesta.num_pregunta = Opcion.num_pregunta
        AND Respuesta.num_opcion = Opcion.num_opcion
        AND Opcion.num_pregunta = 4
    """
    df = ct.get_table(sql_script)
    return df

def get_students_gender():
    sql_script = """
        SELECT
    """