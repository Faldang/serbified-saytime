#!/usr/bin/env python3
# saytime.py by Bill Weinman [http://bw.org/]
# created for Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
# Serbian additions by Marko D. Lukac (Faldang)

import time

def day():
        a = {"Monday":"Ponedeljak",
                 "Tuesday":"Utorak",
                 "Wednesday":"Sredu",
                 "Thursday":"Cetvrtak",
                 "Friday":"Petak",
                 "Saturday":"Subotu",
                 "Sunday":"Nedelju"}
        return a[time.strftime("%A")] + " "
    
def mth():
    t = time.localtime()
    months = ["Januara", "Februara", "Marta", "Aprila", "Maja", "Juna", "Jula",
              "Avgusta", "Septembra", "Oktobra", "Novembra", "Decembra"]
    return months[t.tm_mon-1]

def main():
    pass

if __name__ == '__main__':
    main()