# This file was auto-generated from our API Definition.

import typing

from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.request_options import RequestOptions
from ..types.create_egress_stream_response import CreateEgressStreamResponse
from ..types.create_ingress_stream_response import CreateIngressStreamResponse
from ..types.delete_egress_stream_response import DeleteEgressStreamResponse
from ..types.delete_ingress_stream_response import DeleteIngressStreamResponse
from ..types.get_egress_stream_response import GetEgressStreamResponse
from ..types.get_ingress_stream_response import GetIngressStreamResponse
from ..types.list_egress_streams_response import ListEgressStreamsResponse
from ..types.list_ingress_streams_response import ListIngressStreamsResponse
from ..types.mpeg_ts_settings import MpegTsSettings
from ..types.rtsp_settings import RtspSettings
from ..types.srt_settings import SrtSettings
from .raw_client import AsyncRawVideoClient, RawVideoClient

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class VideoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVideoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVideoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVideoClient
        """
        return self._raw_client

    def list_egress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEgressStreamsResponse:
        """
        Returns a list of active egress stream objects.
         Results are ordered by egress stream create time. If the
         egress backend is unreachable, the listed streams might be stale or degraded.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Desired number of egress streams per page. Defaults to 50 if left blank,
             and capped at 100. The response may contain fewer than max page size.

        page_token : typing.Optional[str]
            To retrieve the next page, pass the `next_page_token` from the previous
             response. Leave empty for the first page.

             Keep the rest of the request identical between pages, otherwise the
             server may reject it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEgressStreamsResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.list_egress_streams()
        """
        _response = self._raw_client.list_egress_streams(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_egress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEgressStreamResponse:
        """
        Creates an egress stream that publishes a live stream to a downstream consumer.
         A stream in `STREAM_STATUS_UNAVAILABLE` is rejected as not-live.

        Parameters
        ----------
        ingress_id : typing.Optional[str]
            Identifier of the live ingress stream to re-publish as an egress stream.

        rtsp : typing.Optional[RtspSettings]

        srt : typing.Optional[SrtSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEgressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.create_egress_stream()
        """
        _response = self._raw_client.create_egress_stream(
            ingress_id=ingress_id, rtsp=rtsp, srt=srt, request_options=request_options
        )
        return _response.data

    def get_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEgressStreamResponse:
        """
        Retrieves an egress stream object and its associated metadata.

        Parameters
        ----------
        egress_id : str
            Identifier of the egress stream to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEgressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.get_egress_stream(
            egress_id="egressId",
        )
        """
        _response = self._raw_client.get_egress_stream(egress_id, request_options=request_options)
        return _response.data

    def delete_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEgressStreamResponse:
        """
        Deletes the egress stream for a live stream. Returns `NOT_FOUND` if no matching active
         egress stream exists.

        Parameters
        ----------
        egress_id : str
            Identifier of the egress stream to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteEgressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.delete_egress_stream(
            egress_id="egressId",
        )
        """
        _response = self._raw_client.delete_egress_stream(egress_id, request_options=request_options)
        return _response.data

    def list_ingress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIngressStreamsResponse:
        """
        Returns a list of top level ingress stream objects, including ingress streams and internal
         Anduril streams. Will only return active streams.
         Results are ordered by ingress stream create time.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Desired number of ingress streams per page. Defaults to 50 if left blank,
             and capped at 100. The response may contain fewer than requested.

        page_token : typing.Optional[str]
            To retrieve the next page, pass the `next_page_token` from the previous
             response. Leave empty for the first page.

             Keep the rest of the request identical between pages, otherwise the
             server may reject it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIngressStreamsResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.list_ingress_streams()
        """
        _response = self._raw_client.list_ingress_streams(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    def create_ingress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        mpeg_ts: typing.Optional[MpegTsSettings] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateIngressStreamResponse:
        """
        Creates a video ingress stream, returning metadata that you can use to stream live video to
         Lattice. Exactly one of `rtsp` or `srt` must be set on the request.

        Parameters
        ----------
        ingress_id : typing.Optional[str]
            Caller-supplied identifier for the new stream. If omitted, the service generates a GUID.
             If supplied, a consistent and recognizable pattern is recommended. A common convention
             is a group prefix (organization, platform, or asset) followed by a specific identifier
             using underscore or dot as a separator, for example, `drone_1`, `vessel_2`, or
             `teamalpha.drone1`.

             When supplied, an ingress_id must be between 4 and 36 characters long and use only
             printable ASCII characters with no spaces; the 36-character ceiling leaves room for a
             full GUID. A value outside that length range, or one containing spaces, control
             characters, or non-ASCII characters, is rejected, as is an ingress_id that another
             ingress stream is already using.

        title : typing.Optional[str]
            Human-readable title for the stream. A title is required: surrounding whitespace is
             trimmed before it is stored, and what remains must be non-empty, valid UTF-8, and no
             longer than 64 characters. Otherwise the request is rejected.

        mpeg_ts : typing.Optional[MpegTsSettings]
            Receive an MPEG-TS push from the producer. The service allocates a UDP port and
             returns the URL the producer must push to in CreateIngressStreamResponse.

             MPEG-TS ingress may be disabled per deployment. When it is disabled, a request
             that selects mpeg_ts is rejected with a gRPC error rather than accepted, so
             callers should be prepared to fall back to another protocol.

        rtsp : typing.Optional[RtspSettings]
            Pull from a caller-supplied RTSP URL.

        srt : typing.Optional[SrtSettings]
            Receive an SRT push from the producer. The service returns a URL and session_id
             in CreateIngressStreamResponse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateIngressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.create_ingress_stream()
        """
        _response = self._raw_client.create_ingress_stream(
            ingress_id=ingress_id, title=title, mpeg_ts=mpeg_ts, rtsp=rtsp, srt=srt, request_options=request_options
        )
        return _response.data

    def get_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetIngressStreamResponse:
        """
        Retrieves a top level ingress stream object and its associated metadata. This includes
         ingress streams and internal Anduril streams.

        Parameters
        ----------
        ingress_id : str
            Identifier of the ingress stream to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIngressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.get_ingress_stream(
            ingress_id="ingressId",
        )
        """
        _response = self._raw_client.get_ingress_stream(ingress_id, request_options=request_options)
        return _response.data

    def delete_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteIngressStreamResponse:
        """
        Deletes a video ingress stream and transitions the stream to `STREAM_STATUS_ARCHIVED`.
         Any egress streams consuming this stream will be stopped automatically.

        Parameters
        ----------
        ingress_id : str
            Identifier of the ingress stream to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteIngressStreamResponse
            OK

        Examples
        --------
        from anduril import Lattice

        client = Lattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )
        client.video.video.delete_ingress_stream(
            ingress_id="ingressId",
        )
        """
        _response = self._raw_client.delete_ingress_stream(ingress_id, request_options=request_options)
        return _response.data


class AsyncVideoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVideoClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVideoClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVideoClient
        """
        return self._raw_client

    async def list_egress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListEgressStreamsResponse:
        """
        Returns a list of active egress stream objects.
         Results are ordered by egress stream create time. If the
         egress backend is unreachable, the listed streams might be stale or degraded.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Desired number of egress streams per page. Defaults to 50 if left blank,
             and capped at 100. The response may contain fewer than max page size.

        page_token : typing.Optional[str]
            To retrieve the next page, pass the `next_page_token` from the previous
             response. Leave empty for the first page.

             Keep the rest of the request identical between pages, otherwise the
             server may reject it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListEgressStreamsResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.list_egress_streams()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_egress_streams(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_egress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateEgressStreamResponse:
        """
        Creates an egress stream that publishes a live stream to a downstream consumer.
         A stream in `STREAM_STATUS_UNAVAILABLE` is rejected as not-live.

        Parameters
        ----------
        ingress_id : typing.Optional[str]
            Identifier of the live ingress stream to re-publish as an egress stream.

        rtsp : typing.Optional[RtspSettings]

        srt : typing.Optional[SrtSettings]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateEgressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.create_egress_stream()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_egress_stream(
            ingress_id=ingress_id, rtsp=rtsp, srt=srt, request_options=request_options
        )
        return _response.data

    async def get_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetEgressStreamResponse:
        """
        Retrieves an egress stream object and its associated metadata.

        Parameters
        ----------
        egress_id : str
            Identifier of the egress stream to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetEgressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.get_egress_stream(
                egress_id="egressId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_egress_stream(egress_id, request_options=request_options)
        return _response.data

    async def delete_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteEgressStreamResponse:
        """
        Deletes the egress stream for a live stream. Returns `NOT_FOUND` if no matching active
         egress stream exists.

        Parameters
        ----------
        egress_id : str
            Identifier of the egress stream to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteEgressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.delete_egress_stream(
                egress_id="egressId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_egress_stream(egress_id, request_options=request_options)
        return _response.data

    async def list_ingress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListIngressStreamsResponse:
        """
        Returns a list of top level ingress stream objects, including ingress streams and internal
         Anduril streams. Will only return active streams.
         Results are ordered by ingress stream create time.

        Parameters
        ----------
        page_size : typing.Optional[int]
            Desired number of ingress streams per page. Defaults to 50 if left blank,
             and capped at 100. The response may contain fewer than requested.

        page_token : typing.Optional[str]
            To retrieve the next page, pass the `next_page_token` from the previous
             response. Leave empty for the first page.

             Keep the rest of the request identical between pages, otherwise the
             server may reject it.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIngressStreamsResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.list_ingress_streams()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ingress_streams(
            page_size=page_size, page_token=page_token, request_options=request_options
        )
        return _response.data

    async def create_ingress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        mpeg_ts: typing.Optional[MpegTsSettings] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateIngressStreamResponse:
        """
        Creates a video ingress stream, returning metadata that you can use to stream live video to
         Lattice. Exactly one of `rtsp` or `srt` must be set on the request.

        Parameters
        ----------
        ingress_id : typing.Optional[str]
            Caller-supplied identifier for the new stream. If omitted, the service generates a GUID.
             If supplied, a consistent and recognizable pattern is recommended. A common convention
             is a group prefix (organization, platform, or asset) followed by a specific identifier
             using underscore or dot as a separator, for example, `drone_1`, `vessel_2`, or
             `teamalpha.drone1`.

             When supplied, an ingress_id must be between 4 and 36 characters long and use only
             printable ASCII characters with no spaces; the 36-character ceiling leaves room for a
             full GUID. A value outside that length range, or one containing spaces, control
             characters, or non-ASCII characters, is rejected, as is an ingress_id that another
             ingress stream is already using.

        title : typing.Optional[str]
            Human-readable title for the stream. A title is required: surrounding whitespace is
             trimmed before it is stored, and what remains must be non-empty, valid UTF-8, and no
             longer than 64 characters. Otherwise the request is rejected.

        mpeg_ts : typing.Optional[MpegTsSettings]
            Receive an MPEG-TS push from the producer. The service allocates a UDP port and
             returns the URL the producer must push to in CreateIngressStreamResponse.

             MPEG-TS ingress may be disabled per deployment. When it is disabled, a request
             that selects mpeg_ts is rejected with a gRPC error rather than accepted, so
             callers should be prepared to fall back to another protocol.

        rtsp : typing.Optional[RtspSettings]
            Pull from a caller-supplied RTSP URL.

        srt : typing.Optional[SrtSettings]
            Receive an SRT push from the producer. The service returns a URL and session_id
             in CreateIngressStreamResponse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateIngressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.create_ingress_stream()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_ingress_stream(
            ingress_id=ingress_id, title=title, mpeg_ts=mpeg_ts, rtsp=rtsp, srt=srt, request_options=request_options
        )
        return _response.data

    async def get_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetIngressStreamResponse:
        """
        Retrieves a top level ingress stream object and its associated metadata. This includes
         ingress streams and internal Anduril streams.

        Parameters
        ----------
        ingress_id : str
            Identifier of the ingress stream to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetIngressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.get_ingress_stream(
                ingress_id="ingressId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_ingress_stream(ingress_id, request_options=request_options)
        return _response.data

    async def delete_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteIngressStreamResponse:
        """
        Deletes a video ingress stream and transitions the stream to `STREAM_STATUS_ARCHIVED`.
         Any egress streams consuming this stream will be stopped automatically.

        Parameters
        ----------
        ingress_id : str
            Identifier of the ingress stream to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteIngressStreamResponse
            OK

        Examples
        --------
        import asyncio

        from anduril import AsyncLattice

        client = AsyncLattice(
            client_id="YOUR_CLIENT_ID",
            client_secret="YOUR_CLIENT_SECRET",
        )


        async def main() -> None:
            await client.video.video.delete_ingress_stream(
                ingress_id="ingressId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ingress_stream(ingress_id, request_options=request_options)
        return _response.data
