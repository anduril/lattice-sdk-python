# This file was auto-generated from our API Definition.

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DeliveryConstraints(UniversalBaseModel):
    """
    DeliveryConstraints defines when Lattice should deliver the task to the agent.
    """

    deliver_after: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deliverAfter"),
        pydantic.Field(
            alias="deliverAfter", description="Optional earliest time the task can attempt to be delivered."
        ),
    ] = None
    """
    Optional earliest time the task can attempt to be delivered.
    """

    deliver_before: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deliverBefore"),
        pydantic.Field(
            alias="deliverBefore",
            description="The latest time by which the task should be delivered.\n If this deadline passes without successful delivery of the task, then the task will time\n out with DELIVERY_ERROR_CODE_TIMEOUT.\n This field is only required for tasks with retry strategies.",
        ),
    ] = None
    """
    The latest time by which the task should be delivered.
     If this deadline passes without successful delivery of the task, then the task will time
     out with DELIVERY_ERROR_CODE_TIMEOUT.
     This field is only required for tasks with retry strategies.
    """

    require_acknowledgement: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="requireAcknowledgement"),
        pydantic.Field(
            alias="requireAcknowledgement",
            description="Requires the agent to acknowledge the request before Lattice considers it delivered.\n Without this, a request sent over a streaming agent connection is marked delivered as soon\n as the send returns, which only proves it reached a local buffer and not that the agent\n received it. With this set, the task is not marked delivered until the agent reports a\n status confirming receipt; Lattice re-sends until it does, and eventually fails delivery\n with DELIVERY_ERROR_CODE_NOT_ACKNOWLEDGED. Requires deliver_before, which bounds that\n retrying.",
        ),
    ] = None
    """
    Requires the agent to acknowledge the request before Lattice considers it delivered.
     Without this, a request sent over a streaming agent connection is marked delivered as soon
     as the send returns, which only proves it reached a local buffer and not that the agent
     received it. With this set, the task is not marked delivered until the agent reports a
     status confirming receipt; Lattice re-sends until it does, and eventually fails delivery
     with DELIVERY_ERROR_CODE_NOT_ACKNOWLEDGED. Requires deliver_before, which bounds that
     retrying.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
