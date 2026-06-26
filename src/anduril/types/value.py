# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .boolean_type import BooleanType
from .bounded_shape_type import BoundedShapeType
from .enum_type import EnumType
from .heading_type import HeadingType
from .numeric_type import NumericType
from .position_type import PositionType
from .range_type import RangeType
from .string_type import StringType
from .timestamp_type import TimestampType


class Value(UniversalBaseModel):
    """
    The Value represents the information against which an entity field is evaluated. It is one of
     a fixed set of types, each of which correspond to specific comparators. See "ComparatorType"
     for the full list of Value <-> Comparator mappings.
    """

    boolean_type: typing_extensions.Annotated[
        typing.Optional[BooleanType], FieldMetadata(alias="booleanType"), pydantic.Field(alias="booleanType")
    ] = None
    numeric_type: typing_extensions.Annotated[
        typing.Optional[NumericType], FieldMetadata(alias="numericType"), pydantic.Field(alias="numericType")
    ] = None
    string_type: typing_extensions.Annotated[
        typing.Optional[StringType], FieldMetadata(alias="stringType"), pydantic.Field(alias="stringType")
    ] = None
    enum_type: typing_extensions.Annotated[
        typing.Optional[EnumType], FieldMetadata(alias="enumType"), pydantic.Field(alias="enumType")
    ] = None
    timestamp_type: typing_extensions.Annotated[
        typing.Optional[TimestampType], FieldMetadata(alias="timestampType"), pydantic.Field(alias="timestampType")
    ] = None
    bounded_shape_type: typing_extensions.Annotated[
        typing.Optional[BoundedShapeType],
        FieldMetadata(alias="boundedShapeType"),
        pydantic.Field(alias="boundedShapeType"),
    ] = None
    position_type: typing_extensions.Annotated[
        typing.Optional[PositionType], FieldMetadata(alias="positionType"), pydantic.Field(alias="positionType")
    ] = None
    heading_type: typing_extensions.Annotated[
        typing.Optional[HeadingType], FieldMetadata(alias="headingType"), pydantic.Field(alias="headingType")
    ] = None
    list_type: typing_extensions.Annotated[
        typing.Optional["ListType"], FieldMetadata(alias="listType"), pydantic.Field(alias="listType")
    ] = None
    range_type: typing_extensions.Annotated[
        typing.Optional[RangeType], FieldMetadata(alias="rangeType"), pydantic.Field(alias="rangeType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .list_type import ListType  # noqa: E402, I001

update_forward_refs(Value, ListType=ListType)
