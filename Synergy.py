print('Введите пятизначное число.')

number = input()

position_edenicy = int(number) % 10
position_desiatki = int(number) // 10 % 10
position_sotni = int(number) // 100 % 10
position_tysiachi = int(number) // 1000 % 10
position_des_tysiach = int(number) // 10000 % 10

print(((position_desiatki ** position_edenicy) * position_sotni) / (position_des_tysiach - position_tysiachi))