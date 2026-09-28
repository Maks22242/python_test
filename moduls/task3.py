# Проверка строки на полиндром
def check_str_polindrom(str):
    str = str.replace(" ", "")
    str = str.lower()
    newstr = ""
    for i in range(len(str)):
        if str[i].isalnum():
            newstr += str[i]
    return newstr[::-1] == newstr

str = input("Enter a string: ")
if check_str_polindrom(str):
    print("Строка является плиндромом")
else:
    print("Строка не является плиндромом")
