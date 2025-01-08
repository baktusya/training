def apply_all_func(int_list, *functions):
    results = {}

    for func in functions:
        func_name = func.__name__
        results[func_name] = func(int_list)

    return results

def min_func(lst):
  return min(lst)

def max_func(lst):
  return max(lst)

def len_func(lst):
  return len(lst)

def sum_func(lst):
  return sum(lst)

def sorted_func(lst):
  return sorted(lst)


#int_list = [1, 6, 8, 3, 5, 7, 3.5, 9, 2.1]

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))




