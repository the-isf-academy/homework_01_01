# Unit 1 Lesson 1 Test script
# Author: Chris Proctor
# --------------------
# YOU DO NOT NEED TO UNDERSTAND THIS CODE RIGHT NOW!
# This script imports all the functions from your homework and tests them out. Hopefully they work!
# Testing is really important in computer science, so some nice functions are provided. We'll use them.

import unittest
from homework_01_01 import *

class TestHomework_01_01(unittest.TestCase):

    def test_double(self):
        self.assertEqual(double(10), 20)
        self.assertEqual(double(5), 10)
        self.assertEqual(double(0), 0)

    def test_triple(self):
        self.assertEqual(triple(10), 30)
        self.assertEqual(triple(5), 15)
        self.assertEqual(triple(0), 0)

    def test_bigger(self):
        self.assertEqual(bigger(1, 2), 2)
        self.assertEqual(bigger(-10, 10), 10)
        self.assertEqual(bigger(5, 3), 5)

    def test_has_an_eight(self):
        self.assertFalse(has_an_eight([1, 2, 3, 4]))
        self.assertTrue(has_an_eight([8, 8, 8, 8]))
        self.assertFalse(has_an_eight([]))
        
    def test_is_a_factor(self):
        self.assertTrue(is_a_factor(2, 6))
        self.assertTrue(is_a_factor(3, 6))
        self.assertFalse(is_a_factor(4, 6))
        self.assertFalse(is_a_factor(5, 6))
        self.assertTrue(is_a_factor(6, 6))

    def test_is_prime(self):
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(10))
        self.assertTrue(is_prime(11))

# This runs all the tests.
unittest.main()

