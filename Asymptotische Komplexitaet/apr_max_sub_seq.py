from apr_max_sub_seq_test import run_tests, measure_times


def max_sub_seq_pythonic(data):
    return max([0] + [sum(data[start:end + 1]) for start in range(len(data)) for end in range(start, len(data))])


def max_sub_seq_1(data):
    max_sum, max_start, max_end = 0, 0, 0
    start = 0
    while start < len(data):
        end = start
        while end < len(data):
            cur_sum, i = 0, start
            while i <= end:
                cur_sum, i = cur_sum + data[i], i + 1
            if cur_sum > max_sum:
                max_sum, max_start, max_end = cur_sum, start, end
            end = end + 1
        start = start + 1
    return max_sum, max_start, max_end


def max_sub_seq_2(data):
    max_sum, max_start, max_end = 0, 0, 0
    start = 0
    while start < len(data):
        cur_sum, end = 0, start
        while end < len(data):
            cur_sum = cur_sum + data[end]
            if cur_sum > max_sum:
                max_sum, max_start, max_end = cur_sum, start, end
            end = end + 1
        start = start + 1
    return max_sum, max_start, max_end


def max_sub_seq_3(data):
    max_sum, max_start, max_end, cur_sum, end = 0, 0, 0, 0, 0
    while end < len(data):
        if cur_sum > 0:
            cur_sum = cur_sum + data[end]
        else:
            cur_sum, start = data[end], end
        if cur_sum > max_sum:
            max_sum, max_start, max_end = cur_sum, start, end
        end = end + 1
    return max_sum, max_start, max_end


def max_sub_seq_1_py(data):
    max_sum, max_start, max_end = 0, 0, 0
    for start in range(len(data)):
        for end in range(start, len(data)):
            cur_sum = sum(data[start:end + 1])
            if cur_sum > max_sum:
                max_sum, max_start, max_end = cur_sum, start, end
    return max_sum, max_start, max_end


def max_sub_seq_2_py(data):
    max_sum, max_start, max_end = 0, 0, 0
    for start in range(len(data)):
        cur_sum = 0
        for end in range(start, len(data)):
            cur_sum = cur_sum + data[end]
            if cur_sum > max_sum:
                max_sum, max_start, max_end = cur_sum, start, end
    return max_sum, max_start, max_end


def max_sub_seq_3_py(data):
    max_sum, max_start, max_end, cur_sum = 0, 0, 0, 0
    for end in range(len(data)):
        if cur_sum > 0:
            cur_sum = cur_sum + data[end]
        else:
            cur_sum, start = data[end], end
        if cur_sum > max_sum:
            max_sum, max_start, max_end = cur_sum, start, end
    return max_sum, max_start, max_end


def max_sub_seq_divide_and_conquer(data):
    def max_in_range(r):
        max_sum, s = 0, 0
        for i in r:
            s = s + data[i]
            if s > max_sum:
                max_sum = s
        return max_sum

    def max_sub_seq_part(beg, end):
        if beg == end:
            return max(0, data[beg])
        else:
            m = (beg + end) // 2
            return max(max_sub_seq_part(beg, m), max_sub_seq_part(m + 1, end),
                       max_in_range(range(m, beg - 1, -1)) + max_in_range(range(m + 1, end + 1)))

    return max_sub_seq_part(0, len(data) - 1) if len(data) > 0 else 0


def test_all_func():
    run_tests(max_sub_seq_pythonic)
    run_tests(max_sub_seq_1)
    run_tests(max_sub_seq_2)
    run_tests(max_sub_seq_3)
    run_tests(max_sub_seq_1_py)
    run_tests(max_sub_seq_2_py)
    run_tests(max_sub_seq_3_py)
    run_tests(max_sub_seq_divide_and_conquer)


def measure_all_times(only_last=False, number=1):
    measure_times(max_sub_seq_3, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_3_py, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_2, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_2_py, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_1, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_1_py, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_pythonic, last_result_only=only_last, number=number)
    measure_times(max_sub_seq_divide_and_conquer, last_result_only=only_last, number=number)


def main():
    test_all_func()
    measure_all_times()


if __name__ == '__main__':
    main()
