#!/usr/bin/env python3
""" test_utils.py - module for TestAccessNestedMap class """


from parameterized import parameterized
import unittest
from utils import access_nested_map
from nose.tools import assert_equal


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase for testing utils.access_nested_map"""
    @parameterized.expand([
                          ({"a": 1}, "a", 1),
                          ({"a": {"b": 2}}, "a", {"b": 2}),
                          ({"a": {"b": 2}}, ("a", "b"), 2)
                          ])
    def test_access_nested_map(self, obj, path, res):
        """tests access_nested_map function from utils"""
        assert_equal(access_nested_map(obj, path), res)
