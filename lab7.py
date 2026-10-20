def find_second_largest(numbers):
    uniqe_numbers = list(set(numbers))
    if len(uniqe_numbers) < 2:
        return None
    uniqe_numbers.sort() 
    return uniqe_numbers[-2]
my_list = [10, 20, 4, 45, 99, 99, 45]
result = find_second_largest(my_list)
print(f"Второй по величине элемент: {result}")