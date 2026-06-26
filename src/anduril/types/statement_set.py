# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class StatementSet(UniversalBaseModel):
    """
    The StatementSet represents a list of statements or "tree nodes," each of which follow the same
     behavior as the Statement proto message.
    """

    statements: typing.Optional[typing.List["Statement"]] = None

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
from .statement import Statement  # noqa: E402, I001

update_forward_refs(
    StatementSet,
    AndOperation=AndOperation,
    ListOperation=ListOperation,
    NotOperation=NotOperation,
    OrOperation=OrOperation,
    Statement=Statement,
)
