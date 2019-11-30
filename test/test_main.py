import io
import unittest

from unittest.mock import patch

import main


class TestMain(unittest.TestCase):
    def test_no_items(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main([])
            self.assertEqual(
                fakeOutput.getvalue().strip(),
                """Subtotal: 0p
(no offers available)
Total: 0p""",
            )

    def test_no_offers(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main([])
            self.assertEqual(
                fakeOutput.getvalue().strip(),
                """Subtotal: 0p
(no offers available)
Total: 0p""",
            )

    def test_multiple_offers(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["Soup", "Apples", "Soup", "Bread"])
            self.assertEqual(
                fakeOutput.getvalue().strip(),
                """Subtotal: £3.10
Apples 10% off: -10p
Soup, Buy 2 and get 50% off a loaf of Bread: -40p
Total: £2.60""",
            )

    def test_one_offer(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["Apples"])
            self.assertEqual(
                fakeOutput.getvalue().strip(),
                """Subtotal: £1.00
Apples 10% off: -10p
Total: 90p""",
            )


if __name__ == "__main__":
    unittest.main()
