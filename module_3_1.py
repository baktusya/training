calls = 0
def count_calls ():
    calls += 1    # количество вызовов этих двух функций
def string_info(string):
    global calls
    calls += 1
    string = tuple([len(string), string.upper(), string.lower()])
    return string
def is_contains(string, list_to_search):
    global calls
    calls += 1
    list_to_search = [word.lower() for word in list_to_search]
    string = string.lower()
    return string in list_to_search

print(string_info('колонада'))
print(string_info('банан'))
print(is_contains('вода', ['куКУруза', 'КОлодец', 'воДа', 'аПельСин']))
print(calls)