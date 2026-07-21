# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .location_geocentric_ecef import LocationGeocentricEcef
from .quaternion import Quaternion
from .t_mat3 import TMat3
from .vec3 import Vec3


class KinematicsGeocentric(UniversalBaseModel):
    location: typing.Optional[LocationGeocentricEcef] = pydantic.Field(default=None)
    """
    The location of the entity, measured in the ECEF reference frame.
    """

    location_uncertainty_ecef: typing_extensions.Annotated[
        typing.Optional[TMat3],
        FieldMetadata(alias="locationUncertaintyEcef"),
        pydantic.Field(
            alias="locationUncertaintyEcef",
            description="Location uncertainty of this measurement, measured in the ECEF frame.",
        ),
    ] = None
    """
    Location uncertainty of this measurement, measured in the ECEF frame.
    """

    velocity_ecef_m_per_s: typing_extensions.Annotated[
        typing.Optional[Vec3],
        FieldMetadata(alias="velocityEcefMPerS"),
        pydantic.Field(
            alias="velocityEcefMPerS", description="Velocity in the ECEF frame, measured in meters per second."
        ),
    ] = None
    """
    Velocity in the ECEF frame, measured in meters per second.
    """

    velocity_uncertainty_ecef: typing_extensions.Annotated[
        typing.Optional[TMat3],
        FieldMetadata(alias="velocityUncertaintyEcef"),
        pydantic.Field(
            alias="velocityUncertaintyEcef",
            description="A 3x3 covariance matrix representing the uncertainty of the velocity measurement.",
        ),
    ] = None
    """
    A 3x3 covariance matrix representing the uncertainty of the velocity measurement.
    """

    acceleration_m_per_s2: typing_extensions.Annotated[
        typing.Optional[Vec3],
        FieldMetadata(alias="accelerationMPerS2"),
        pydantic.Field(
            alias="accelerationMPerS2", description="The entity's acceleration in meters per second squared."
        ),
    ] = None
    """
    The entity's acceleration in meters per second squared.
    """

    attitude_ecef: typing_extensions.Annotated[
        typing.Optional[Quaternion],
        FieldMetadata(alias="attitudeEcef"),
        pydantic.Field(
            alias="attitudeEcef",
            description="Quaternion that rotates the X unit vector in the entity's body frame (assumed to be front-left-up) [1,0,0]\n to the entity's orientation unit vector in the ECEF frame at the entity's location.",
        ),
    ] = None
    """
    Quaternion that rotates the X unit vector in the entity's body frame (assumed to be front-left-up) [1,0,0]
     to the entity's orientation unit vector in the ECEF frame at the entity's location.
    """

    measurement_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="measurementTime"),
        pydantic.Field(
            alias="measurementTime",
            description="The time when these kinematics were measured by the sensor. For tracks, this represents when the sensor made\n the observation that produced these kinematics. For asset pose data, this represents the system time when the\n pose was captured.",
        ),
    ] = None
    """
    The time when these kinematics were measured by the sensor. For tracks, this represents when the sensor made
     the observation that produced these kinematics. For asset pose data, this represents the system time when the
     pose was captured.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
