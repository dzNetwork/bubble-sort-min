#!/usr/bin/env python3


# v1-dznet

def sort_digits_list(_list):

  for _ in _list:

    key = int()

    for digit in _list:

      key = key.__add__(int(1))

      if key.__lt__(_list.__len__()) \
      and digit.__gt__(_list.__getitem__(key)):

        tmp = _list.__getitem__(key)

        _list.__setitem__(key, digit)
        _list.__setitem__(key - int(1), tmp)

  return _list


# v2-buildin

def buildin_sort(_list):
  return _list.sort()


# test

from string import digits
from random import choice

def gen_random_list(size=int(16)):
  return list(map(lambda x: choice(digits), range(int(size))))


print(sort_digits_list(gen_random_list()))
