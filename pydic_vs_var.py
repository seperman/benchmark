'''
Example result:
Getting dictionary key every time:
0.125132083893
Getting dictionary key and assigning it to a variable:
0.0884749889374
assigning a dictionary key value to a variable is 1.41432155455 faster
'''


def test_dict():
    thedict = {'a': 10, 'b': 20}
    for i in range(100000):
        val = thedict['a'] * 2


def test_var():
    thedict = {'a': 10, 'b': 20}
    val = thedict['a']
    for i in range(100000):
         val2 = val * 2


if __name__ == '__main__':
    print ("""
    ############################################################################
    #          DICTIONARY KEY GETTING vs. ASSIGNING KEY VALUE TO A VAR         #
    ############################################################################
    """)
    import timeit
    print('Getting dictionary key every time:')
    getting_from_dict_every_time = timeit.timeit("test_dict()", setup="from __main__ import test_dict", number=20)
    print(getting_from_dict_every_time)
    print('Getting dictionary key and assigning it to a variable:')
    assiging_key_value_to_var_time = timeit.timeit("test_var()", setup="from __main__ import test_var", number=20)
    print(assiging_key_value_to_var_time)
    print('assigning a dictionary key value to a variable is %s faster' % (getting_from_dict_every_time/assiging_key_value_to_var_time))