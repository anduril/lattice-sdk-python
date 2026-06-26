# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .predicate import Predicate


class PredicateSet(UniversalBaseModel):
    """
    The PredicateSet represents a list of predicates or "leaf nodes" in the expression tree, which
     can be directly evaluated to a boolean TRUE/FALSE result.
    """

    predicates: typing.Optional[typing.List[Predicate]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(PredicateSet)
