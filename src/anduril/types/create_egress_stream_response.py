# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .rtsp_egress import RtspEgress
from .srt_egress import SrtEgress


class CreateEgressStreamResponse(UniversalBaseModel):
    egress_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="egressId"),
        pydantic.Field(
            alias="egressId",
            description="Service-generated identifier for the new egress stream. Use it for subsequent\n `GetEgressStream` and `DeleteEgressStream` calls.",
        ),
    ] = None
    """
    Service-generated identifier for the new egress stream. Use it for subsequent
     `GetEgressStream` and `DeleteEgressStream` calls.
    """

    rtsp: typing.Optional[RtspEgress] = None
    srt: typing.Optional[SrtEgress] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
