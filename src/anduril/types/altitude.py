# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .altitude_above_ground_level import AltitudeAboveGroundLevel
from .altitude_above_mean_sea_level_egm96 import AltitudeAboveMeanSeaLevelEgm96
from .altitude_above_mean_sea_level_pressure import AltitudeAboveMeanSeaLevelPressure
from .altitude_above_sea_floor import AltitudeAboveSeaFloor
from .altitude_above_standard_datum_plane_pressure import AltitudeAboveStandardDatumPlanePressure
from .altitude_above_wgs84ellipsoid import AltitudeAboveWgs84Ellipsoid
from .altitude_below_sea_surface import AltitudeBelowSeaSurface


class Altitude(UniversalBaseModel):
    hae_wgs84: typing_extensions.Annotated[
        typing.Optional[AltitudeAboveWgs84Ellipsoid], FieldMetadata(alias="haeWgs84"), pydantic.Field(alias="haeWgs84")
    ] = None
    asf: typing.Optional[AltitudeAboveSeaFloor] = None
    bss: typing.Optional[AltitudeBelowSeaSurface] = None
    pressure_sdp: typing_extensions.Annotated[
        typing.Optional[AltitudeAboveStandardDatumPlanePressure],
        FieldMetadata(alias="pressureSdp"),
        pydantic.Field(alias="pressureSdp"),
    ] = None
    pressure_amsl: typing_extensions.Annotated[
        typing.Optional[AltitudeAboveMeanSeaLevelPressure],
        FieldMetadata(alias="pressureAmsl"),
        pydantic.Field(alias="pressureAmsl"),
    ] = None
    egm96amsl: typing_extensions.Annotated[
        typing.Optional[AltitudeAboveMeanSeaLevelEgm96],
        FieldMetadata(alias="egm96Amsl"),
        pydantic.Field(alias="egm96Amsl"),
    ] = None
    agl: typing.Optional[AltitudeAboveGroundLevel] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
