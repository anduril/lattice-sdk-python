# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .egress_stream import EgressStream


class GetEgressStreamResponse(UniversalBaseModel):
    egress_stream: typing_extensions.Annotated[
        typing.Optional[EgressStream],
        FieldMetadata(alias="egressStream"),
        pydantic.Field(
            alias="egressStream", description="The egress stream corresponding to the requested `egress_id`."
        ),
    ] = None
    """
    The egress stream corresponding to the requested `egress_id`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
