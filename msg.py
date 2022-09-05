import random

list_of_numbers = []
list_of_numbers = [str(i) for i in range(10)]
print("Список Цифр",list_of_numbers)

list_of_letters = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','Q','W',\
'E','R','T','Y','U','I','O','P','A', 'S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
print("Cписок букв",list_of_letters)

letters_from_table = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]
print("Список букв по таблице ASCII",letters_from_table)

#получение случайного элемента из списка
import string

letters = string.ascii_letters
digits = string.digits
symbol = string.punctuation
str_elements = letters + digits + symbol
random_symbol = random.choice(string.punctuation)
list_of_elements = letters_from_table + list_of_numbers

#получение комбинации случайных элементов

length = 10

password_list = [random.choice(list_of_elements) for i in range(length)]
print("Вот он,",password_list)
#переписывается пароль строкой и добавляется символ

password = ' '
for elem in password_list:
    password = password + elem

print("ваш пароль!", password + random_symbol)