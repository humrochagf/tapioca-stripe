# -*- coding: utf-8 -*-

import unittest

from tapioca_stripe import Stripe


class TestTapiocaStripe(unittest.TestCase):

    def setUp(self):
        self.wrapper = Stripe()

    def test_get_api_root(self):
        self.assertTrue(
            self.wrapper.customers_list().data.startswith('https://api.')
        )
        self.assertTrue(
            self.wrapper.files_create().data.startswith('https://files.')
        )


if __name__ == '__main__':
    unittest.main()
