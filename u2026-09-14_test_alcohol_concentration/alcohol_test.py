from person import Person


class AlcoholTest:
    """Estimate blood alcohol concentration using the Widmark formula."""

    def __init__(
        self,
        test_name: str,
        limit: float = 0.5
    ) -> None:
        self.test_name: str = test_name
        self.limit: float = limit

    def alcohol_amount(
        self,
        volume: float,
        alcohol_content: float,
        density: float = 0.8
    ) -> float:
        """
        Calculate the amount of alcohol in grams.

        Args:
            volume: Drink volume in milliliters.
            alcohol_content: Alcohol percentage as a decimal.
            density: Alcohol density in grams per milliliter.

        Returns:
            Amount of alcohol in grams.
        """

        if volume <= 0:
            raise ValueError("Volume must be greater than zero.")

        if not 0 <= alcohol_content <= 1:
            raise ValueError(
                "Alcohol content must be between 0 and 1."
            )

        if density <= 0:
            raise ValueError("Density must be greater than zero.")

        return volume * alcohol_content * density

    def concentration(
        self,
        person: Person,
        volume: float,
        alcohol_content: float,
        density: float = 0.8
    ) -> float:
        """
        Calculate the estimated alcohol concentration in grams per kilogram.

        Formula:
            concentration = alcohol_amount / (mass * distribution_factor)
        """

        alcohol_amount = self.alcohol_amount(
            volume,
            alcohol_content,
            density
        )

        distribution_factor = person.distribution_factor()

        return alcohol_amount / (
            person.mass * distribution_factor
        )

    def passed(
        self,
        person: Person,
        volume: float,
        alcohol_content: float,
        density: float = 0.8
    ) -> bool:
        """Return True if the person is below or equal to the limit."""

        concentration = self.concentration(
            person,
            volume,
            alcohol_content,
            density
        )

        return concentration <= self.limit
