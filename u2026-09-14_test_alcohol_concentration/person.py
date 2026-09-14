class Person:
    """Represent a person taking an alcohol concentration test."""

    def __init__(
        self,
        name: str,
        gender: str,
        mass: float
    ) -> None:
        if not name:
            raise ValueError("Name cannot be empty.")

        if gender not in ("male", "female"):
            raise ValueError(
                "Gender must be either 'male' or 'female'."
            )

        if mass <= 0:
            raise ValueError("Mass must be greater than zero.")

        self.name: str = name
        self.gender: str = gender
        self.mass: float = mass

    def distribution_factor(self) -> float:
        """Return the Widmark distribution factor."""

        if self.gender == "male":
            return 0.7

        return 0.6

    def __str__(self) -> str:
        """Return a readable representation of the person."""

        return f"{self.name} ({self.gender}, {self.mass} kg)"
