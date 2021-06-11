from fib_with_log_time import power


def fib(num:int):
    f_matrix = [[1,1],[1,0]]
    if num == 0:
        return 1
    power(f_matrix, num-1)


def power(matrix, exponent):
    pass