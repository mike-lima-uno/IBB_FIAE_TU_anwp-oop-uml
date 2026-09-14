import unittest

from person import Person


class TestPerson(unittest.TestCase):
    """Test the Person class."""

    def test_create_male_person(self) -> None:
        hansel = Person(
            name="Hansel",
            gender="male",
            mass=95
        )

        self.assertEqual(hansel.name, "Hansel")
        self.assertEqual(hansel.gender, "male")
        self.assertEqual(hansel.mass, 95)
        self.assertEqual(hansel.distribution_factor(), 0.7)

    def test_create_female_person(self) -> None:
        gretel = Person(
            name="Gretel",
            gender="female",
            mass=65
        )

        self.assertEqual(gretel.name, "Gretel")
        self.assertEqual(gretel.gender, "female")
        self.assertEqual(gretel.mass, 65)
        self.assertEqual(gretel.distribution_factor(), 0.6)

    def test_invalid_gender(self) -> None:
        with self.assertRaises(ValueError):
            Person(
                name="Person",
                gender="unknown",
                mass=70
            )

    def test_invalid_mass(self) -> None:
        with self.assertRaises(ValueError):
            Person(
                name="Person",
                gender="male",
                mass=0
            )


if __name__ == "__main__":
    unittest.main()
