# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: anduril/type/attribution.pub.proto, anduril/type/color.pub.proto, anduril/type/coords.pub.proto, anduril/type/geometry.pub.proto, anduril/type/orbit.pub.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from datetime import datetime
from typing import (
    List,
    Optional,
)

import betterproto


class LlaAltitudeReference(betterproto.Enum):
    """What altitude of zero refers to."""

    ALTITUDE_REFERENCE_INVALID = 0
    """
    Depending on the context its possible INVALID just means that it is
     clear from the context (e.g. this is LLA is named lla_hae).
     This also might mean AGL which would depend on what height map you are
     using.
    """

    ALTITUDE_REFERENCE_HEIGHT_ABOVE_WGS84 = 1
    ALTITUDE_REFERENCE_HEIGHT_ABOVE_EGM96 = 2
    ALTITUDE_REFERENCE_UNKNOWN = 3
    ALTITUDE_REFERENCE_BAROMETRIC = 4
    ALTITUDE_REFERENCE_ABOVE_SEA_FLOOR = 5
    ALTITUDE_REFERENCE_BELOW_SEA_SURFACE = 6


class MeanElementTheory(betterproto.Enum):
    INVALID = 0
    SGP4 = 1


class EciReferenceFrame(betterproto.Enum):
    INVALID = 0
    TEME = 1


@dataclass(eq=False, repr=False)
class ThetaPhi(betterproto.Message):
    """Spherical angular coordinates"""

    theta: float = betterproto.double_field(1)
    """Angle clockwise relative to forward in degrees (Azimuth)."""

    phi: float = betterproto.double_field(2)
    """Angle upward relative to forward in degrees (Elevation)."""


@dataclass(eq=False, repr=False)
class Lla(betterproto.Message):
    lon: float = betterproto.double_field(1)
    lat: float = betterproto.double_field(2)
    alt: float = betterproto.double_field(3)
    is2_d: bool = betterproto.bool_field(4)
    altitude_reference: "LlaAltitudeReference" = betterproto.enum_field(5)
    """
    Meaning of alt.
     altitude in meters above either WGS84 or EGM96, use altitude_reference to
     determine what zero means.
    """


@dataclass(eq=False, repr=False)
class Enu(betterproto.Message):
    e: float = betterproto.double_field(1)
    n: float = betterproto.double_field(2)
    u: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class Eci(betterproto.Message):
    """
    Holds ECI (Earth-Centered Inertial, https://en.wikipedia.org/wiki/Earth-centered_inertial)
     coordinates.
    """

    x: float = betterproto.double_field(1)
    """Holds the x-coordinate of ECI."""

    y: float = betterproto.double_field(2)
    """Holds the y-coordinate of ECI."""

    z: float = betterproto.double_field(3)
    """Holds the z-coordinate of ECI."""


@dataclass(eq=False, repr=False)
class Vec2(betterproto.Message):
    x: float = betterproto.double_field(1)
    y: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class Vec2F(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)


@dataclass(eq=False, repr=False)
class Vec3(betterproto.Message):
    x: float = betterproto.double_field(1)
    y: float = betterproto.double_field(2)
    z: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class Vec3F(betterproto.Message):
    x: float = betterproto.float_field(1)
    y: float = betterproto.float_field(2)
    z: float = betterproto.float_field(3)


@dataclass(eq=False, repr=False)
class Quaternion(betterproto.Message):
    x: float = betterproto.double_field(1)
    """x, y, z are vector portion, w is scalar"""

    y: float = betterproto.double_field(2)
    z: float = betterproto.double_field(3)
    w: float = betterproto.double_field(4)


@dataclass(eq=False, repr=False)
class YawPitch(betterproto.Message):
    """Yaw-Pitch in radians"""

    yaw: float = betterproto.double_field(1)
    pitch: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class Ypr(betterproto.Message):
    """Yaw-Pitch-Roll in degrees."""

    yaw: float = betterproto.double_field(1)
    pitch: float = betterproto.double_field(2)
    roll: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class Pose(betterproto.Message):
    pos: "Lla" = betterproto.message_field(1)
    """Geospatial location defined by this Pose."""

    att_enu: "Quaternion" = betterproto.message_field(2)
    """
    The quaternion to transform a point in the Pose frame to the ENU frame. The Pose frame could be Body, Turret,
     etc and is determined by the context in which this Pose is used.
     The normal convention for defining orientation is to list the frames of transformation, for example
     att_gimbal_to_enu is the quaternion which transforms a point in the gimbal frame to the body frame, but
     in this case we truncate to att_enu because the Pose frame isn't defined. A potentially better name for this
     field would have been att_pose_to_enu.
    
     Implementations of this quaternion should left multiply this quaternion to transform a point from the Pose frame
     to the enu frame.
    
     Point<Pose\> posePt{1,0,0};
     Rotation<Enu, Pose\> attPoseToEnu{};
     Point<Enu\> = attPoseToEnu*posePt;
    
     This transformed point represents some vector in ENU space that is aligned with the x axis of the attPoseToEnu
     matrix.
    
     An alternative matrix expression is as follows:
     ptEnu = M x ptPose
    """


@dataclass(eq=False, repr=False)
class LlaPolygon(betterproto.Message):
    points: List["Lla"] = betterproto.message_field(1)
    """
    standard is that points are defined in a counter-clockwise order. this
     is only the exterior ring of a polygon, no holes are supported.
    """


@dataclass(eq=False, repr=False)
class AerPolygon(betterproto.Message):
    points: List["Spherical"] = betterproto.message_field(1)
    """Azimuth-Range-Elevation"""


@dataclass(eq=False, repr=False)
class LlaPath(betterproto.Message):
    points: List["Lla"] = betterproto.message_field(1)
    """Ordered list of points on the path."""

    loop: bool = betterproto.bool_field(2)
    """
    True if the last point on the path connects to the first in a closed
     loop
    """


@dataclass(eq=False, repr=False)
class Spherical(betterproto.Message):
    az: float = betterproto.double_field(1)
    """azimuth angle in radians"""

    el: float = betterproto.double_field(2)
    """elevation angle in radians, we'll use 0 = XY plane"""

    range: float = betterproto.double_field(3)
    """range in meters"""


@dataclass(eq=False, repr=False)
class DoubleRange(betterproto.Message):
    min: float = betterproto.double_field(1)
    max: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class Uint64Range(betterproto.Message):
    min: int = betterproto.uint64_field(1)
    max: int = betterproto.uint64_field(2)


@dataclass(eq=False, repr=False)
class TMat4F(betterproto.Message):
    """
    A symmetric 4D matrix only representing the upper right triangle, useful for covariance matrices.
    """

    m00: float = betterproto.float_field(1)
    m01: float = betterproto.float_field(2)
    m02: float = betterproto.float_field(3)
    m03: float = betterproto.float_field(4)
    m11: float = betterproto.float_field(5)
    m12: float = betterproto.float_field(6)
    m13: float = betterproto.float_field(7)
    m22: float = betterproto.float_field(8)
    m23: float = betterproto.float_field(9)
    m33: float = betterproto.float_field(10)


@dataclass(eq=False, repr=False)
class TMat3(betterproto.Message):
    """
    A symmetric 3D matrix only representing the upper right triangle, useful for covariance matrices.
    """

    mxx: float = betterproto.double_field(1)
    mxy: float = betterproto.double_field(2)
    mxz: float = betterproto.double_field(3)
    myy: float = betterproto.double_field(4)
    myz: float = betterproto.double_field(5)
    mzz: float = betterproto.double_field(6)


@dataclass(eq=False, repr=False)
class TMat2(betterproto.Message):
    """
    symmetric 2d matrix only representing the upper right triangle, useful for
     covariance matrices
    """

    mxx: float = betterproto.double_field(1)
    mxy: float = betterproto.double_field(2)
    myy: float = betterproto.double_field(3)


@dataclass(eq=False, repr=False)
class RigidTransform(betterproto.Message):
    """
    Rx + t, Technically this is a duplicate of AffineTransform
     but Affine Transform isn't really an affine transform (since it doesn't allow
     skewing and stretching).
    """

    rotation: "Quaternion" = betterproto.message_field(3)
    translation: "Vec3" = betterproto.message_field(4)


@dataclass(eq=False, repr=False)
class OrbitMeanElements(betterproto.Message):
    """
    Orbit Mean Elements data, analogous to the Orbit Mean Elements Message in CCSDS 502.0-B-3
    """

    metadata: "OrbitMeanElementsMetadata" = betterproto.message_field(1)
    mean_keplerian_elements: "MeanKeplerianElements" = betterproto.message_field(2)
    tle_parameters: "TleParameters" = betterproto.message_field(3)


@dataclass(eq=False, repr=False)
class OrbitMeanElementsMetadata(betterproto.Message):
    creation_date: datetime = betterproto.message_field(1)
    """Creation date/time in UTC"""

    originator: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    """Creating agency or operator"""

    message_id: Optional[str] = betterproto.message_field(
        3, wraps=betterproto.TYPE_STRING
    )
    """ID that uniquely identifies a message from a given originator."""

    ref_frame: "EciReferenceFrame" = betterproto.enum_field(4)
    """Reference frame, assumed to be Earth-centered"""

    ref_frame_epoch: datetime = betterproto.message_field(5)
    """
    Reference frame epoch in UTC - mandatory only if not intrinsic to frame definition
    """

    mean_element_theory: "MeanElementTheory" = betterproto.enum_field(6)


@dataclass(eq=False, repr=False)
class MeanKeplerianElements(betterproto.Message):
    epoch: datetime = betterproto.message_field(1)
    """UTC time of validity"""

    semi_major_axis_km: float = betterproto.double_field(2, group="line2_field8")
    """Preferred: semi major axis in kilometers"""

    mean_motion: float = betterproto.double_field(3, group="line2_field8")
    """
    If using SGP/SGP4, provide the Keplerian Mean Motion in revolutions per day
    """

    eccentricity: float = betterproto.double_field(4)
    inclination_deg: float = betterproto.double_field(5)
    """Angle of inclination in deg"""

    ra_of_asc_node_deg: float = betterproto.double_field(6)
    """Right ascension of the ascending node in deg"""

    arg_of_pericenter_deg: float = betterproto.double_field(7)
    """Argument of pericenter in deg"""

    mean_anomaly_deg: float = betterproto.double_field(8)
    """Mean anomaly in deg"""

    gm: Optional[float] = betterproto.message_field(9, wraps=betterproto.TYPE_DOUBLE)
    """
    Optional: gravitational coefficient (Gravitational Constant x central mass) in kg^3 / s^2
    """


@dataclass(eq=False, repr=False)
class TleParameters(betterproto.Message):
    ephemeris_type: Optional[int] = betterproto.message_field(
        1, wraps=betterproto.TYPE_UINT32
    )
    """Integer specifying TLE ephemeris type"""

    classification_type: Optional[str] = betterproto.message_field(
        2, wraps=betterproto.TYPE_STRING
    )
    """User-defined free-text message classification/caveats of this TLE"""

    norad_cat_id: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT32
    )
    """Norad catalog number: integer up to nine digits."""

    element_set_no: Optional[int] = betterproto.message_field(
        4, wraps=betterproto.TYPE_UINT32
    )
    rev_at_epoch: Optional[int] = betterproto.message_field(
        5, wraps=betterproto.TYPE_UINT32
    )
    """Optional: revolution number"""

    bstar: float = betterproto.double_field(6, group="line1_field11")
    """Drag parameter for SGP-4 in units 1 / Earth radii"""

    bterm: float = betterproto.double_field(7, group="line1_field11")
    """Drag parameter for SGP4-XP in units m^2 / kg"""

    mean_motion_dot: Optional[float] = betterproto.message_field(
        8, wraps=betterproto.TYPE_DOUBLE
    )
    """First time derivative of mean motion in rev / day^2"""

    mean_motion_ddot: float = betterproto.double_field(9, group="line1_field10")
    """
    Second time derivative of mean motion in rev / day^3. For use with SGP or PPT3.
    """

    agom: float = betterproto.double_field(10, group="line1_field10")
    """
    Solar radiation pressure coefficient A_gamma / m in m^2 / kg. For use with SGP4-XP.
    """


@dataclass(eq=False, repr=False)
class Color(betterproto.Message):
    red: float = betterproto.float_field(1)
    """The amount of red in the color as a value in the interval [0, 1]."""

    green: float = betterproto.float_field(2)
    """The amount of green in the color as a value in the interval [0, 1]."""

    blue: float = betterproto.float_field(3)
    """The amount of blue in the color as a value in the interval [0, 1]."""

    alpha: Optional[float] = betterproto.message_field(4, wraps=betterproto.TYPE_FLOAT)
    """
    The fraction of this color that should be applied to the pixel. That is,
     the final pixel color is defined by the equation:
    
     `pixel color = alpha * (this color) + (1.0 - alpha) * (background color)`
    
     This means that a value of 1.0 corresponds to a solid color, whereas
     a value of 0.0 corresponds to a completely transparent color. This
     uses a wrapper message rather than a simple float scalar so that it is
     possible to distinguish between a default value and the value being unset.
     If omitted, this color object is rendered as a solid color
     (as if the alpha value had been explicitly given a value of 1.0).
    """


@dataclass(eq=False, repr=False)
class Attribution(betterproto.Message):
    timestamp: int = betterproto.int64_field(1)
    """
    The timestamp at which the event occurred, in UTC epoch microseconds.
    """

    user_id: str = betterproto.string_field(2)
    """The user ID that initiated the event."""


@dataclass(eq=False, repr=False)
class Grid(betterproto.Message):
    """A 2d grid with binary values for each grid cell."""

    bottom_left_pos: "Lla" = betterproto.message_field(1)
    """
    The bottom left extent of the 2d grid. This represents the
     farthest corner on the grid cell, not the center of the
     grid cell.
    """

    top_right_pos: "Lla" = betterproto.message_field(2)
    """
    The top right extent of the 2d grid. This represents the
     farthest corner on the grid cell, not the center of the
     grid cell.
    """

    grid_width: int = betterproto.uint32_field(3)
    """The width of the grid in number of cells."""

    grid_height: int = betterproto.uint32_field(4)
    """The height of the grid in number of cells."""

    cell_values: bytes = betterproto.bytes_field(5)
    """
    Stores the cell values. Each byte contains 8 bits representing
     binary values of cells. Cells are unravelled in row-major order,
     with the first cell located at the top-left corner of the grid.
     In a single byte, the smallest bit represents the left most cell.
    """
