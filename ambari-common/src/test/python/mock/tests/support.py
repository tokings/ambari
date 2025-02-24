#!/usr/bin/env python3
import sys

info = sys.version_info
if info[:3] >= (3, 2, 0):
  # for Python 3.2 ordinary unittest is fine
  import unittest as unittest2
else:
  import unittest2


try:
  callable = callable
except NameError:

  def callable(obj):
    return hasattr(obj, "__call__")


inPy3k = sys.version_info[0] == 3
with_available = sys.version_info[:2] >= (2, 5)


def is_instance(obj, klass):
  """Version of is_instance that doesn't access __class__"""
  return issubclass(type(obj), klass)


class SomeClass(object):
  class_attribute = None

  def wibble(self):
    pass


class X(object):
  pass


try:
  next = next
except NameError:

  def next(obj):
    return obj.__next__()
