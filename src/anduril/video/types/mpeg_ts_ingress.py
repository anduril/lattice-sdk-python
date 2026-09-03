# This file was auto-generated from our API Definition.

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MpegTsIngress(UniversalBaseModel):
    """
    MPEG-TS ingress connection details.

     MPEG-TS ingress is supported only at the edge, in closed networks; in a cloud
     environment reached over the public internet it may be disabled per deployment. These
     details are populated only when a stream was successfully created with mpeg_ts. An
     MPEG-TS stream created at the edge can still be listed and inspected on the
     IngressStream read model even when cloud ingress is disabled.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL that the producer should push the MPEG-TS stream to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
