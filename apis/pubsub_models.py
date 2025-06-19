import datetime

from pydantic import BaseModel, computed_field
from typing_extensions import deprecated

from .i18n import format_date_ru
from .models import OrganizationInfo, OutageDetails


class Outage(BaseModel):
    """Model representing an outage event.

    Attributes:
        area (str): The area affected by the outage.
        organization_info (OrganizationInfo): Information about the organization responsible for the outage.
        details (OutageDetails): Detailed information about the outage, including affected streets and reasons.
        period (list[datetime.datetime]): List of datetime objects representing the outage period.
    """

    area: str
    organization_info: OrganizationInfo
    details: OutageDetails
    period: list[datetime.datetime]

    @computed_field
    @property
    @deprecated("Use `organization_info` instead")
    def organization(self) -> str:
        """Deprecated property. Use `organization_info` instead.

        Returns:
            str: String representation of the organization information.
        """
        return str(self.organization_info)

    @computed_field
    @property
    @deprecated("Use `details` instead")
    def address(self) -> str:
        """Deprecated property. Use `details` instead.

        Returns:
            str: String representation of the outage details.
        """
        return str(self.details)

    @computed_field
    @property
    @deprecated("Use `period` instead")
    def dates(self) -> str:
        """Deprecated method. Use `period` instead.

        Returns:
            str: String representation of the outage period dates.
        """
        return " ".join([format_date_ru(date) for date in self.period])
