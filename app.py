"""Small application entry point for Coffee Corp BrewLedger."""

from dataclasses import dataclass


@dataclass
class CoffeeBean:
    """A coffee bean offering tracked by the inventory."""

    name: str
    origin: str
    kilograms_in_stock: float


class Inventory:
    """A small in-memory collection of coffee bean offerings."""

    def __init__(self, beans: list[CoffeeBean]) -> None:
        self.beans = beans

    def low_stock(self, threshold: float = 10.0) -> list[CoffeeBean]:
        """Return offerings with less than the requested stock threshold."""

        return [bean for bean in self.beans if bean.kilograms_in_stock < threshold]


def build_inventory() -> Inventory:
    """Create the current sample inventory used by the application."""

    return Inventory(
        [
            CoffeeBean("House Blend", "Colombia", 24.5),
            CoffeeBean("Night Shift Espresso", "Brazil", 7.0),
            CoffeeBean("Decaf Diplomat", "Mexico", 15.0),
        ]
    )


def main() -> None:
    """Print a short stock report for the coffee operations team."""

    inventory = build_inventory()
    for bean in inventory.low_stock():
        print(f"Restock {bean.name}: only {bean.kilograms_in_stock:.1f} kg remain")


if __name__ == "__main__":
    main()