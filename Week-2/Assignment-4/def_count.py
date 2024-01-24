def count(input):
    count = {}
    for alphabet in input:
        if alphabet in count:
            count[alphabet] += 1
        else:
            count[alphabet] = 1
    
    return count

input1 = ['a', 'b', 'c', 'a', 'c', 'a', 'x']
print(count(input1)) # should print {'a': 3, 'b': 1, 'c': 2, 'x': 1}

# old code
# def count(input):
#     count_a = 0, count_b = 0, count_c = 0, count_x = 0
#     for alphabet in input:
#         if alphabet == 'a':
#             count_a += 1
#         elif alphabet == 'b':
#             count_b += 1
#         elif alphabet == 'c':
#             count_c += 1
#         elif alphabet == 'x':
#             count_x += 1
#         else:
#             pass
#     return {
#           'a': count_a, 'b': count_b, 'c': count_c, 'x': count_x 
#     }
