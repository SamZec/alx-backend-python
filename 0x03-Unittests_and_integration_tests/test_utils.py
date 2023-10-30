#!/usr/bin/env python3
""" test_utils.py """


from parameterized import parameterized
import unittest
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch


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


class TestGetJson(unittest.TestCase):
    """implement the TestGetJson.test_get_json method
        to test get_json functio from utils
    """
    @parameterized.expand([
                          ("http://example.com", {"payload": True}),
                          ("http://holberton.io", {"payload": False})
                          ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """tests get_json function from utils"""
        with patch('utils.get_json') as get:
            get.return_value = test_payload
            res = get(test_url)
            get.assert_called_once_with(test_url)
            self.assertEqual(res, test_payload)


class TestMemoize(unittest.TestCase):
    """ memoization implentation """
    def test_memoize(self) -> None:
        """testing memoization"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as myFunc:
            inst = TestClass()
            inst.a_property()
            inst.a_property()
            myFunc.assert_called_once()
