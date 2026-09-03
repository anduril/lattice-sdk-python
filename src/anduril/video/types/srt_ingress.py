# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class SrtIngress(UniversalBaseModel):
    """
    SRT ingress connection details. Returned to the producer so it knows where to
     push the stream.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL the producer should push the SRT stream to.
    """

    session_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sessionId"),
        pydantic.Field(
            alias="sessionId",
            description="Unique session identifier the producer must include on the SRT connection. See\n SrtSettings for context.",
        ),
    ] = None
    """
    Unique session identifier the producer must include on the SRT connection. See
     SrtSettings for context.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
