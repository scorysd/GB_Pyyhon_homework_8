import func
import time 

def base():
    while True:
        time.sleep(3)
        match input('Здравствуйте! Что вы хотите сделать? (введите цифру):\n1 --> Добавить ученика\n2 --> Удалить ученика\n3 --> Отобразить всех учеников\n4 --> Найти ученика\n5 --> Выход из программы').lower():
            case '1':
                func.add_pers()
            case '2':
                func.del_person()
            case '3':
                UI.display()
            case '4':
                func.find_person()
            case '5':
                print('До свидания!')
                exit()
            case _:
                print('Я так еще не умею(((')