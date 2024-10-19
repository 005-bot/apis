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
    
    def to_json(self)->str:
        return json.dumps(self.to_dict())
    
    @classmethod
    def from_json(cls, json):
        dict = json.loads(json)
        return cls(
            area=dict["area"],
            organization=dict["organization"],
            address=dict["address"],
            dates=dict["dates"],
        )
