#!/usr/bin/python3
# saytime.py by Bill Weinman [http://bw.org/]
# created for Python 3 Essential Training on lynda.com
# Copyright 2010 The BearHeart Gorup, LLC
import sys
import time

__version__ = "1.1.0"

class numwords():
    """
        return a number as words,
        e.g., 42 becomes "forty-two"
    """
    _words = {
        'ones': (
            'nula', 'jedan', 'dva', 'tri', 'cetiri', 'pet', 'sest', 'sedam', 'osam', 'devet'
        ), 'tens': (
            '', 'deset', 'dvadeset', 'trideset', 'cetrdeset', 'pedeset', 'sezdeset', 'sedamdeset', 'osamdeset', 'devedeset'
        ), 'teens': (
            'deset', 'jedanaest', 'dvanaest', 'trinaest', 'cetrnaest', 'petnaest', 'sesnaest', 'sedamnaest', 'osamnaest', 'devetnaest' 
        ), 'quarters': (
            ('', 'sat' ,'sata', 'sata', 'sata', 'sati', 'sati', 'sati', 'sati', 'sati', 'sati', 'sati', 'sati') ,
            'cetvrt', 'pola'
        ), 'range': {
            'hundred': 'stotina'
        }, 'misc': {
            'minus': 'minus'
        }
    }
    _oor = 'OOR'    # Out Of Range

    def __init__(self, n):
        self.__number = n;

    def numwords(self, num = None):
        "Return the number as words"
        n = self.__number if num is None else num
        s = ''
        if n < 0:           # negative numbers
            s += self._words['misc']['minus'] + ' '
            n = abs(n)
        if n < 10:          # single-digit numbers
            s += self._words['ones'][n]  
        elif n < 20:        # teens
            s += self._words['teens'][n - 10]
        elif n < 100:       # tens
            m = n % 10
            t = n // 10
            s += self._words['tens'][t]
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        elif n < 1000:      # hundreds
            m = n % 100
            t = n // 100
            if t==1: s += 'sto'
            elif t==2: s += 'dve stotine'
            else: s += self._words['ones'][t] + ' ' + self._words['range']['hundred']
            if m: s += ' ' + numwords(m).numwords()    # recurse for remainder
        else:
            s += self._oor
        return s

    def number(self):
        "Return the number as a number"
        return str(self.__number);

class saytime(numwords):
    """
        return the time (from two parameters) as words,
        e.g., fourteen til noon, quarter past one, etc.
    """

    _specials = {
        'noon': 'podne',
        'midnight': 'ponoc',
        'til': 'do',
        'past': 'i',
        'tilmidnight': 'ponoci'
    }

    def __init__(self, h, m):
        self._hour = abs(int(h))
        self._min = abs(int(m))

    def words(self):
        h = self._hour
        m = self._min
        
        if h > 23: return self._oor     # OOR errors
        if m > 59: return self._oor

        sign = self._specials['past']        
        
        if self._min >= 30:
            sign = self._specials['til']
            h += 1
            m = 60 - m
        if h > 23: h -= 24
        elif h > 12: h -= 12
        if self._min == 30: return "pola {}".format(self.numwords(h))

        # hword is the hours word)
        hcond = (h is 0 and m is 0) or (h is 0 and m is 15 and sign is 'do')
        if hcond and sign is 'do': hword = self._specials['tilmidnight']
        elif (h is 0 and m is 0): hword = self._specials['midnight']
        elif h is 12 and (self._min>=30 or self._min==0): hword = self._specials['noon']
        elif h is 0: hword = self.numwords(h+12)
        else: hword = self.numwords(h)

        if m is 0:
            if h is 0: return hword   # for noon and midnight
            elif h is 12: return hword
            else: return "{} {}".format(self.numwords(h), self._words['quarters'][m][h])
        if m % 15 is 0:
            if self._min >= 30: return "{} {} {}".format(self._words['quarters'][m // 15], sign, hword) 
            else: return "{} {} {}".format(hword, sign, self._words['quarters'][m // 15]) 
        if self._min >= 30: return "{} {} {}".format(self.numwords(m), sign, hword)
        return "{} {} {}".format(hword, sign, self.numwords(m),) 

    def digits(self):
        "return the traditionl time, e.g., 13:42"
        return "{:02}:{:02}".format(self._hour, self._min)

class saytime_t(saytime):   # wrapper for saytime to use time object
    """
        return the time (from a time object) as words
        e.g., fourteen til noon
    """
    def __init__(self, t):
        self._hour = t.tm_hour
        self._min = t.tm_min

def main():
    test()
    if len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            test()
        else:
            try: print(saytime(*(sys.argv[1].split(':'))).words())
            except TypeError: print("Invalid time ({})".format(sys.argv[1]))
    else:
        print(saytime_t(time.localtime()).words())

def test():
    print("\nnumbers test:")
    list = (
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 19, 20, 30, 
        50, 51, 52, 55, 59, 99, 100, 101, 112, 200, 253, 900, 999, 1000 
    )
    for l in list:
        print(l, numwords(l).numwords())

    print("\ntime test:")
    list = (
        (0, 0), (0, 1), (11, 0), (12, 0), (13, 0), (12, 29), (12, 30),
        (12, 31), (12, 15), (14, 30), (12, 45), (11, 59), (23, 15), 
        (23, 59), (12, 59), (13, 59), (1, 60), (24, 0)
    )
    for l in list:
        print(saytime(*l).digits(), saytime(*l).words())

    print("\nlocal time is " + saytime_t(time.localtime()).words())

if __name__ == "__main__": main()