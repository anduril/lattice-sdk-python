# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .list_operation_list_comparator import ListOperationListComparator


class ListOperation(UniversalBaseModel):
    """
    The ListOperation represents an operation against a proto list. If the list is of primitive proto
     type (e.g. int32), paths in all child predicates should be left empty. If the list is of message
     proto type (e.g. Sensor), paths in all child predicates should be relative to the list path.

     For example, the criteria "take an action if an entity has any sensor with sensor_id='sensor' and
     OperationalState=STATE_OFF" would be modeled as:
     Predicate1: { path: "sensor_id", comparator: EQUAL_TO, value: "sensor" }
     Predicate2: { path: "operational_state", comparator: EQUAL_TO, value: STATE_OFF }

     Statement2: { AndOperation: PredicateSet: { <Predicate1>, <Predicate2> } }
     ListOperation: { list_path: "sensors.sensors", list_comparator: ANY, statement: <Statement2> }
     Statement1: { ListOperation: <ListOperation> }

     Note that in the above, the child predicates of the list operation have paths relative to the
     list_path because the list is comprised of message not primitive types.
    """

    list_path: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="listPath"),
        pydantic.Field(
            alias="listPath",
            description="The list_path specifies the repeated field on an entity to which this operation applies.",
        ),
    ] = None
    list_comparator: typing_extensions.Annotated[
        typing.Optional[ListOperationListComparator],
        FieldMetadata(alias="listComparator"),
        pydantic.Field(
            alias="listComparator",
            description="The list_comparator specifies how to compose the boolean results from the child statement\n for each member of the specified list.",
        ),
    ] = None
    statement: typing.Optional["Statement"] = pydantic.Field(default=None)
    """
    The statement is a new expression tree conceptually rooted at type of the list. It determines
     how each member of the list is evaluated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .and_operation import AndOperation  # noqa: E402, I001
from .not_operation import NotOperation  # noqa: E402, I001
from .or_operation import OrOperation  # noqa: E402, I001
from .statement import Statement  # noqa: E402, I001
from .statement_set import StatementSet  # noqa: E402, I001

update_forward_refs(
    ListOperation,
    AndOperation=AndOperation,
    NotOperation=NotOperation,
    OrOperation=OrOperation,
    Statement=Statement,
    StatementSet=StatementSet,
)
