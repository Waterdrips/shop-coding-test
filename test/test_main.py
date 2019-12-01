import io
import unittest

from unittest.mock import patch

import main


class TestMain(unittest.TestCase):
    def test_no_items(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main([])
            self.assertEqual(
                """Subtotal: 0p
(no offers available)
Total: 0p""",
                fakeOutput.getvalue().strip(),
            )

    def test_no_offers(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main([])
            self.assertEqual(
                """Subtotal: 0p
(no offers available)
Total: 0p""",
                fakeOutput.getvalue().strip(),
            )

    def test_multiple_offers(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["Soup", "Apples", "Soup", "Bread"])
            self.assertEqual(
                """Subtotal: £3.10
Apples 10% off: -10p
Soup, Buy 2 and get 50% off a loaf of Bread: -40p
Total: £2.60""",
                fakeOutput.getvalue().strip(),
            )

    def test_one_offer(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["Apples"])
            self.assertEqual(
                """Subtotal: £1.00
Apples 10% off: -10p
Total: 90p""",
                fakeOutput.getvalue().strip(),
            )

    def test_rejected_item(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["NOTApples"])
            self.assertEqual(
                """We were unable to match these items to products: NOTApples
Subtotal: 0p
(no offers available)
Total: 0p""",
                fakeOutput.getvalue().strip(),
            )

    def test_multiple_rejected_items(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["NOTApples", "NOTBread"])
            self.assertEqual(
                """We were unable to match these items to products: NOTApples, NOTBread
Subtotal: 0p
(no offers available)
Total: 0p""",
                fakeOutput.getvalue().strip(),
            )

    def test_multiple_rejected_items_and_actual_items(self):
        with patch("sys.stdout", new=io.StringIO()) as fakeOutput:
            main.main(["NOTApples", "NOTBread", "Bread", "Apples", "Milk"])
            self.assertEqual(
                """We were unable to match these items to products: NOTApples, NOTBread
Subtotal: £3.10
Apples 10% off: -10p
Total: £3.00""",
                fakeOutput.getvalue().strip(),
            )


if __name__ == "__main__":
    unittest.main()
