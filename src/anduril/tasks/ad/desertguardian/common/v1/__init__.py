# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: anduril/tasks/ad/desertguardian/common/v1/common_tasks.pub.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


class PowerState(betterproto.Enum):
    INVALID = 0
    ON = 1
    OFF = 2


@dataclass(eq=False, repr=False)
class SetPowerState(betterproto.Message):
    """
    Set the power state of a Platform. It is up to the Platform to interpret the power state and act accordingly.
    """

    power_state: "PowerState" = betterproto.enum_field(1)


@dataclass(eq=False, repr=False)
class DeleteTrack(betterproto.Message):
    """
    Delete an entity from the internal tracker of a Platform.
     Does not silence or suppress the track from re-forming if the tracking conditions are satisfied.
    """

    entity_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class SetHighPriorityTrack(betterproto.Message):
    """
    Set this entity as a "High Priority Track".
     The tasked Platform is responsible for maintaining a list of current High-Priority tracks.
    """

    entity_id: str = betterproto.string_field(1)


@dataclass(eq=False, repr=False)
class RemoveHighPriorityTrack(betterproto.Message):
    """
    Unset this entity as a "High Priority Track".
     The tasked Platform is responsible for maintaining a list of current High-Priority tracks.
    """

    entity_id: str = betterproto.string_field(1)