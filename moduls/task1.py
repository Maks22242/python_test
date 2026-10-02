
def rev_str(str):
    list_str = str.split(" ")
    new_str = ""
    for i in range(len(list_str)):
        new_str += list_str[i][::-1] + " "
    return new_str

str = input("Enter a string: ")
print(rev_str(str))








