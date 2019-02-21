import unittest

import utils


class TestPreparingData(unittest.TestCase):
    def test_prepare_time_for_display(self):
        self.assertEqual(utils.prepare_date_for_display(1, 1, 2000), '01.01.2000')

