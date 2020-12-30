'''
Example result:
    ############################################################################
    #                             HASHES COMPARISON                            #
    ############################################################################

sha256:
0.0032799430191516876
mmh3:
0.0007216100057121366
mmh3 is 4.545312555519243 faster than sha256
'''
import random
import string
import mmh3
from hashlib import sha256


def get_random_string():
    string_len = random.randint(128, 1024)
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(string_len)).encode('utf-8')


print("getting random strings")

RANDOM_STRINGS = [get_random_string() for i in range(2000)]

rand_generator1 = iter(RANDOM_STRINGS)
rand_generator2 = iter(RANDOM_STRINGS)


def test_sha256():
    text = next(rand_generator1)
    sha256(text).hexdigest()


def test_mmh3():
    text = next(rand_generator2)
    mmh3.hash128(text, 1234)


if __name__ == '__main__':
    print ("""
    ############################################################################
    #                             HASHES COMPARISON                            #
    ############################################################################
    """)
    import timeit
    print('sha256:')
    sha256_time = timeit.timeit("test_sha256()", setup="from __main__ import test_sha256", number=2000)
    print(sha256_time)
    print('mmh3:')
    mmh3_time = timeit.timeit("test_mmh3()", setup="from __main__ import test_mmh3", number=2000)
    print(mmh3_time)
    print('mmh3 is %s faster than sha256' % (sha256_time/mmh3_time))
