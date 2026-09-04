# This file was auto-generated from our API Definition.

import typing

from ...core.api_error import ApiError
from ...types.google_rpc_status import GoogleRpcStatus


class NotFoundError(ApiError):
    def __init__(self, body: GoogleRpcStatus, headers: typing.Optional[typing.Dict[str, str]] = None):
        super().__init__(status_code=404, headers=headers, body=body)
