# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class SrtEgress(UniversalBaseModel):
    """
    SRT egress connection details.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL on which Lattice listens. The downstream consumer pulls from this URL.
    """

    session_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sessionId"),
        pydantic.Field(
            alias="sessionId", description="Unique session identifier the consumer must supply on the SRT connection."
        ),
    ] = None
    """
    Unique session identifier the consumer must supply on the SRT connection.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
