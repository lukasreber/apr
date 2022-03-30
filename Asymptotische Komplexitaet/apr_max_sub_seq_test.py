import random
import timeit

_test_data = [
    ([1, 3, -5, 3, 3, 2, -9, -2], 8),
    ([31, -41, 59, 26, -53, 58, 97, -93, -23], 187),
    ([31, -41, 259, 26, -453, 58, 97, -93, -23], 285),
    ([41, -31, 59, -97, -53, -58, 26], 69),
    ([-97, 41, -31, 59, -97, -53, -58, 26], 69),
    ([31, -41, 59, 26, -53, 58, 97], 187),
    ([31, -41, 59, 26, -53, 58, 97, -1], 187),
    ([2, -10, 8, -10, 2], 8),
    ([41, -31, -59, -26, -13], 41),
    ([-31, -59, -26, -13, 47], 47),
    ([12], 12),
    ([1], 1),
    ([0], 0),
    ([-12], 0),
    ([-1], 0),
    ([-31, -59, -26, -13, -47], 0),
    ([], 0)
]


def run_tests(func, output=True):
    """
    runs a set of tests als specified in variable _test_data: tuples of a list of values and the expected result

    @param func: max_sub_array solution to test, func is expected to accept a parameter of type list
            and to return the maximum sum of a sub array found
            optionally followed by further parameters being ignored by the test
    @param output: boolean parameter stating whether results should be written to console
    @return: boolean value indicating whether all tests have run successful
    """
    if output:
        print('testing function ', func.__name__, end='')
    ok, param_changed = True, False
    for values, res in _test_data:
        param = values.copy()
        try:
            r = func(param)
        except BaseException as e:
            r = e
        if type(r) == list or type(r) == tuple:
            r = r[0]
        if r != res:
            ok = False
            if output:
                print('\n\ttesting with', values, 'expecting', res, 'got', r, end='')
        param_changed = param_changed or param != values
    if output:
        if param_changed:
            print('\n\tfunction changes input parameter values', end='')
        print(' -- ok' if ok and not param_changed else '\n')
    return ok


_rand_data_storage = dict()


def _rand_data(n):
    if n not in _rand_data_storage:
        _rand_data_storage[n] = [random.randint(-100, 100) for _ in range(n)]
    return _rand_data_storage[n]


def measure_times(func, last_result_only=False, number=1):
    """
    Runs func on successively growing data (amount doubled for each run) and measures time for comparison
    @param func: function to measure times for
    @param last_result_only: if True output reporting each run will be suppressed, only last run will be reported
    @param number: number of runs per measurement (default: 1 because of long duration with large data already)
    @return: None
    """
    print('\nMeasuring time of ', func.__name__)
    n = 10
    data = _rand_data(n)
    t0, t1 = 1, timeit.timeit(lambda: func(data), number=number)
    if not last_result_only:
        print(n, ' values: ', t1, 'sec')
    while t1 < 10 and n < 10000000:
        n *= 2
        t0 = t1
        data = _rand_data(n).copy()
        t1 = timeit.timeit(lambda: func(data), number=number)
        if not last_result_only:
            print(n, ' values: ', t1, 'sec, ratio: ', t1 / t0)
    if last_result_only:
        print(n, ' values: ', t1, 'sec, ratio: ', t1 / t0)
