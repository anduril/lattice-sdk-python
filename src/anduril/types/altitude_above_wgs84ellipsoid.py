# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .altitude_provenance import AltitudeProvenance


class AltitudeAboveWgs84Ellipsoid(UniversalBaseModel):
    """
    Altitude above the WGS84 defined ellipsoid. Often measured with a GNSS sensor.
    """

    provenance: typing.Optional[AltitudeProvenance] = pydantic.Field(default=None)
    """
    The provenance of the measurement.
    """

    value_meters: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="valueMeters"),
        pydantic.Field(alias="valueMeters", description="The altitude value in meters."),
    ] = None
    """
    The altitude value in meters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
