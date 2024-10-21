from dataclasses import dataclass
import json


@dataclass(frozen=True, slots=True)
class Outage:
    area: str
    organization: str
    address: str
    dates: str

    def to_dict(self):
        return {
            "area": self.area,
            "organization": self.organization,
            "address": self.address,
            "dates": self.dates,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, j: str | bytes):
        if isinstance(j, bytes):
            j = j.decode("utf-8")
        d = json.loads(j)
        return cls(
            area=d["area"],
            organization=d["organization"],
            address=d["address"],
            dates=d["dates"],
        )
