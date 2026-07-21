# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .altitude_provenance_source_type import AltitudeProvenanceSourceType


class AltitudeProvenance(UniversalBaseModel):
    source_type: typing_extensions.Annotated[
        typing.Optional[AltitudeProvenanceSourceType],
        FieldMetadata(alias="sourceType"),
        pydantic.Field(alias="sourceType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
