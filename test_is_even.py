#!/usr/bin/env python3

from is_even import even_or_odds
import unittest


class Testevens(unittest.TestCase):
	def test_even(self):
		testcase = 2
		expected = True
		self.assertEqual(even_or_odds(testcase), expected)
		
	def test_odd(self):
		testcase = 3
		expected = False
		self.assertEqual(even_or_odds(testcase),expected)
unittest.main()