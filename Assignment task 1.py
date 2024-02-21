def odd_values(num,arr):
    print(f'output for arr {num}:\n')
    for value in arr:
        if value % 2 != 0:
            print(value, end='')
    print('\nEnd of odd values')

arr1 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]
arr2 = [89, 52, 36, 24, 17, 99, 82, 73, 61, 48]
arr3 = [15, 13, 16, 12, 17, 11, 18, 10, 19, 9]

print(odd_values(1,arr1))
print(odd_values(2,arr2))
print(odd_values(3,arr3))






def sum_values(num,arr):
    print(f'output for arr {num}:\n')
    print(sum(arr)/len(arr))
    print('\n End of sum values')

arr1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # 1
arr2 = [17, 19, 15, 16, 14, 18, 13, 12, 11, 20] #2
arr3 = [55, 66, 77, 88, 99, 11, 22, 33, 44] #3

print(sum_values(1,arr1))
print(sum_values(2,arr2))
print(sum_values(3,arr3))


def converted_total_values(num, arr):
    print(f'output for arr {num}:\n')
    converted_total = sum(abs(value) for value in arr )
    print(f'output for arr {num}: {converted_total}')
    print('End of converted total values')

arr1 = [-10, 20, -30, 40, -50, 60, -70, 80, -90, 100] #1
arr2 = [5, -8, 13, -21, 34, -55, 89, -144, 233] #2 
arr3 = [-7, 12, -15, 18, -21, 24, -27, 30, -33] #3
arr4 = [11, -22, 33, -44, 55, -66, 77, -88, 99] #4
arr5 = [-3, 6, -9, 12, -15, 18, -21, 24, -27, 30] #5


print(converted_total_values(1,arr1))
print(converted_total_values(2,arr2))
print(converted_total_values(3,arr3))
print(converted_total_values(4,arr4))
print(converted_total_values(5,arr5))


def empty_str(num, arr): 
    print(f'output for arr {num} :')
    arr = [s for s in arr if s!=""]
    print(arr)
    print('End of empty str values')


arr1 = ['apple', '', 'banana', '', 'cherry'] #1
arr2 = ['', 'dog', '', 'cat', ''] #2
arr3 = ['hello', '', 'world', '', ''] #3
arr4 = ['', '', '', '', ''] #4
arr5 = ['one', '', 'two', '', 'three'] #5


print(empty_str(1,arr1))
print(empty_str(2,arr2))
print(empty_str(3,arr3))
print(empty_str(4,arr4))
print(empty_str(5,arr5))


def print_small_num(arr):
    if arr:
        small_num = min(arr)
        print(f'The smallest num in the list is: {small_num}')
    else:
        print('The list is empty.')


example_list = [2, -3, 20, 1, -10, 50]
print_small_num(example_list)


