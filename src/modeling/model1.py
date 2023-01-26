import matplotlib.pyplot as plt
import processing.process1 as p1

def get_students_EIU():
    df = p1.get_students_EIU()
    if df.empty: return
    df.groupby(['Respuesta']).size().plot(kind='pie', subplots=True, autopct='%1.1f%%')
    plt.title('Estudiantes que conocen el EIU')
    plt.show()

def get_students_gender():
    df = p1.get_students_gender()
    if df.empty: return
    df.groupby(['Genero']).size().plot(kind='pie', subplots=True, autopct='%1.1f%%')
    plt.title('Genero de estudiantes que conocen el EIU')
    plt.show()

def get_students_semester():
    df = p1.get_students_semester()
    if df.empty: return
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Semestre de estudiantes que conocen el EIU')
    plt.show()

def get_students_semester_2():
    df = p1.get_students_semester_2()
    if df.empty: return
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Semestre de estudiantes que no conocen el EIU')
    plt.show()

def get_students_career():
    df = p1.get_students_career()
    if df.empty: return
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Carrera de estudiantes que conocen el EIU')
    plt.show()

def get_students_career_2():
    df = p1.get_students_career_2()
    if df.empty: return
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Carrera de estudiantes que no conocen el EIU')
    plt.show()

def get_answer():
    get_students_EIU()
    get_students_gender()
    get_students_semester()
    get_students_semester_2()
    get_students_career()
    get_students_career_2()