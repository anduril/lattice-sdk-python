# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .numeric_type import NumericType


class RangeType(UniversalBaseModel):
    """
    The RangeType represents a numeric range.
     Whether endpoints are included are based on the comparator used.
     Both endpoints must be of the same numeric type.
    """

    start: typing.Optional[NumericType] = None
    end: typing.Optional[NumericType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
