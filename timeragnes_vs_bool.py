'''
Timerange checking vs. bool

Example result:

############################################################################
#          CHECKING TIME RANGES VS. BOOLEANS                               #
############################################################################

Checking if number is in any of the ranges.
0.176210165024
Checking if bool is True
0.0246558189392
Checking if boolean is True is 7.14679830584 faster than checking time ranges.
'''
import random


def create_time_range():
    ranges = []
    begin = 0
    for i in range(random.randint(2, 6)):
        begin = random.randint(begin, begin + 200)
        end = random.randint(begin, begin + 300)
        ranges.append((begin, end))
    return ranges


def check_time_range(ranges, number):
    for i in range(1):
        for slot in ranges:
            if number >= slot[0] and number <= slot[1]:
                return True


def check_if_bool_is_true(Boolean):
    for i in range(1):
        if Boolean:
            return True


if __name__ == '__main__':
    print ("""
    ############################################################################
    #          CHECKING TIME RANGES VS. BOOLEANS                               #
    ############################################################################
    """)
    import timeit
    print('Checking if number is in any of the ranges.')
    checking_ranges_time = timeit.timeit("check_time_range(create_time_range(), random.randint(200, 600))", setup="from __main__ import random, check_time_range, create_time_range", number=3000)
    print(checking_ranges_time)
    print('Checking if bool is True')
    checking_bool_time = timeit.timeit("check_if_bool_is_true(bool(random.randint(0, 1)))", setup="from __main__ import random, check_if_bool_is_true", number=3000)
    print(checking_bool_time)
    print('Checking if boolean is True is %s faster than checking time ranges.' % (checking_ranges_time/checking_bool_time))
