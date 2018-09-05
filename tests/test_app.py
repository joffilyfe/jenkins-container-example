import unittest
from app import say_hello
import pdb

#pdb.set_trace()

class BasicTest(unittest.TestCase):
  '''basic example tests'''

  def test_should_say_hello_world(self):
    self.assertEqual('hello world', say_hello())
