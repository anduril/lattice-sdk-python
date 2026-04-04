# This file was auto-generated from our API Definition.

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.google_protobuf_any import GoogleProtobufAny


class StreamManualControlFramesResponse_Heartbeat(UniversalBaseModel):
    """
    The stream event response.
    """

    event: typing.Literal["heartbeat"] = "heartbeat"
    timestamp: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StreamManualControlFramesResponse_ManualControlFrame(UniversalBaseModel):
    """
    The stream event response.
    """

    event: typing.Literal["manual_control_frame"] = "manual_control_frame"
    task_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="taskId"), pydantic.Field(alias="taskId")
    ] = None
    epoch_micros: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="epochMicros"), pydantic.Field(alias="epochMicros")
    ] = None
    sequence: typing.Optional[str] = None
    creation_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="creationTime"), pydantic.Field(alias="creationTime")
    ] = None
    specification: typing.Optional[GoogleProtobufAny] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StreamManualControlFramesResponse = typing_extensions.Annotated[
    typing.Union[StreamManualControlFramesResponse_Heartbeat, StreamManualControlFramesResponse_ManualControlFrame],
    pydantic.Field(discriminator="event"),
]
