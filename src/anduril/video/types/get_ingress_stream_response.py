# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ingress_stream import IngressStream


class GetIngressStreamResponse(UniversalBaseModel):
    ingress_stream: typing_extensions.Annotated[
        typing.Optional[IngressStream],
        FieldMetadata(alias="ingressStream"),
        pydantic.Field(
            alias="ingressStream", description="The ingress stream corresponding to the requested `ingress_id`."
        ),
    ] = None
    """
    The ingress stream corresponding to the requested `ingress_id`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
