# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .media_item_type import MediaItemType


class MediaItem(UniversalBaseModel):
    item_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemIdentifier"),
        pydantic.Field(alias="itemIdentifier", description="A unique identifier for this mediaItem."),
    ] = None
    type: typing.Optional[MediaItemType] = pydantic.Field(default=None)
    """
    The type of media for this item.
    """

    relative_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="relativePath"),
        pydantic.Field(
            alias="relativePath",
            description="The path, relative to the environment base URL, where media related to an entity can be accessed",
        ),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
