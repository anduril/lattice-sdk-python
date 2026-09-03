# This file was auto-generated from our API Definition.

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper


class RawVideoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper


class AsyncRawVideoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper
