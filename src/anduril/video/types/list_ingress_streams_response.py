# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ingress_stream import IngressStream


class ListIngressStreamsResponse(UniversalBaseModel):
    ingress_streams: typing_extensions.Annotated[
        typing.Optional[typing.List[IngressStream]],
        FieldMetadata(alias="ingressStreams"),
        pydantic.Field(
            alias="ingressStreams",
            description="The ingress streams on this page. Up to `page_size` entries\n (defaults to 50, capped at 100). Ordered by ingress stream create time.",
        ),
    ] = None
    """
    The ingress streams on this page. Up to `page_size` entries
     (defaults to 50, capped at 100). Ordered by ingress stream create time.
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(
            alias="nextPageToken",
            description="Pass this back as `page_token` to retrieve the next page.\n Empty when there are no more pages.",
        ),
    ] = None
    """
    Pass this back as `page_token` to retrieve the next page.
     Empty when there are no more pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
