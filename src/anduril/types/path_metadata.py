# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .content_identifier import ContentIdentifier


class PathMetadata(UniversalBaseModel):
    content_identifier: ContentIdentifier
    size_bytes: int
    last_updated_at: dt.datetime = pydantic.Field()
    """
    When this object arrived on the node that holds it, according to that node's clock. Because an object is never modified in place, this is effectively the time the object was created on that node.
    
    The value is local to the node holding the object and may differ when the same object is held on multiple nodes. It is not propagated from the node where the object originated.
    """

    expiry_time: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
