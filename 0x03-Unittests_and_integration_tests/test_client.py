#!/usr/bin/env python3
"""test_client.py - Parameterize and patch as decorators"""


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """tesing object for GithubOrgClient"""
    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, data, mock) -> None:
        """ test that GithubOrgClient.org returns the correct value."""
        url = f'https://api.github.com/orgs/{data}'
        inst = GithubOrgClient(data)
        inst.org()
        mock.assert_called_once_with(url)
