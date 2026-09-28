
#Наоходи самое длинное слово в строке
def lond_in_str(str):
    split_str = str.split(" ")
    long_word = split_str[0]
    for i in range(len(split_str)):
        if len(long_word) < len(split_str[i]):
            long_word = split_str[i]
    return long_word


str = input("Enter a string: ")
print('Самое длинное слово в строке: '+ lond_in_str(str))
