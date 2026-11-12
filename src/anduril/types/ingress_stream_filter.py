# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .creator_filter import CreatorFilter
from .ingress_stream_filter_statuses_item import IngressStreamFilterStatusesItem
from .string_filter import StringFilter


class IngressStreamFilter(UniversalBaseModel):
    """
    Chooses which streams QueryIngressStreams returns.

     A stream must match every field you set. For a field that takes a list, the
     stream only needs to match one value in it. Fields you leave out don't limit
     the results. The server rejects unrecognized values, so a typo never quietly
     returns more streams than you asked for. The filter only works within the
     streams you already have permission to see.
    """

    creator: typing.Optional[CreatorFilter] = pydantic.Field(default=None)
    """
    Returns only streams that match by who created them. Leave it out to include
     every creator.
    """

    ingress_id: typing_extensions.Annotated[
        typing.Optional[StringFilter],
        FieldMetadata(alias="ingressId"),
        pydantic.Field(
            alias="ingressId",
            description="Returns only streams whose ingress ID matches. Compares against the part of\n `ingress_id` before any `#`. For a stream you created, that's the ID you chose.",
        ),
    ] = None
    """
    Returns only streams whose ingress ID matches. Compares against the part of
     `ingress_id` before any `#`. For a stream you created, that's the ID you chose.
    """

    title: typing.Optional[StringFilter] = pydantic.Field(default=None)
    """
    Returns only streams whose title matches.
    """

    statuses: typing.Optional[typing.List[IngressStreamFilterStatusesItem]] = pydantic.Field(default=None)
    """
    Returns only streams in one of these statuses.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
