#!/usr/bin/env python3
from string import digits
from random import choice

DIGITS_LIST = [3, 7, 1, 5, 0, 2, 9, 6]
RANDOM_LIST = [choice(digits) for _ in range(24)]


# v1-dznet

def sort_digits_list(_list):

  _int = int(1)
  key = int()

  for _ in _list:

    for digit in _list:

      key = key.__add__(_int)

      if key.__lt__(_list.__len__()) \
      and digit.__gt__(_list.__getitem__(key)):

        tmp = _list.__getitem__(key)

        _list.__setitem__(key, digit)
        _list.__setitem__((key - _int), tmp)

    key = int()

  return _list


# v2-buildin

def buildin_sort(_list):
  return _list.sort()


# test

print(sort_digits_list(DIGITS_LIST))
