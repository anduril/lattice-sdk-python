# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreatorFilter(UniversalBaseModel):
    """
    Matches streams by who created them. Set exactly one option. The server rejects
     the request with INVALID_ARGUMENT (HTTP 400) if you set none.
    """

    owned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Set to true to return only streams you created, or false to return only
     streams you didn't create. Requires valid credentials. When you set it,
     each stream's `egressIds` lists only your own egress sessions.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
