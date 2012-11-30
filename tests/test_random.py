# -*- coding: utf8 -*-

from nose.tools import assert_greater_equal, assert_less_equal


def test_random_cherries():
    from awesome.sauce import Cherry
    cherries = Cherry().random()
    assert_less_equal(cherries, 1000)
    assert_greater_equal(cherries, 1)
