# -*- coding: utf-8 -*-

import unittest

from tapioca_stripe import Stripe


class TestTapiocaStripe(unittest.TestCase):

    def setUp(self):
        self.wrapper = Stripe()


if __name__ == '__main__':
    unittest.main()
