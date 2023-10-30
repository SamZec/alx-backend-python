#!/usr/bin/env python3
""" test_utils.py - module for TestAccessNestedMap class """


from parameterized import parameterized
import unittest
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """inherits from unittest.TestCase for testing utils.access_nested_map"""
    @parameterized.expand([
                          ({"a": 1}, "a", 1),
                          ({"a": {"b": 2}}, "a", {"b": 2}),
                          ({"a": {"b": 2}}, ("a", "b"), 2)
                          ])
    def test_access_nested_map(self, obj: Mapping,
                               path: Sequence, res: Any) -> Any:
        """tests access_nested_map function from utils"""
        self.assertEqual(access_nested_map(obj, path), res)

    @parameterized.expand([
                          ({}, "a"),
                          ({"a": 1}, ("a", "b"))
                          ])
    def test_access_nested_map_exception(self, obj: Mapping,
                                         path: Sequence) -> None:
        """Use the assertRaises context manager to test a KeyError"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(obj, path)
        self.assertTrue(e)
