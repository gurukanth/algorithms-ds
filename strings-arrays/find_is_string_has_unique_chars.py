
def has_unique_chars_brute_force(string:str):
    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True


assert False == has_unique_chars_brute_force('HelloWorld')
assert True == has_unique_chars_brute_force('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
test_code = '''
def test():
    return   has_unique_chars_brute_force('abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ')
'''
import timeit
time = timeit.Timer(stmt=test_code).timeit()
print(time)
