import unittest

from person import Person
from alcohol_test import AlcoholTest


class TestAlcoholTest(unittest.TestCase):
    """Test the AlcoholTest class."""

    def setUp(self) -> None:
        self.alcohol_test = AlcoholTest(
            test_name="Alcohol test",
            limit=0.5
        )

        self.hansel = Person(
            name="Hansel",
            gender="male",
            mass=95
        )

        self.gretel = Person(
            name="Gretel",
            gender="female",
            mass=65
        )

    def test_alcohol_amount(self) -> None:
        amount = self.alcohol_test.alcohol_amount(
            volume=500,
            alcohol_content=0.05,
            density=0.8
        )

        self.assertAlmostEqual(amount, 20.0)

    def test_hansel_passes(self) -> None:
        concentration = self.alcohol_test.concentration(
            person=self.hansel,
            volume=500,
            alcohol_content=0.05,
            density=0.8
        )

        expected = 20 / (95 * 0.7)

        self.assertAlmostEqual(concentration, expected)

        self.assertTrue(
            self.alcohol_test.passed(
                person=self.hansel,
                volume=500,
                alcohol_content=0.05,
                density=0.8
            )
        )

    def test_gretel_does_not_pass(self) -> None:
        concentration = self.alcohol_test.concentration(
            person=self.gretel,
            volume=500,
            alcohol_content=0.05,
            density=0.8
        )

        expected = 20 / (65 * 0.6)

        self.assertAlmostEqual(concentration, expected)

        self.assertFalse(
            self.alcohol_test.passed(
                person=self.gretel,
                volume=500,
                alcohol_content=0.05,
                density=0.8
            )
        )


if __name__ == "__main__":
    unittest.main()
