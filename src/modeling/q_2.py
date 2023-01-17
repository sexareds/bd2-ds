import matplotlib.pyplot as plt
import processing.q_2 as q_2

def get_qualities():
    df = q_2.get_qualities()
    print(df)
    # df['respuesta'].groupby(['respuesta']).size().plot(kind='pie', autopct='%1.1f%%')
    # plt.title('Cualidades de estudiantes que conocen el EIU')
    # plt.show()