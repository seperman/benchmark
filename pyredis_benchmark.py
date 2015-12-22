#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from redis import StrictRedis, RedisError
import random
import string
import argparse
import settings

redis = StrictRedis(
    host=settings.PACMAN_REDIS_HOST,
    port=settings.PACMAN_REDIS_PORT,
    db=settings.PACMAN_REDIS_DB_NUM
    )

NUMBER_OF_KEYS_TO_MAKE = settings.PYREDIS_NUMBER_OF_KEYS_TO_MAKE
REPEAT_TEST_THIS_MANY_TIMES = settings.PYREDIS_REPEAT_TEST_THIS_MANY_TIMES


def prepare_redis():
    """fills redis with stuff"""
    stuff = {}
    for i in range(NUMBER_OF_KEYS_TO_MAKE):
        stuff['redis_benchmark.%s' % i] = ''.join([random.choice(string.ascii_letters + string.digits + '    ') for n in xrange(random.randint(1,256))])
    redis.mset(stuff)
    print ('%s keys made' % NUMBER_OF_KEYS_TO_MAKE)
    return stuff.keys()


def cleanup_redis(keys_to_be_deleted):
    redis.delete(*keys_to_be_deleted)


def test_inidividual_calls(keys):
    """Test hitting redis"""
    for key in keys:
        redis.get(key)
    cleanup_redis(keys)


def test_mget_calls(keys):
    """Test hitting redis mget"""
    redis.mget(keys)
    cleanup_redis(keys)

if __name__ == '__main__':
    import timeit
    print ("""
    #####################################################
    #          REDIS BENCHMARKING WITH PY REDIS         #
    #####################################################
    """)

    prepare_redis()
    print "repeating tests %s times." % REPEAT_TEST_THIS_MANY_TIMES
    inidividual_get_time = timeit.timeit("test_inidividual_calls(keys)", setup="from __main__ import NUMBER_OF_KEYS_TO_MAKE,test_inidividual_calls;keys=['redis_benchmark.%s' % i for i in range(NUMBER_OF_KEYS_TO_MAKE)]", number=REPEAT_TEST_THIS_MANY_TIMES)
    print("Get: Getting %s keys from redis individually took %s seconds." % (NUMBER_OF_KEYS_TO_MAKE, inidividual_get_time/REPEAT_TEST_THIS_MANY_TIMES))
    mget_time = timeit.timeit("test_mget_calls(keys)", setup="from __main__ import NUMBER_OF_KEYS_TO_MAKE,test_mget_calls;keys=['redis_benchmark.%s' % i for i in range(NUMBER_OF_KEYS_TO_MAKE)]", number=REPEAT_TEST_THIS_MANY_TIMES)
    print("Mget: Getting %s keys from redis usgin mget took %s seconds." % (NUMBER_OF_KEYS_TO_MAKE, mget_time/REPEAT_TEST_THIS_MANY_TIMES))

