# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from ..core.serialization import FieldMetadata
from .predicate_set import PredicateSet


class OrOperation(UniversalBaseModel):
    """
    The OrOperation represents the boolean OR operation, which is to be applied to the list of
     children statement(s) or predicate(s).
    """

    predicate_set: typing_extensions.Annotated[
        typing.Optional[PredicateSet], FieldMetadata(alias="predicateSet"), pydantic.Field(alias="predicateSet")
    ] = None
    statement_set: typing_extensions.Annotated[
        typing.Optional["StatementSet"], FieldMetadata(alias="statementSet"), pydantic.Field(alias="statementSet")
    ] = None

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
from .statement import Statement  # noqa: E402, I001
from .statement_set import StatementSet  # noqa: E402, I001

update_forward_refs(
    OrOperation,
    AndOperation=AndOperation,
    ListOperation=ListOperation,
    NotOperation=NotOperation,
    Statement=Statement,
    StatementSet=StatementSet,
)
