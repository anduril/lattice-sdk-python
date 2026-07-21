# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LocationGeocentricEcef(UniversalBaseModel):
    """
    Location measurement in reference to the center of the earth using the ECEF
     coordinate system. This is in the WGS84 coordinate frame.
    """

    x_meters: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="xMeters"),
        pydantic.Field(
            alias="xMeters",
            description="The plane of the equator, passing through extending from 90°W longitude (negative)\n to 90°E longitude (positive).",
        ),
    ] = None
    """
    The plane of the equator, passing through extending from 90°W longitude (negative)
     to 90°E longitude (positive).
    """

    y_meters: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="yMeters"),
        pydantic.Field(
            alias="yMeters",
            description="The plane of the equator, passing through the origin and extending from 180° longitude\n (negative) to the prime meridian.",
        ),
    ] = None
    """
    The plane of the equator, passing through the origin and extending from 180° longitude
     (negative) to the prime meridian.
    """

    z_meters: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="zMeters"),
        pydantic.Field(
            alias="zMeters",
            description="The line between the North and South Poles, with positive values increasing northward.",
        ),
    ] = None
    """
    The line between the North and South Poles, with positive values increasing northward.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
