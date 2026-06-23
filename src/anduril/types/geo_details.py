# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .acm_details import AcmDetails
from .control_area_details import ControlAreaDetails
from .geo_details_type import GeoDetailsType
from .geo_visual_details import GeoVisualDetails


class GeoDetails(UniversalBaseModel):
    """
    A component that describes a geo-entity.
    """

    type: typing.Optional[GeoDetailsType] = None
    control_area: typing_extensions.Annotated[
        typing.Optional[ControlAreaDetails], FieldMetadata(alias="controlArea"), pydantic.Field(alias="controlArea")
    ] = None
    acm: typing.Optional[AcmDetails] = None
    visual_details: typing_extensions.Annotated[
        typing.Optional[GeoVisualDetails], FieldMetadata(alias="visualDetails"), pydantic.Field(alias="visualDetails")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
