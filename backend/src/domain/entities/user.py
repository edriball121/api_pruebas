from dataclasses import dataclass, field
from typing import List, Optional
from uuid import UUID, uuid4


@dataclass
class User:
    id: Optional[int] = None
    name: str = ""
    username: str = ""
    email: str = ""
    phone: str = ""
    website: str = ""

    # Address is embedded
    address_street: str = ""
    address_suite: str = ""
    address_city: str = ""
    address_zipcode: str = ""
    address_geo_lat: str = ""
    address_geo_lng: str = ""

    # Company is embedded
    company_name: str = ""
    company_catch_phrase: str = ""
    company_bs: str = ""