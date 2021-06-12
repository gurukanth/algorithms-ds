
def has_unique_chars_brute_force(string:str):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

def has_unique_chars_ext_ds(string:str):
    char_set = set(string)
    if len(string) == len(char_set):
        return True
    else:
        return False

def has_unique_chars_sort(string:str):
    sorted(string)
    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False
    return True

def has_unique_chars_checker_bit(string:str):
    checker = 0
    for char in string:
        order = ord(char) - ord('a')
        print('checker:' + str(checker))
        print('left shift:' + str(1<<order))
        print('condition-result:' + str(checker & 1<<order))
        if (checker & (1<<order)) > 0:
            return False
        
        checker |= 1<<order
    return True


has_unique_chars_checker_bit('hello')

assert False == has_unique_chars_ext_ds('Hello')
assert True == has_unique_chars_ext_ds('H')
assert False == has_unique_chars_ext_ds('HeloGuru')
assert True == has_unique_chars_ext_ds('abcdefghijkABCDEFIJK')


# string = ''
# for i in range(1, 2000):
#     string += chr(i)

# import timeit

# time = timeit.default_timer()
# print(has_unique_chars_brute_force(string))
# print(timeit.default_timer() - time)

# time = timeit.default_timer()
# print(has_unique_chars_ext_ds(string))
# print(timeit.default_timer() - time)

# time = timeit.default_timer()
# print(has_unique_chars_sort(string))
# print(timeit.default_timer() - time)

##############Test cases#######################


# assert False == has_unique_chars_brute_force('HelloWorld')
# assert False == has_unique_chars_ext_ds('HelloWorld')
# assert False == has_unique_chars_sort('HelloWorld')

# assert True == has_unique_chars_ext_ds('Helo Guys')
# assert True == has_unique_chars_brute_force('Helo Guys')
# assert True == has_unique_chars_sort('Helo Guys')

# assert True == has_unique_chars_brute_force('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# assert True == has_unique_chars_ext_ds('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
# assert True == has_unique_chars_sort('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# test_code = '''
# def test():
#     return   has_unique_chars_brute_force('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-')
# '''
# import timeit
# time = timeit.Timer(stmt=test_code).timeit()
# print(time)

# test_code2 = '''
# def test():
#     return   has_unique_chars_ext_ds('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-')
# '''
# time = timeit.Timer(stmt=test_code2).timeit()
# print(time)

# test_code3 = '''
# def test():
#     return   has_unique_chars_sort('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-')
# '''
# time = timeit.Timer(stmt=test_code3).timeit()
# print(time)
