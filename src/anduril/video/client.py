# This file was auto-generated from our API Definition.

from __future__ import annotations

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .raw_client import AsyncRawVideoClient, RawVideoClient

if typing.TYPE_CHECKING:
    from .video.client import AsyncVideoClient as video_video_client_AsyncVideoClient
    from .video.client import VideoClient as video_video_client_VideoClient


class VideoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVideoClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._video: typing.Optional[video_video_client_VideoClient] = None

    @property
    def with_raw_response(self) -> RawVideoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVideoClient
        """
        return self._raw_client

    @property
    def video(self):
        if self._video is None:
            from .video.client import VideoClient as video_video_client_VideoClient  # noqa: E402

            self._video = video_video_client_VideoClient(client_wrapper=self._client_wrapper)
        return self._video


class AsyncVideoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVideoClient(client_wrapper=client_wrapper)
        self._client_wrapper = client_wrapper
        self._video: typing.Optional[video_video_client_AsyncVideoClient] = None

    @property
    def with_raw_response(self) -> AsyncRawVideoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVideoClient
        """
        return self._raw_client

    @property
    def video(self):
        if self._video is None:
            from .video.client import AsyncVideoClient as video_video_client_AsyncVideoClient  # noqa: E402

            self._video = video_video_client_AsyncVideoClient(client_wrapper=self._client_wrapper)
        return self._video
