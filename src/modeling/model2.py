import matplotlib.pyplot as plt
import squarify
import processing.process2 as p2

def get_qualities():
    df = p2.get_qualities()
    if df.empty: return
    df = df.groupby(['respuesta']).size().reset_index(name='counts')
    squarify.plot(label=df['respuesta'], sizes=df['counts'], alpha=.7)
    plt.show()

def get_most_relevant_qualities():
    df = p2.get_qualities()
    if df.empty: return
    df = df.value_counts().reset_index(name='counts')
    df = df.set_index('respuesta').head(10)
    df['counts'].plot(kind='bar')
    plt.title('Cualidades más relevantes')
    plt.xlabel('Cualidades')
    plt.ylabel('Cantidad')
    plt.show()

def get_answer():
    get_qualities()
    get_most_relevant_qualities()