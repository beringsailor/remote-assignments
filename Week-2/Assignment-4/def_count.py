def count(input):
    count_a = 0
    count_b = 0
    count_c = 0
    count_x = 0
    for alphabet in input:
        if alphabet == 'a':
            count_a += 1
        elif alphabet == 'b':
            count_b += 1
        elif alphabet == 'c':
            count_c += 1
        elif alphabet == 'x':
            count_x += 1
        else:
            pass
    return {
          'a': count_a, 
          'b': count_b, 
          'c': count_c, 
          'x': count_x 
    }

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

# def group_by_key(input):
# # your code here

# input2 = [
# {'key': 'a', 'value': 3},
# {'key': 'b', 'value': 1},
# {'key': 'c', 'value': 2},
# {'key': 'a', 'value': 3},
# {'key': 'c', 'value': 5}
# ]

# print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}
