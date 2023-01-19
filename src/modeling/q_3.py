import matplotlib.pyplot as plt
import processing.q_3 as q_3

def get_top_students():
    df = q_3.get_top_students()
    df['votos'].plot(kind='bar')
    plt.title('Top 15 estudiantes')
    plt.xlabel('Estudiantes')
    plt.ylabel('Votos')
    plt.show()

def get_students_semester():
    df = q_3.get_students_semester()
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Semestre de estudiantes que votaron')
    plt.show()

def get_students_career():
    df = q_3.get_students_career()
    df.groupby(['titulo']).size().plot(kind='bar', subplots=True)
    plt.title('Carrera de estudiantes que votaron')
    plt.show()

def get_answer():
    get_top_students()
    get_students_semester()
    get_students_career()