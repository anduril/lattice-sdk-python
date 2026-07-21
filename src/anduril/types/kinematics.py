# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .kinematics_geocentric import KinematicsGeocentric
from .kinematics_geodetic import KinematicsGeodetic


class Kinematics(UniversalBaseModel):
    """
    Kinematics of the entity, including its location, location uncertainty, motion, attitude, and the time the
     kinematics were measured.

     Only one of the fields on this message is expected to be set when publishing an entity.
    """

    kinematics_geodetic: typing_extensions.Annotated[
        typing.Optional[KinematicsGeodetic],
        FieldMetadata(alias="kinematicsGeodetic"),
        pydantic.Field(
            alias="kinematicsGeodetic",
            description="Kinematics measured in a geodetic (WGS84 latitude/longitude/altitude and ENU) reference frame.",
        ),
    ] = None
    """
    Kinematics measured in a geodetic (WGS84 latitude/longitude/altitude and ENU) reference frame.
    """

    kinematics_geocentric: typing_extensions.Annotated[
        typing.Optional[KinematicsGeocentric],
        FieldMetadata(alias="kinematicsGeocentric"),
        pydantic.Field(
            alias="kinematicsGeocentric", description="Kinematics measured in a geocentric (ECEF) reference frame."
        ),
    ] = None
    """
    Kinematics measured in a geocentric (ECEF) reference frame.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
