# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .mpeg_ts_ingress import MpegTsIngress
from .srt_ingress import SrtIngress


class CreateIngressStreamResponse(UniversalBaseModel):
    ingress_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ingressId"),
        pydantic.Field(
            alias="ingressId",
            description="Identifier of the newly created ingress stream. Echoes the caller-supplied\n `ingress_id` if one was provided, otherwise a service-generated GUID.",
        ),
    ] = None
    """
    Identifier of the newly created ingress stream. Echoes the caller-supplied
     `ingress_id` if one was provided, otherwise a service-generated GUID.
    """

    mpeg_ts: typing_extensions.Annotated[
        typing.Optional[MpegTsIngress],
        FieldMetadata(alias="mpegTs"),
        pydantic.Field(
            alias="mpegTs",
            description="Connection details for an MPEG-TS push. Only returned when MPEG-TS ingress is\n enabled for the deployment and the request selected mpeg_ts.",
        ),
    ] = None
    """
    Connection details for an MPEG-TS push. Only returned when MPEG-TS ingress is
     enabled for the deployment and the request selected mpeg_ts.
    """

    srt: typing.Optional[SrtIngress] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
