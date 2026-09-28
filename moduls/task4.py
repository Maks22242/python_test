#сумма числовых элементов в заданном списке

def sum_in_list(items):
    total = 0
    for item in items:
        if isinstance(item,(int, float)):
            total += item
    return total

print(sum_in_list([1,2,3,4,"hello",5.3]))