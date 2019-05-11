import random
l  = []
#Generating random flight entries of 1000 flights with ID 1 to 1000
for i in range(20):
  l = l + random.sample(range(1,1001), 500)

lcopy = l[:]

import time
print("Number of flight entries :"+str(len(l)))

                    #### CODE 1 ####
print("Using simple operation")
start = time.time()
# The list v cotains all the missing flight ID's
v = [i for i in l if l.count(i)%2 != 0]
end = time.time()

# v = sorted(v)
print("One of the missing flight :"+str(v[0]))
print(" Runtime:"+str((end-start)*1000) +" milliseconds")

                    #### CODE 2 ####
print("Using collections")
start = time.time()
from collections import Counter
l = Counter(l)
l = l.most_common()
# The list v cotains all the missing flight ID's
v = [i[0] for i in l if i[1]%2 != 0]
end = time.time()

# v = sorted(v)
print("One of the missing flight :"+str(v[0]))
print(" Runtime:"+str((end-start)*1000) +" milliseconds")


###The solution may differ becasue the first element of list v may differ by code ###
### uncomment the sorting the list v for same answer

def test_random_lists():
    '''
    Generates 20 lists of random sizes within
    the range - 5, 10, inclusive.Modify these as per your choice 
    '''
    tcount = 2
    low = 1
    high = 2000000
    size_variation = [100000]

    def exp_func(alist):
        print("\n", alist[: 10], "...")
    
        
    import random# help(random)
    for test_num in range(tcount):
        unique = random.randint(low, high)
        use_it = random.choice([True, False])
        size = random.choice(size_variation)

        alist = []
        for count in range(size): 
            rand = random.randint(low, high)
            if rand != unique: 
                alist.extend([rand, rand])
                
        if use_it: 
            loc = random.randint(0, size) 
            print("inserting unique at loc", loc)
            alist.insert(loc, unique)
        
        random.shuffle(alist)
    
        # Use `alist` for testing your code as required
        # your asserts go below
        # Modify / delete the print() as you deem fit
        #
        print("Test", test_num, len(alist), exp_func(alist))
        start = time.time()
        if use_it: 
            assert unique == missing_plane(alist)
        else: 
            assert 0 == missing_plane(alist) 
        end = time.time()
        print(" Runtime:", (end-start)*1000, "milliseconds")


def missing_plane(alist):
	import operator
	from functools import reduce
	return reduce(operator.xor, alist)
	# print(v)

print("------ Testing 10,00,000 entries, twice")
print("")
test_random_lists()

