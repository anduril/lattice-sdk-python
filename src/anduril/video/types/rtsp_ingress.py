# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RtspIngress(UniversalBaseModel):
    """
    RTSP ingress connection details.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The upstream RTSP URL. Lattice will pull from the supplied URL.
     The URL must be prefixed with `rtsp://`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
