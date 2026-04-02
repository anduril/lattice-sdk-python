# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .task_stream_request_status_filter_filter_type import TaskStreamRequestStatusFilterFilterType
from .task_stream_request_status_filter_statuses_item import TaskStreamRequestStatusFilterStatusesItem


class TaskStreamRequestStatusFilter(UniversalBaseModel):
    """
    A filter for task statuses (inclusive or exclusive).
    """

    statuses: typing.Optional[typing.List[TaskStreamRequestStatusFilterStatusesItem]] = pydantic.Field(default=None)
    """
    The statuses to filter by.
    """

    filter_type: typing_extensions.Annotated[
        typing.Optional[TaskStreamRequestStatusFilterFilterType],
        FieldMetadata(alias="filterType"),
        pydantic.Field(alias="filterType", description="The type of filter to apply."),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
