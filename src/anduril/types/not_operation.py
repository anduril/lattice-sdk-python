# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .predicate import Predicate


class NotOperation(UniversalBaseModel):
    """
    The NotOperation represents the boolean NOT operation, which can only be applied to a single
     child predicate or statement.
    """

    predicate: typing.Optional[Predicate] = None
    statement: typing.Optional["Statement"] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .and_operation import AndOperation  # noqa: E402, I001
from .list_operation import ListOperation  # noqa: E402, I001
from .or_operation import OrOperation  # noqa: E402, I001
from .statement import Statement  # noqa: E402, I001
from .statement_set import StatementSet  # noqa: E402, I001

update_forward_refs(
    NotOperation,
    AndOperation=AndOperation,
    ListOperation=ListOperation,
    OrOperation=OrOperation,
    Statement=Statement,
    StatementSet=StatementSet,
)
