my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
positive_numbers = []
start_variable = 0

while start_variable < len(my_list):

    if my_list[start_variable] > 0:
        positive_numbers.append(my_list[start_variable])
        if start_variable < len(positive_numbers):
            print(positive_numbers[start_variable])
            start_variable += 1
            if start_variable == len(my_list) or my_list[start_variable] < 0:
                break
            
        
    else:
        start_variable += 1
