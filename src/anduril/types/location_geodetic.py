# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .altitude import Altitude
from .altitude_above_wgs84ellipsoid import AltitudeAboveWgs84Ellipsoid


class LocationGeodetic(UniversalBaseModel):
    """
    Geodetic location measurement in reference to the WGS84 ellipsoid. This also optionally
     provides other altitude reference frames.
    """

    latitude_degrees: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="latitudeDegrees"),
        pydantic.Field(alias="latitudeDegrees", description="WGS84 latitude in decimal degrees."),
    ] = None
    """
    WGS84 latitude in decimal degrees.
    """

    longitude_degrees: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="longitudeDegrees"),
        pydantic.Field(alias="longitudeDegrees", description="WGS84 longitude in decimal degrees."),
    ] = None
    """
    WGS84 longitude in decimal degrees.
    """

    universal_altitude_hae: typing_extensions.Annotated[
        typing.Optional[AltitudeAboveWgs84Ellipsoid],
        FieldMetadata(alias="universalAltitudeHae"),
        pydantic.Field(
            alias="universalAltitudeHae",
            description="Altitude measurement in reference to the WGS84 defined ellipsoid. This is expected to\n always be set if an altitude measurement is available and should be derived from the\n most accurate altitude measurement available. If this is a 2D measurement, then this\n message should not be set. If you are unable to calculate this value, then this\n message should also not be set.",
        ),
    ] = None
    """
    Altitude measurement in reference to the WGS84 defined ellipsoid. This is expected to
     always be set if an altitude measurement is available and should be derived from the
     most accurate altitude measurement available. If this is a 2D measurement, then this
     message should not be set. If you are unable to calculate this value, then this
     message should also not be set.
    """

    additional_altitudes: typing_extensions.Annotated[
        typing.Optional[typing.List[Altitude]],
        FieldMetadata(alias="additionalAltitudes"),
        pydantic.Field(
            alias="additionalAltitudes",
            description="This allows for multiple additional altitudes to be conveyed.\n e.g. Barometric Pressure and Radar Altimeter readings\n for an aircraft",
        ),
    ] = None
    """
    This allows for multiple additional altitudes to be conveyed.
     e.g. Barometric Pressure and Radar Altimeter readings
     for an aircraft
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
