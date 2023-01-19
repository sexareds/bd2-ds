import matplotlib.pyplot as plt
import processing.q_1 as q_1

def get_students_EIU():
    df = q_1.get_students_EIU()
    df.groupby(['Respuesta']).size().plot(kind='bar', subplots=True)
    plt.title('Estudiantes que conocen el EIU')
    plt.show()

def get_students_gender():
    df = q_1.get_students_gender()
    df.groupby(['Genero']).size().plot(kind='pie', autopct='%1.1f%%')
    plt.title('Genero de estudiantes que conocen el EIU')
    plt.show()

def get_students_semester():
    df = q_1.get_students_semester()
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Semestre de estudiantes que conocen el EIU')
    plt.show()

def get_students_career():
    df = q_1.get_students_career()
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Carrera de estudiantes que conocen el EIU')
    plt.show()

def answer():
    get_students_EIU()
    get_students_gender()
    get_students_semester()
    get_students_career()