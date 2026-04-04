# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .google_protobuf_any import GoogleProtobufAny


class ManualControlFrame(UniversalBaseModel):
    """
    A single frame of manual control input forwarded by Lattice to an agent.

     When an operator sends manual control input, for example, joystick movements using
     `SendManualControlFrames`, Lattice packages each input into a `ManualControlFrame`
     and forwards it to the executing agent via the `ListenForManualControlFrames`
     streaming RPC.

     Each frame carries sequencing metadata to support concurrent control sessions,
     detect stale frames, and ensure proper ordering.
    """

    task_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="taskId"),
        pydantic.Field(alias="taskId", description="The ID of the manual control task this frame belongs to."),
    ] = None
    epoch_micros: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="epochMicros"),
        pydantic.Field(
            alias="epochMicros",
            description="Unix timestamp in microseconds identifying the control session.\n Increments each time a client opens a new stream for this task.\n Agents should ignore frames with a lower epoch to handle stale streams\n or operator handoffs.",
        ),
    ] = None
    sequence: typing.Optional[str] = pydantic.Field(default=None)
    """
    The sequence number for a stream, incremented for each frame.
     Agents can use this to detect out-of-order delivery within the same epoch.
    """

    creation_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="creationTime"),
        pydantic.Field(
            alias="creationTime",
            description="The time at which this frame was created.\n Agents can use this to detect stale frame data.",
        ),
    ] = None
    specification: typing.Optional[GoogleProtobufAny] = pydantic.Field(default=None)
    """
    The control instructions for this frame, passed through from the client.
     The format of each task is specific to the task, and not visible to Lattice.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
