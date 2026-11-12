# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StringFilter(UniversalBaseModel):
    """
    Matches text, treating upper and lower case as different. Set exactly one of
     `exact`, `prefix`, or `contains`, and give it a non-empty value. The server
     rejects the request with INVALID_ARGUMENT (HTTP 400) if you set none, more than
     one, or an empty value.
    """

    exact: typing.Optional[str] = pydantic.Field(default=None)
    """
    Matches text that is exactly this value. Can't be combined with `prefix` or
     `contains`.
    """

    prefix: typing.Optional[str] = pydantic.Field(default=None)
    """
    Matches text that starts with this value. Can't be combined with `exact` or
     `contains`.
    """

    contains: typing.Optional[str] = pydantic.Field(default=None)
    """
    Matches text that includes this value anywhere. Can't be combined with
     `exact` or `prefix`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
