# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CameraConfiguration(UniversalBaseModel):
    """
    Camera zoom state for a camera sensor. Unset means the entity does not report zoom.
    """

    zoom_percentage: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="zoomPercentage"),
        pydantic.Field(
            alias="zoomPercentage",
            description="Percentage of the camera's zoom range, 0-100. 0 is fully zoomed out, 100 fully zoomed in.",
        ),
    ] = None
    """
    Percentage of the camera's zoom range, 0-100. 0 is fully zoomed out, 100 fully zoomed in.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
