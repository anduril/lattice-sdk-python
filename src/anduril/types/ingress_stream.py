# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ingress_stream_status import IngressStreamStatus
from .mpeg_ts_ingress import MpegTsIngress
from .rtsp_ingress import RtspIngress
from .srt_ingress import SrtIngress


class IngressStream(UniversalBaseModel):
    """
    An ingress stream represents a single source feeding frames into Lattice.
     Ingress streams are replicated across Lattice and visible anywhere in the deployment.
    """

    ingress_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ingressId"),
        pydantic.Field(alias="ingressId", description="Unique identifier for the ingress stream."),
    ] = None
    """
    Unique identifier for the ingress stream.
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-readable title supplied at creation time.
    """

    status: typing.Optional[IngressStreamStatus] = pydantic.Field(default=None)
    """
    Current lifecycle status of the stream. See StreamStatus for the full state machine.
    """

    mpeg_ts: typing_extensions.Annotated[
        typing.Optional[MpegTsIngress], FieldMetadata(alias="mpegTs"), pydantic.Field(alias="mpegTs")
    ] = None
    rtsp: typing.Optional[RtspIngress] = None
    srt: typing.Optional[SrtIngress] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Wall-clock time the stream was created."),
    ] = None
    """
    Wall-clock time the stream was created.
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(
            alias="updatedAt",
            description="Wall-clock time the stream's status (STREAM_STATUS) was changed. The status can change based on the activity or\n the deletion of the stream.",
        ),
    ] = None
    """
    Wall-clock time the stream's status (STREAM_STATUS) was changed. The status can change based on the activity or
     the deletion of the stream.
    """

    egress_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="egressIds"),
        pydantic.Field(
            alias="egressIds", description="Identifiers of the egress streams currently consuming this ingress stream."
        ),
    ] = None
    """
    Identifiers of the egress streams currently consuming this ingress stream.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
