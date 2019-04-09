def test_random_lists():
    '''
    Generates 20 lists of random sizes within
    the range -5, 10, inclusive. Modify these as per your choice
    '''
    tcount = 20
    low = -5
    high = 10
    size_variation = [3, 5, 6, 20, 1000]

    def exp_func(alist):
        return "TBD"
    import random
    # help(random)
    for test_num in range(tcount):
        alist = [random.randint(low, high)
                 for count in range(
                     random.choice(size_variation)
        )
        ]
        print(("Test " + str(test_num), len(alist), exp_func(alist)),
              end="...\n"
              )

        # Use `alist` for testing your function as required
        # your asserts go below
        #
