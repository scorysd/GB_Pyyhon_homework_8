import pandas as pd

def add_pers():
    df = pd.read_csv('database.csv', index_col=0)
    add_pers= {
    'Surname': input("Введите фамилию ученика:"),
    'Name': input("Введите имя ученика:"),
    'Age': input("Введите возраст ученика:"),
    'Sex': input("Введите пол ученика:"),
    'Class': input("Введите класс ученика:"),
    'Status': input("Введите статус по оценкам ученика:"),
    'sit_position': input("Введите место в классе ученика:")
    }
    df = df.append(add_pers, ignore_index=True)
    print(df)
    df.to_csv('database.csv')

def find_person():   
    df = pd.read_csv('database.csv', index_col=0)
    print(df[lambda x: x['Surname'] == input('Введите фамилию ученика:')])
  