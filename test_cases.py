from API import *
import pytest


class TestAPI:
    def test_nums(self, get_nums_data):
        response = nums(get_nums_data[0], get_nums_data[1])
        result = response.json()['num']

        assert result == get_nums_data[2]
