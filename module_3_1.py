# count_calls подсчитывающая вызовы остальных функций
# string_info  принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains (string, list_to_search):
    count_calls()
    string = string.lower()
    for i in list_to_search:
        count_calls()
        string = string.lower()

        for j in list_to_search:
            if string == j.lower():
                return True
            else:
                return False


print(string_info('Традесканция'))
print(string_info('Тегусигальпа'))
print(is_contains('Honduras', ['dur', 'Hond', 'ras']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(is_contains('Urban',['ban', 'BaNaN', 'urBAN']))

print(calls)

