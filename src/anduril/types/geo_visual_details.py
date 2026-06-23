# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .color import Color


class GeoVisualDetails(UniversalBaseModel):
    """
    Details specific to displaying a geo-entity
    """

    fill_color: typing_extensions.Annotated[
        typing.Optional[Color],
        FieldMetadata(alias="fillColor"),
        pydantic.Field(alias="fillColor", description="Describes the fill color of a geo-entity."),
    ] = None
    line_color: typing_extensions.Annotated[
        typing.Optional[Color],
        FieldMetadata(alias="lineColor"),
        pydantic.Field(alias="lineColor", description="Describes the line color of a geo-entity."),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
