# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EnumType(UniversalBaseModel):
    """
    The EnumType represents members of well-known anduril ontologies, such as "disposition." When
     such a value is specified, the evaluation library expects the integer representation of the enum
     value. For example, a disposition derived from ontology.v1 such as "DISPOSITION_HOSTILE" should be
     represented with the integer value 2.
    """

    value: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
