# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .predicate_comparator import PredicateComparator


class Predicate(UniversalBaseModel):
    """
    The Predicate fully encodes the information required to make an evaluation of an entity field
     against a given static value, resulting in a boolean TRUE/FALSE result. The structure of a
     predicate will always follow: "{entity-value} {comparator} {fixed-value}" where the entity value
     is determined by the field path.

     For example, a predicate would read as: "{entity.location.velocity_enu} {LESS_THAN} {500kph}"
    """

    field_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="fieldPath"),
        pydantic.Field(
            alias="fieldPath",
            description="The field_path determines which field on an entity is being referenced in this predicate. For\n example: correlated.primary_entity_id would be primary_entity_id in correlated component.",
        ),
    ] = None
    value: typing.Optional["Value"] = pydantic.Field(default=None)
    """
    The value determines the fixed value against which the entity field is to be compared.
     In the case of COMPARATOR_MATCH_ALL, the value contents do not matter as long as the Value is a supported
     type.
    """

    comparator: typing.Optional[PredicateComparator] = pydantic.Field(default=None)
    """
    The comparator determines the manner in which the entity field and static value are compared.
     Comparators may only be applied to certain values. For example, the WITHIN comparator cannot
     be used for a boolean value comparison.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .list_type import ListType  # noqa: E402, I001
from .value import Value  # noqa: E402, I001

update_forward_refs(Predicate, ListType=ListType, Value=Value)
