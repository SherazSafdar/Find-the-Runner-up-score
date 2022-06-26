def find_value(list_values):
    high = list_values[0]
    second_high = list_values[0]
    for item in list_values:
        if high<item:
            second_high = high
            high = item
        elif second_high<item:
            second_high = item
    
    return second_high
list_values = [4, 3, 5, 1, 9, 12, 11]
ans = find_value(list_values)
print("return value is")
print(ans)
                

