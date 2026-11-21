# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ingress_stream import IngressStream


class QueryIngressStreamsResponse(UniversalBaseModel):
    """
    Response for QueryIngressStreams.
    """

    ingress_streams: typing_extensions.Annotated[
        typing.Optional[typing.List[IngressStream]],
        FieldMetadata(alias="ingressStreams"),
        pydantic.Field(
            alias="ingressStreams",
            description="Up to `pageSize` streams, newest first. Streams created through this API come\n first, then streams discovered on the mesh, and each group starts with its\n newest stream.",
        ),
    ] = None
    """
    Up to `pageSize` streams, newest first. Streams created through this API come
     first, then streams discovered on the mesh, and each group starts with its
     newest stream.
    """

    next_page_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="nextPageToken"),
        pydantic.Field(
            alias="nextPageToken",
            description="Pass this back as `pageToken` to get the next page. Empty when there are no\n more pages.",
        ),
    ] = None
    """
    Pass this back as `pageToken` to get the next page. Empty when there are no
     more pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
