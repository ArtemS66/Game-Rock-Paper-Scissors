import random #импортирую модуль random

winner = ''
user_choice = ''
spisok = ['камень', 'ножницы', 'бумага']
computer_choice= random.choice(spisok)  #прописываю глобальные переменные

while (user_choice != 'камень' and user_choice != 'ножницы' and user_choice != 'бумага'):
    user_choice = input('Выберите знак: камень, ножницы или бумага')  #запрашиваю выбор игрока

if computer_choice == user_choice:
    winner = 'Ничья'
elif computer_choice == 'камень' and user_choice == 'ножницы':
    winner = 'компьютер'
elif computer_choice == 'ножницы' and user_choice == 'бумага':
    winner = 'компьютер'
elif computer_choice == 'бумага' and user_choice == 'камень':
    winner = 'компьютер'
else:
    winner = 'игрок'   #логика определения победителя

if winner == 'Ничья':
    print('Ничья')
else:
    print('Победил ', winner, 'компьютер выбрал', computer_choice)
