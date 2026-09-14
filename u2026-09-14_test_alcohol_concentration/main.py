from alcohol_test import AlcoholTest
from person import Person


def main() -> None:
    """Run the alcohol concentration test."""

    hansel = Person(
        name="Hansel",
        gender="male",
        mass=95
    )

    gretel = Person(
        name="Gretel",
        gender="female",
        mass=65
    )

    alcohol_test = AlcoholTest(
        test_name="Alcohol concentration test",
        limit=0.5
    )

    drink_volume = 500
    alcohol_content = 0.05
    alcohol_density = 0.8

    people = [hansel, gretel]

    print(f"Test: {alcohol_test.test_name}")
    print(f"Allowed limit: {alcohol_test.limit:.2f} g/kg")
    print(f"Drink volume: {drink_volume} ml")
    print(f"Alcohol content: {alcohol_content * 100:.2f}%")
    print()

    for person in people:
        concentration = alcohol_test.concentration(
            person=person,
            volume=drink_volume,
            alcohol_content=alcohol_content,
            density=alcohol_density
        )

        passed = alcohol_test.passed(
            person=person,
            volume=drink_volume,
            alcohol_content=alcohol_content,
            density=alcohol_density
        )

        result = "PASS" if passed else "FAIL"

        print(f"Person: {person}")
        print(f"Concentration: {concentration:.2f} g/kg")
        print(f"Result: {result}")
        print()


if __name__ == "__main__":
    main()
