#!/usr/bin/pyhton3
"""
FizzBuzz
"""

import sys

def fizzBuzz(n):
    """
    Prints numbers from 1 to n separated by a space.
        -- For multiples of 3 prints "Fizz" intead of the number of
        and for multio\ples of 5 prints "Buzz".
        -- For numbera that are multiples for both 3 and 5 prints "FizzBuzz". 
    """

    if n < 1:
        return

    tmp_result  = []

    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
        print(" ".join(tmp_result))

    if __name__ == '__main__':
        if len(sys.argv) <= 1:
            print("Missing number")
            print("Usage: ./0-fizzbuzz.py <number>")
            print("Example: ./0-fizzbuzz.py 89")
            sys.exit(1)

        number = int(sys.argv[1])
        fizzBuzz(number)