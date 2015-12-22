# Benchmarking

# Install

1. Clone the repo
2. Copy settings_sample.py to settings.py and modify it for your setup

# PyRedis

1. Make sure you have pyredis installed: `pip install pyredis`
2. run `./pyredis_benchmark.py`

Example result:

```
    #####################################################
    #          REDIS BENCHMARKING WITH PY REDIS         #
    #####################################################

10 keys made
repeating tests 100 times.
Get: Getting 10 keys from redis individually took 0.0286107707024 seconds.
Mget: Getting 10 keys from redis usgin mget took 0.00733426094055 seconds.
```
