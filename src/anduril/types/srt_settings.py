# This file was auto-generated from our API Definition.

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SrtSettings(UniversalBaseModel):
    """
    The Lattice video service supports SRT protocol for push operations (ingress)
     and pull operations (egress).

     When configuring SRT for ingress, CreateIngressStreamResponse will
     return to the user a url to push to which contains a unique 'session_id' to use
     on the connection. If supplied, passphrase will be applied on incoming
     connections.

     When configuring SRT for egress, CreateEgressStreamResponse will
     return to the user a url from which to pull a stream. Use the supplied
     session_id and passphrase in your StreamId if applicable.
     See the SRT documentation on Access Control for more information.
    """

    passphrase: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional passphrase for the stream, set by the user, that applies AES encryption.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
