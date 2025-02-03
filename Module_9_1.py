def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results.update({func.__name__: func(int_list)})
    return results

    def min(int_list):
        i =0
        for i in range((int_list)-1):
            if int_list[i]<int_list[i+1]:
                result = int_list[i]
        return result

    def max(int_list):
        i =0
        for i in range((int_list)-1):
            if int_list[i]>int_list[i+1]:
                result = int_list[i]
        return result

    def len(int_list):
        return len(int_list)

    def sum(int_list):
        result = 0
        for i in int_list:
            result +=i
        return result

    def sorted(int_list):
        return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))