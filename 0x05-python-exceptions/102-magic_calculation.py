#!/usr/bin/env python

def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            result = result + (a ** b / i)
        except:
            result = result + a + b
            break
        return (result)

    if __name__ == "__main__":
        a = 5
        b = 2
        result = magic_calculation(a, b)
        print(result)
