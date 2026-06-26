# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class HeadingType(UniversalBaseModel):
    """
    The HeadingType represents the heading in degrees for an entity's
     attitudeEnu quaternion to be compared against. Defaults between a range of 0 to 360
    """

    value: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
