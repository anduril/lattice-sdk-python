# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ExecutionConstraints(UniversalBaseModel):
    """
    `ExecutionConstraints` provides scheduling details that informs the agent when to execute the task.
    """

    start_after: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startAfter"),
        pydantic.Field(alias="startAfter", description="The timestamp after which the agent can execute the task"),
    ] = None
    """
    The timestamp after which the agent can execute the task
    """

    complete_before: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="completeBefore"),
        pydantic.Field(
            alias="completeBefore", description="The timestamp before which the agent can execute the task."
        ),
    ] = None
    """
    The timestamp before which the agent can execute the task.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
