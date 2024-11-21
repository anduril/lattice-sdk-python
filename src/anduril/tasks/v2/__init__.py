# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: anduril/tasks/v2/catalog.pub.proto, anduril/tasks/v2/common.pub.proto, anduril/tasks/v2/objective.pub.proto, anduril/tasks/v2/shared/isr.pub.proto, anduril/tasks/v2/shared/maneuver.pub.proto, anduril/tasks/v2/shared/strike.pub.proto
# plugin: python-betterproto
# This file has been @generated
import warnings
from dataclasses import dataclass
from datetime import (
    datetime,
    timedelta,
)
from typing import (
    List,
    Optional,
)

import betterproto
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf

from ... import type as __type__


class ControlAreaType(betterproto.Enum):
    INVALID = 0
    KEEP_IN_ZONE = 1
    KEEP_OUT_ZONE = 2
    DITCH_ZONE = 3
    """
    Zone for an autonomous asset to nose-dive into
     when its assignment has been concluded
    """


class OrbitDirection(betterproto.Enum):
    """Direction of the loiter relative to the front of the vehicle."""

    DIRECTION_INVALID = 0
    RIGHT = 1
    LEFT = 2


class OrbitPattern(betterproto.Enum):
    INVALID = 0
    CIRCLE = 1
    RACETRACK = 2
    FIGURE_EIGHT = 3


class LaunchTrackingMode(betterproto.Enum):
    INVALID = 0
    GO_TO_WAYPOINT = 1
    TRACK_TO_WAYPOINT = 2


@dataclass(eq=False, repr=False)
class TaskCatalog(betterproto.Message):
    """Catalog of supported tasks."""

    task_definitions: List["TaskDefinition"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class TaskDefinition(betterproto.Message):
    """
    Defines a supported task by the task specification URL of its "Any" type.
    """

    task_specification_url: str = betterproto.string_field(1)
    display_name: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class DurationRange(betterproto.Message):
    """Maps to the UCI DurationRangeType."""

    min: timedelta = betterproto.message_field(1)
    max: timedelta = betterproto.message_field(2)


@dataclass(eq=False, repr=False)
class AnglePair(betterproto.Message):
    """Maps to the UCI AnglePair."""

    min: float = betterproto.double_field(1)
    """Angle lower bound in radians."""

    max: float = betterproto.double_field(2)
    """Angle lower bound in radians."""


@dataclass(eq=False, repr=False)
class AreaConstraints(betterproto.Message):
    """Maps to UCI AreaConstraints."""

    altitude_constraint: "AltitudeConstraint" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class AltitudeConstraint(betterproto.Message):
    min: float = betterproto.double_field(1)
    """Minimum altitude (AGL) in meters."""

    max: float = betterproto.double_field(2)
    """Maximum altitude (AGL) in meters."""


@dataclass(eq=False, repr=False)
class Agent(betterproto.Message):
    """Includes information about an Agent."""

    entity_id: str = betterproto.string_field(2)


@dataclass(eq=False, repr=False)
class ControlArea(betterproto.Message):
    """Models a Control Area within which Agents must operate."""

    entity_id: str = betterproto.string_field(1)
    """Reference to GeoPolygon GeoEntity representing the ControlArea."""

    control_area_type: "ControlAreaType" = betterproto.enum_field(2)
    """Type of ControlArea."""


@dataclass(eq=False, repr=False)
class Objective(betterproto.Message):
    """Describes the objective of a task."""

    entity_id: str = betterproto.string_field(1, group="objective")
    """
    Prefer Entity Objectives whenever the objective is in fact an entity. In other words, don't take position/point
     out of an entity and pass it as a simple point.
    """

    point: "Point" = betterproto.message_field(5, group="objective")
    """
    Point objectives for simple reference points that are not geo entities.
    """


@dataclass(eq=False, repr=False)
class Point(betterproto.Message):
    """Describes a single point location."""

    reference_name: str = betterproto.string_field(1)
    """A human readable name for the point."""

    lla: "__type__.Lla" = betterproto.message_field(2)
    """Indicates the objective is the provided location."""

    backing_entity_id: str = betterproto.string_field(3)
    """
    An optional entity id that is provided for reverse lookup purposes. This may be used any time the UI might
     have to convert a geoentity to statically defined LLA.
    """


@dataclass(eq=False, repr=False)
class Investigate(betterproto.Message):
    """Maps to BREVITY code INVESTIGATE."""

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to investigate."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class VisualId(betterproto.Message):
    """Maps to BREVITY code ID with type Visual."""

    objective: "Objective" = betterproto.message_field(1)
    """Indicates what to identify."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class Map(betterproto.Message):
    """Maps to BREVITY code MAP."""

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to perform the SAR."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""

    min_niirs: Optional[int] = betterproto.message_field(
        3, wraps=betterproto.TYPE_UINT32
    )
    """
    minimum desired NIIRS (National Image Interpretability Rating Scales) see https://irp.fas.org/imint/niirs.htm
    """


@dataclass(eq=False, repr=False)
class Loiter(betterproto.Message):
    """
    Maps to the Loiter behavior within the FlightTask type within UCI v2.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to perform the loiter."""

    loiter_type: "LoiterType" = betterproto.message_field(2)
    """Specifies the details of the loiter."""

    parameters: "IsrParameters" = betterproto.message_field(3)
    """
    Optional common ISR parameters.
     The loiter radius and bearing should be inferred from the standoff_distance and standoff_angle respectively.
    """


@dataclass(eq=False, repr=False)
class AreaSearch(betterproto.Message):
    """
    Represents intent to search an area. Maps to the Area Search Team Task within the Mission Autonomy Task Model.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to perform the area search."""

    priors: List["Prior"] = betterproto.message_field(2)
    """Priors that can be used to inform this AreaSearch."""

    participants: List["Agent"] = betterproto.message_field(3)
    """Agents participating in this AreaSearch."""

    control_areas: List["ControlArea"] = betterproto.message_field(4)
    """Control Area for this AreaSearch."""


@dataclass(eq=False, repr=False)
class VolumeSearch(betterproto.Message):
    """
    Represents intent to search a volume. Maps to the Volume Search Team Task within the Mission Autonomy Task Model.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to perform the volume search."""

    priors: List["Prior"] = betterproto.message_field(2)
    """Priors that can be used to inform this VolumeSearch."""

    participants: List["Agent"] = betterproto.message_field(3)
    """Agents participating in this VolumeSearch."""

    control_areas: List["ControlArea"] = betterproto.message_field(4)
    """Control Area for this VolumeSearch."""


@dataclass(eq=False, repr=False)
class ImproveTrackQuality(betterproto.Message):
    """
    Task to improve the quality of a track. Maps to the Improve Track Task within the Mission Autonomy Task Model.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates the target track that is having its quality improved."""

    termination_track_quality: int = betterproto.uint32_field(2)
    """
    Task will complete when the requested track reaches a TQ >= the termination_track_quality.
    """


@dataclass(eq=False, repr=False)
class Shadow(betterproto.Message):
    """
    Indicates intent to follow an Objective. Maps to Brevity code SHADOW.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates what to follow."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class LoiterType(betterproto.Message):
    """Maps to UCI v2 LoiterType."""

    orbit_type: "OrbitType" = betterproto.message_field(1, group="loiter_type")


@dataclass(eq=False, repr=False)
class OrbitType(betterproto.Message):
    direction: "OrbitDirection" = betterproto.enum_field(1)
    """Indicates the direction in which to perform the loiter."""

    pattern: "OrbitPattern" = betterproto.enum_field(2)
    """Indicates the loiter pattern to perform."""

    duration: "OrbitDuration" = betterproto.message_field(3)
    """Indicates the amount of time to be spent in loiter."""


@dataclass(eq=False, repr=False)
class OrbitDuration(betterproto.Message):
    duration_range: "DurationRange" = betterproto.message_field(1, group="duration")
    num_of_orbits: int = betterproto.uint64_field(2, group="duration")


@dataclass(eq=False, repr=False)
class Prior(betterproto.Message):
    """A Prior that can be used to inform an ISR Task."""

    entity_id: str = betterproto.string_field(1, group="prior")
    """
    Prefer Entity priors whenever the prior is in fact an entity. In other words, don't take position/point
     out of an entity and pass it as a simple point.
    """

    point: "Point" = betterproto.message_field(5, group="prior")
    """Point priors for simple reference points that are not geo entities."""


@dataclass(eq=False, repr=False)
class IsrParameters(betterproto.Message):
    """Common parameters for ISR Tasks."""

    speed: Optional[float] = betterproto.message_field(1, wraps=betterproto.TYPE_FLOAT)
    """
    Indicates the target speed of the asset. DEPRECATION NOTE: deprecated in favor
     of speed_ms since we might have legacy integrations not conforming to the meters per second units.
    """

    speed_m_s: Optional[float] = betterproto.message_field(
        2, wraps=betterproto.TYPE_FLOAT
    )
    """
    Indicates the target speed of the asset. Units are meters per second.
    """

    standoff_distance_m: Optional[float] = betterproto.message_field(
        3, wraps=betterproto.TYPE_FLOAT
    )
    """
    Indicates the standoff distance from the objective. The units are in meters.
    """

    standoff_distance: Optional[float] = betterproto.message_field(
        4, wraps=betterproto.TYPE_FLOAT
    )
    """
    Indicates the standoff distance from the objective. DEPRECATION NOTE: deprecated in favor of standoff_distance_m
      since we might have legacy integrations not conforming to the meters unit.
    """

    standoff_angle: Optional[float] = betterproto.message_field(
        5, wraps=betterproto.TYPE_FLOAT
    )
    """
    Indicates the standoff angle relative to the objective's bearing orientation (defaults to north).
     In particular, the asset should approach target from this angle. Units in degrees.
    """

    expiration_time_ms: Optional[int] = betterproto.message_field(
        6, wraps=betterproto.TYPE_UINT64
    )
    """
    Indicates the amount of time in milliseconds to execute an ISR task before expiring. 0 value indicates no
     expiration.
    """

    def __post_init__(self) -> None:
        super().__post_init__()
        if self.is_set("speed"):
            warnings.warn("IsrParameters.speed is deprecated", DeprecationWarning)
        if self.is_set("standoff_distance"):
            warnings.warn(
                "IsrParameters.standoff_distance is deprecated", DeprecationWarning
            )


@dataclass(eq=False, repr=False)
class GimbalPoint(betterproto.Message):
    """Gimbal pointing command."""

    look_at: "Objective" = betterproto.message_field(1, group="point_type")
    """
    Point the gimbal at and lock on, continuing to look at a specific objective even as the platform moves.
    """

    celestial_location: "AzimuthElevationPoint" = betterproto.message_field(
        2, group="point_type"
    )
    """
    Point the gimbal at a fixed azimuth/elevation with respect to the platform frame.
    """

    frame_location: "FramePoint" = betterproto.message_field(4, group="point_type")
    """Point gimbal to an [x, y] location in the video feed."""

    parameters: "IsrParameters" = betterproto.message_field(3)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class AzimuthElevationPoint(betterproto.Message):
    """Celestial location with respect to a platform frame."""

    azimuth: float = betterproto.double_field(1)
    elevation: float = betterproto.double_field(2)


@dataclass(eq=False, repr=False)
class FramePoint(betterproto.Message):
    """Point clicked in the frame of the video feed."""

    x: float = betterproto.float_field(1)
    """
    Frame-normalized location in frame on the x-axis, range (0, 1).
     For example, x = 0.3 implies a pixel location of 0.3 * image_width.
    """

    y: float = betterproto.float_field(2)
    """
    Frame-normalized location in frame on the y-axis, range (0, 1).
     For example, y = 0.3 implies a pixel location of 0.3 * image_height.
    """

    timestamp: datetime = betterproto.message_field(3)
    """Timestamp of frame"""


@dataclass(eq=False, repr=False)
class GimbalZoom(betterproto.Message):
    """Command for setting gimbal zoom levels."""

    set_horizontal_fov: Optional[float] = betterproto.message_field(
        1, wraps=betterproto.TYPE_DOUBLE, group="mode"
    )
    """
    Set the zoom level to the provided horizontal field of view in degrees.
    """

    set_magnification: Optional[float] = betterproto.message_field(
        2, wraps=betterproto.TYPE_FLOAT, group="mode"
    )
    """Set the zoom level to the provided zoom level."""


@dataclass(eq=False, repr=False)
class Monitor(betterproto.Message):
    """
    Maps to BREVITY code ID with type MONITOR. To task assets to maintain sensor awareness
     on a given objective.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates objective to monitor."""


@dataclass(eq=False, repr=False)
class Scan(betterproto.Message):
    """
    Maps to BREVITY code ID with type SCAN. To task assets to find and report any tracks in a geographic area.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Indicates where to scan."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class BattleDamageAssessment(betterproto.Message):
    """
    Performs a Battle Damage Assessment (BDA). Does not map to any Task in either UCI or BREVITY.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Objective to perform BDA on."""

    parameters: "IsrParameters" = betterproto.message_field(2)
    """Optional common ISR parameters."""


@dataclass(eq=False, repr=False)
class Marshal(betterproto.Message):
    """
    Maps to BREVITY code Marshal.
     Establish(ed) at a specific point, typically used to posture forces in preparation for an offensive operation.
    """

    objective: "Objective" = betterproto.message_field(1)
    """Objective to Marshal to."""


@dataclass(eq=False, repr=False)
class Transit(betterproto.Message):
    """
    Maps to UCI code RoutePlan.
     Used to command a platform between locations by requesting to make this RoutePlan the single primary active route.
    """

    plan: "RoutePlan" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class RoutePlan(betterproto.Message):
    route: "Route" = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class Route(betterproto.Message):
    path: List["PathSegment"] = betterproto.message_field(1)


@dataclass(eq=False, repr=False)
class PathSegment(betterproto.Message):
    waypoint: "Waypoint" = betterproto.message_field(1, group="end_point")
    loiter: "Loiter" = betterproto.message_field(2, group="end_point")


@dataclass(eq=False, repr=False)
class Waypoint(betterproto.Message):
    lla_point: "Point" = betterproto.message_field(1, group="point")


@dataclass(eq=False, repr=False)
class SetLaunchRoute(betterproto.Message):
    plan: "RoutePlan" = betterproto.message_field(1)
    tracking_mode: "LaunchTrackingMode" = betterproto.enum_field(2)


@dataclass(eq=False, repr=False)
class Smack(betterproto.Message):
    """Maps to BREVITY code SMACK."""

    objective: "Objective" = betterproto.message_field(1)
    """Objective to SMACK."""

    parameters: "StrikeParameters" = betterproto.message_field(2)
    """Optional parameters associated with Strike Tasks."""


@dataclass(eq=False, repr=False)
class Strike(betterproto.Message):
    """Maps to UCI StrikeTask."""

    objective: "Objective" = betterproto.message_field(1)
    """Objective to Strike."""

    ingress_angle: "AnglePair" = betterproto.message_field(2)
    """Angle range within which to ingress."""

    strike_release_constraint: "StrikeReleaseConstraint" = betterproto.message_field(3)
    """
    Distance at which to yield flight control to the onboard flight computer rather than
     higher level autonomy.
    """

    parameters: "StrikeParameters" = betterproto.message_field(4)
    """Optional parameters associated with the Strike task."""


@dataclass(eq=False, repr=False)
class StrikeReleaseConstraint(betterproto.Message):
    """Maps to UCI StrikeTaskReleaseConstraintsType."""

    release_area: "AreaConstraints" = betterproto.message_field(
        1, group="strike_release_constraint"
    )


@dataclass(eq=False, repr=False)
class StrikeParameters(betterproto.Message):
    payloads_to_employ: List["PayloadConfiguration"] = betterproto.message_field(1)
    desired_impact_time: timedelta = betterproto.message_field(2)
    """GPS time at which the strike should be performed."""

    run_in_bearing: float = betterproto.double_field(3)
    """Bearing at which to perform the run in for a strike."""

    glide_slope_angle: float = betterproto.double_field(4)
    """Angle which to glide into the run in for a strike."""


@dataclass(eq=False, repr=False)
class PayloadConfiguration(betterproto.Message):
    """
    Individual payload configuration, can represent a munition such as a missile, a gun, or a non-kinetic effect.
    """

    capability_id: str = betterproto.string_field(1)
    """Unique ID or descriptor for the capability."""

    quantity: int = betterproto.uint32_field(2)


@dataclass(eq=False, repr=False)
class ReleasePayload(betterproto.Message):
    """Releases a payload from the vehicle"""

    payloads: List["PayloadConfiguration"] = betterproto.message_field(1)
    """The payload(s) that will be released"""

    objective: "Objective" = betterproto.message_field(2)
    """
    Optional objective, of where the payload should be dropped. If omitted the payload will drop the current location
    """

    precision_release: "betterproto_lib_google_protobuf.Empty" = (
        betterproto.message_field(3, group="release_method")
    )
    """Attempt to place the payload delicately from a standstill"""
