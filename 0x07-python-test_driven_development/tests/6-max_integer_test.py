#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for Unittest f Max_integer"""
    def setUp(self):
        self.em_list = []
        self.ele_list = [2]
        self.elements_l = [2, 3, 5, 6, 46, 47]
        self.neg_ele_l = [-56, -9, -23, -1, -3]
        self.max_beg = [-1, -3, -6, -2]
        self.max_end = [0, 23, 2, 192]
        self.dup_li = [23, 4, 45, 23, 45, 4]
        self.one_neg = [2, 5, -456, 5, 67]
    
    def test_em_lis(self):
        self.assertIsNone(max_integer(self.em_list))

    def test_one_el(self):
        self.assertEqual(max_integer(self.ele_list), 2)

    def test_neg_list(self):
        self.assertEqual(max_integer(self.neg_ele_l), -1)

    def test_pos_list(self):
        self.assertEqual(max_integer(self.elements_l), 47)

    def test_max_beg(self):
        self.assertEqual(max_integer(self.max_beg), -1)

    def test_max_end(self):
        self.assertEqual(max_integer(self.max_end), 192)

    def test_dup_list(self):
        self.assertEqual(max_integer(self.dup_li), 45)

    def test_one_neg(self):
        self.assertEqual(max_integer(self.one_neg), 67)

    def test_non_integers(self):
        with self.assertRaises(TypeError):
            max_integer([2, 'abc', True, [1, 2, 3]])
