#!/usr/bin/env python3
from string import digits
from random import choice

DIGITS_LIST = [3, 7, 1, 5, 0, 2, 9, 6]
RANDOM_LIST = [choice(digits) for _ in range(24)]


# v1

def sort_digits_list(_list):

  unit = 1
  key = int()
  length = (_list.__len__() - unit)

  for _ in range(length):

    for digit in _list:

      key = key.__add__(unit)

      if key.__lt__(length + unit) \
      and digit.__gt__(_list.__getitem__(key)):

        tmp = _list.__getitem__(key)

        _list.__setitem__(key, digit)
        _list.__setitem__(key - unit, tmp)

    key = int()

  return _list


# v2

def sort_digits_list(_list):
  return _list.sort()


# test

print(sort_digits_list(DIGITS_LIST))
