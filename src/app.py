import modeling.q_1 as q_1
import modeling.q_2 as q_2
import pandas as pd
from thefuzz import fuzz, process

if __name__ == '__main__':
    # q_1.answer()
    # q_2.get_qualities()

    data = {
        'nombres': ['sesar rojas', 'sexar rojas', 'samuel', 'césar rojas', 'sesar roja', 'eduardo']
    }

    df = pd.DataFrame(data)
    print(df, '\n')

    names = []

    for i in range(0, len(df)):
        for j in range(i+1, len(df)):
            ratio = fuzz.ratio(df['nombres'][i], df['nombres'][j])
            if ratio > 80:
                print(df['nombres'][i], df['nombres'][j], ratio)
                names.append(df['nombres'][i])
    
    print(names)
    