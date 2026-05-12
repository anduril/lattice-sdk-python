# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .deleted_object_entry import DeletedObjectEntry


class ListDeletedObjectsResponse(UniversalBaseModel):
    deleted_objects: typing.List[DeletedObjectEntry]
    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Present when more pages are available. Pass back as `pageToken`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
