import unittest

from offers.offer import Offer


class TestOffer(unittest.TestCase):
    def test_not_implemented_error(self):
        with self.assertRaises(NotImplementedError):
            Offer().calculate_discount([])


if __name__ == "__main__":
    unittest.main()
