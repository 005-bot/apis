import enum
from dataclasses import dataclass


class ResourceType(str, enum.Enum):
    """Enumeration of resource types for utility services.

    This enum defines various types of utility services such as water supply,
    electricity, and gas. Each member of the enum is associated with a string
    representation in Russian.
    """

    COLD_WATER = "Холодное водоснабжение"
    HOT_WATER = "Горячее водоснабжение"
    ELECTRICITY = "Электроснабжение"
    GAS = "Газоснабжение"


@dataclass(frozen=True)
class OrganizationInfo:
    """Data class containing organization information parsed from input strings"""

    resource_type: ResourceType | None
    resource: str
    organization: str
    phones: list[str]

    def __str__(self) -> str:
        parts = [self.resource, self.organization]
        if self.phones:
            parts.append(", ".join(self.phones))
        return "\n".join(parts)


@dataclass(frozen=True)
class Street:
    """
    Represents a street with a name.
    """

    name: str
    buildings: list[str] | None

    def __str__(self) -> str:
        s = self.name
        if self.buildings:
            s += " " + ", ".join(self.buildings)

        return s


@dataclass(frozen=True)
class Reason:
    """
    Represents a reason for an event.
    """

    type: str
    description: str

    def __str__(self) -> str:
        return f"{self.type} - {self.description}"


@dataclass(frozen=True)
class WaterDelivery:
    """Represents a water delivery request."""

    street: str
    buildings: str
    time_start: str
    time_end: str

    def __str__(self) -> str:
        return f"{self.street} {self.buildings} с {self.time_start} до {self.time_end}"


@dataclass(frozen=True)
class OutageDetails:
    """Details about an outage, including the affected streets."""

    streets: list[Street]
    reason: Reason | None = None
    water_deliveries: list[WaterDelivery] | None = None
    comments: str | None = None

    def __str__(self) -> str:
        base = "\n".join([str(s) for s in self.streets])
        if self.reason:
            base += f"\n\n{self.reason}"
        if self.water_deliveries:
            base += "\n\nПодвоз воды: "
            base += "; ".join([str(wd) for wd in self.water_deliveries])
        elif self.comments:
            base += f"\n\n{self.comments}"
        return base
