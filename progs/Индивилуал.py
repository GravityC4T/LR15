#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def start_sum(start):
    def wrapper(func):
        def wrapped(*args):
            print("Entering the wrapper with start value of " +str(start))
            print("Processing wrapped function: " +str(func))
            string = args[0]
            lst = string.split()
            lst = lst[start:]
            start_string = " ".join(lst)
            return_sum = func(start_string)
            print("Returning from wrapper")
            return return_sum
        return wrapper
    return decorator


#@start_sum(start=5)
def str_summary(string):
    a = [int(s) for s in string.split()]
    summary = sum(elem for elem in a)
    return summary


if __name__ == "__main__":
    string_inp = input("Enter the str numbers: ")
    print("The sum is: " +str(str_summary(string_inp)))
