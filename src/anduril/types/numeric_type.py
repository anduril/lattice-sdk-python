# This file was auto-generated from our API Definition.

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NumericType(UniversalBaseModel):
    """
    The NumericType represents static numeric values. It supports all numeric primitives supported
     by the proto3 language specification.
    """

    double_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="doubleValue"), pydantic.Field(alias="doubleValue")
    ] = None
    float_value: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="floatValue"), pydantic.Field(alias="floatValue")
    ] = None
    int32value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="int32Value"), pydantic.Field(alias="int32Value")
    ] = None
    int64value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="int64Value"), pydantic.Field(alias="int64Value")
    ] = None
    uint32value: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="uint32Value"), pydantic.Field(alias="uint32Value")
    ] = None
    uint64value: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="uint64Value"), pydantic.Field(alias="uint64Value")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
