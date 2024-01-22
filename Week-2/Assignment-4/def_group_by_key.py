def group_by_key(input):
    sum_a = 0
    sum_b = 0
    sum_c = 0
    for dics in input:
        if dics['key'] == 'a':
            sum_a += dics['value']
        elif dics['key'] == 'b':
            sum_b += dics['value']
        elif dics['key'] == 'c':
            sum_c += dics['value']
        else:
            pass
    return {
          'a': sum_a, 
          'b': sum_b, 
          'c': sum_c, 
    }

input2 = [
{'key': 'a', 'value': 3},
{'key': 'b', 'value': 1},
{'key': 'c', 'value': 2},
{'key': 'a', 'value': 3},
{'key': 'c', 'value': 5}
]

print(group_by_key(input2)) # should print {‘a’: 6, ‘b’: 1, ‘c’: 7}