#!/usr/bin/env python3
import collections

my_counter = collections.Counter()

def log_and_count(key=None, counts = my_counter):
    def dec(func):
        def inner(*args,**kwargs):
            if (func.__name__=='f1'):
                counts["basic"] += 1
            elif (func.__name__=='f2'):
                counts[func.__name__] += 1  
            else:
                counts[func.__name__] += 1
            #Counter=my_counter.update({('basic functions' if key == 'basic functions' else func.__name__): 1})
                #under task solution print(my_counter)  -> Counter({'basic function': 5, 'f3': 2})
                #athena -> Counter() ERROR
            print("called {} with {} and {}".format(func.__name__,args,kwargs))
            return func(*args,**kwargs)
        return inner
    return dec

@log_and_count(key = 'basic functions', counts = my_counter)
def f1(a, b=2):
    return a ** b

@log_and_count(key = 'basic functions', counts = my_counter)
def f2(a, b=3):
    return a ** 2 + b

@log_and_count(counts = my_counter)
def f3(a, b=5):
    return a ** 3 - b

f1(2)
f2(2, b=4)
f1(a=2, b=4)
f2(4)
f2(5)
f3(5)
f3(5,4)
print(my_counter)
