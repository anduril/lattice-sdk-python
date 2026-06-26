# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .predicate import Predicate


class Statement(UniversalBaseModel):
    """
    A Statement is the building block of the entity filter. The outermost statement is conceptually
     the root node of an "expression tree" which allows for the construction of complete boolean
     logic statements. Statements are formed by grouping sets of children statement(s) or predicate(s)
     according to the boolean operation which is to be applied.

     For example, the criteria "take an action if an entity is hostile and an air vehicle" can be
     represented as: Statement1: { AndOperation: { Predicate1, Predicate2 } }. Where Statement1
     is the root of the expression tree, with an AND operation that is applied to children
     predicates. The predicates themselves encode "entity is hostile" and "entity is air vehicle."
    """

    and_: typing_extensions.Annotated[
        typing.Optional["AndOperation"], FieldMetadata(alias="and"), pydantic.Field(alias="and")
    ] = None
    or_: typing_extensions.Annotated[
        typing.Optional["OrOperation"], FieldMetadata(alias="or"), pydantic.Field(alias="or")
    ] = None
    not_: typing_extensions.Annotated[
        typing.Optional["NotOperation"], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    list_: typing_extensions.Annotated[
        typing.Optional["ListOperation"], FieldMetadata(alias="list"), pydantic.Field(alias="list")
    ] = None
    predicate: typing.Optional[Predicate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .and_operation import AndOperation  # noqa: E402, I001
from .list_operation import ListOperation  # noqa: E402, I001
from .not_operation import NotOperation  # noqa: E402, I001
from .or_operation import OrOperation  # noqa: E402, I001
from .statement_set import StatementSet  # noqa: E402, I001

update_forward_refs(
    Statement,
    AndOperation=AndOperation,
    ListOperation=ListOperation,
    NotOperation=NotOperation,
    OrOperation=OrOperation,
    StatementSet=StatementSet,
)
