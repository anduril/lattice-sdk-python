# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DeletedObjectEntry(UniversalBaseModel):
    path: str = pydantic.Field()
    """
    Object path that was deleted on this node.
    A valid path must not contain the following:
    - Spaces or Tabs
    - Special characters other than underscore (_), dash (-), period (.) and slash (/)
    - Non-ASCII characters such as accents or symbols
    Paths must not start with a leading space.
    """

    checksum: str = pydantic.Field()
    """
    The SHA-256 checksum of this object.
    """

    deleted_at: dt.datetime = pydantic.Field()
    """
    Wall-clock time at which the deletion was initiated on this node.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
