#w1 assignment3

def find_max(numbers):
    try: 
        max_num = numbers[0]
        for num in numbers:
            if num > max_num:
                max_num = num
        return(max_num)
    except IndexError:
        return "No number in array"

print(find_max([1,2,4,5]))
print(find_max([5, 2, 7, 1, 6]))
print(find_max([]))

#------------------------------------

# def find_position(numbers, target):
#     for num_index, num in enumerate(numbers):
#         list_of_index = []
#         if num == target:
#             list_of_index.append(num_index)
#             if list_of_index == []:
#                 print(-1)
#             else:
#                 print(list_of_index[0])

# list_of_index = []

# def find_position(numbers, target):
#     for num_index, num in enumerate(numbers):
#         if num == target:
#             print(num_index)
#         else: 
#             print(-1)

def find_position(numbers, target):
    result = -1
    index = 0
    for num in numbers:
        if num == target:
            result = index
            break
        else: 
            index = index + 1
    return result

print(find_position([5, 2, 7, 1, 6], 5)) # should print 0
print(find_position([5, 2, 7, 1, 6], 7)) # should print 2
print(find_position([5, 2, 7, 7, 7, 1, 6], 7)) # should print 2 (the first one)
print(find_position([5, 2, 7, 1, 6], 8)) # should print -1
