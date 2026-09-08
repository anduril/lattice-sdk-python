# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .echelon import Echelon
from .platform_subcomponents import PlatformSubcomponents
from .team import Team


class GroupDetails(UniversalBaseModel):
    """
    Details related to grouping for this entity
    """

    team: typing.Optional[Team] = None
    platform_subcomponents: typing_extensions.Annotated[
        typing.Optional[PlatformSubcomponents],
        FieldMetadata(alias="platformSubcomponents"),
        pydantic.Field(alias="platformSubcomponents"),
    ] = None
    echelon: typing.Optional[Echelon] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
