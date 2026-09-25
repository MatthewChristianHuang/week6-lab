# test_duckfine.py
import unittest
from duckfine import DuckFine


class TestDuckFine(unittest.TestCase):

    def setUp(self):
        self.fine = DuckFine(member_id="M123")

    def test_initial_total_owed_is_zero(self):
        self.assertEqual(self.fine.total_owed, 0.0)

    def test_no_fee_when_returned_on_time(self):
        fee = self.fine.charge(days_late=0)
        self.assertEqual(fee, 0.0)

    def test_no_fee_within_grace_period(self):
        fee = self.fine.charge(days_late=2)
        self.assertEqual(fee, 0.0)

    def test_standard_fee_after_grace_period(self):
        # 3 days late -> 1 chargeable day * 0.50 = 0.50
        fee = self.fine.charge(days_late=3)
        self.assertEqual(fee, 0.50)

    def test_deluxe_fee_doubles_standard_rate(self):
        # 3 days late -> 1 chargeable day * 0.50 * 2 = 1.00
        fee = self.fine.charge(days_late=3, deluxe=True)
        self.assertEqual(fee, 1.00)

    def test_fee_caps_at_maximum_limit(self):
        # 20 days late -> 18 chargeable days * 0.50 = 9.00 -> capped at 5.00
        fee = self.fine.charge(days_late=20)
        self.assertEqual(fee, 5.00)

    def test_deluxe_fee_caps_at_maximum_limit(self):
        # 8 days late -> 6 chargeable days * 0.50 * 2 = 6.00 -> capped at 5.00
        fee = self.fine.charge(days_late=8, deluxe=True)
        self.assertEqual(fee, 5.00)

    def test_total_owed_accumulates_multiple_charges(self):
        self.fine.charge(days_late=3)  # 0.50
        self.fine.charge(days_late=4)  # 1.00
        self.assertEqual(self.fine.total_owed, 1.50)

    def test_negative_days_late_raises_value_error(self):
        with self.assertRaises(ValueError):
            self.fine.charge(days_late=-1)


if __name__ == "__main__":
    unittest.main()