# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RtspSettings(UniversalBaseModel):
    """
    Settings for RTSP.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The upstream RTSP URL the service should pull frames from. Must use
     the `rtsp://` scheme.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
