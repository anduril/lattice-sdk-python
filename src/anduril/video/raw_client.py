# This file was auto-generated from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.conflict_error import ConflictError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .errors.not_found_error import NotFoundError
from .errors.service_unavailable_error import ServiceUnavailableError
from .errors.too_many_requests_error import TooManyRequestsError
from .errors.unauthorized_error import UnauthorizedError
from .types.create_egress_stream_response import CreateEgressStreamResponse
from .types.create_ingress_stream_response import CreateIngressStreamResponse
from .types.delete_egress_stream_response import DeleteEgressStreamResponse
from .types.delete_ingress_stream_response import DeleteIngressStreamResponse
from .types.get_egress_stream_response import GetEgressStreamResponse
from .types.get_ingress_stream_response import GetIngressStreamResponse
from .types.google_rpc_status import GoogleRpcStatus
from .types.list_egress_streams_response import ListEgressStreamsResponse
from .types.list_ingress_streams_response import ListIngressStreamsResponse
from .types.mpeg_ts_settings import MpegTsSettings
from .types.rtsp_settings import RtspSettings
from .types.srt_settings import SrtSettings
from pydantic import ValidationError

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class RawVideoClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_egress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListEgressStreamsResponse]:
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
        HttpResponse[ListEgressStreamsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/video/egress_streams",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEgressStreamsResponse,
                    parse_obj_as(
                        type_=ListEgressStreamsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_egress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateEgressStreamResponse]:
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
        HttpResponse[CreateEgressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/video/egress_streams",
            method="POST",
            json={
                "ingressId": ingress_id,
                "rtsp": convert_and_respect_annotation_metadata(
                    object_=rtsp, annotation=RtspSettings, direction="write"
                ),
                "srt": convert_and_respect_annotation_metadata(object_=srt, annotation=SrtSettings, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateEgressStreamResponse,
                    parse_obj_as(
                        type_=CreateEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEgressStreamResponse]:
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
        HttpResponse[GetEgressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/video/egress_streams/{encode_path_param(egress_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEgressStreamResponse,
                    parse_obj_as(
                        type_=GetEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteEgressStreamResponse]:
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
        HttpResponse[DeleteEgressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/video/egress_streams/{encode_path_param(egress_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteEgressStreamResponse,
                    parse_obj_as(
                        type_=DeleteEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_ingress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListIngressStreamsResponse]:
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
        HttpResponse[ListIngressStreamsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/video/ingress_streams",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIngressStreamsResponse,
                    parse_obj_as(
                        type_=ListIngressStreamsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_ingress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        mpeg_ts: typing.Optional[MpegTsSettings] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateIngressStreamResponse]:
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
        HttpResponse[CreateIngressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/video/ingress_streams",
            method="POST",
            json={
                "ingressId": ingress_id,
                "title": title,
                "mpegTs": mpeg_ts,
                "rtsp": convert_and_respect_annotation_metadata(
                    object_=rtsp, annotation=RtspSettings, direction="write"
                ),
                "srt": convert_and_respect_annotation_metadata(object_=srt, annotation=SrtSettings, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateIngressStreamResponse,
                    parse_obj_as(
                        type_=CreateIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetIngressStreamResponse]:
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
        HttpResponse[GetIngressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/video/ingress_streams/{encode_path_param(ingress_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIngressStreamResponse,
                    parse_obj_as(
                        type_=GetIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteIngressStreamResponse]:
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
        HttpResponse[DeleteIngressStreamResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/video/ingress_streams/{encode_path_param(ingress_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteIngressStreamResponse,
                    parse_obj_as(
                        type_=DeleteIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawVideoClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_egress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListEgressStreamsResponse]:
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
        AsyncHttpResponse[ListEgressStreamsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/video/egress_streams",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListEgressStreamsResponse,
                    parse_obj_as(
                        type_=ListEgressStreamsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_egress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateEgressStreamResponse]:
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
        AsyncHttpResponse[CreateEgressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/video/egress_streams",
            method="POST",
            json={
                "ingressId": ingress_id,
                "rtsp": convert_and_respect_annotation_metadata(
                    object_=rtsp, annotation=RtspSettings, direction="write"
                ),
                "srt": convert_and_respect_annotation_metadata(object_=srt, annotation=SrtSettings, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateEgressStreamResponse,
                    parse_obj_as(
                        type_=CreateEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEgressStreamResponse]:
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
        AsyncHttpResponse[GetEgressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/video/egress_streams/{encode_path_param(egress_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEgressStreamResponse,
                    parse_obj_as(
                        type_=GetEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_egress_stream(
        self, egress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteEgressStreamResponse]:
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
        AsyncHttpResponse[DeleteEgressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/video/egress_streams/{encode_path_param(egress_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteEgressStreamResponse,
                    parse_obj_as(
                        type_=DeleteEgressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_ingress_streams(
        self,
        *,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListIngressStreamsResponse]:
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
        AsyncHttpResponse[ListIngressStreamsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/video/ingress_streams",
            method="GET",
            params={
                "pageSize": page_size,
                "pageToken": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListIngressStreamsResponse,
                    parse_obj_as(
                        type_=ListIngressStreamsResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_ingress_stream(
        self,
        *,
        ingress_id: typing.Optional[str] = OMIT,
        title: typing.Optional[str] = OMIT,
        mpeg_ts: typing.Optional[MpegTsSettings] = OMIT,
        rtsp: typing.Optional[RtspSettings] = OMIT,
        srt: typing.Optional[SrtSettings] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateIngressStreamResponse]:
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
        AsyncHttpResponse[CreateIngressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/video/ingress_streams",
            method="POST",
            json={
                "ingressId": ingress_id,
                "title": title,
                "mpegTs": mpeg_ts,
                "rtsp": convert_and_respect_annotation_metadata(
                    object_=rtsp, annotation=RtspSettings, direction="write"
                ),
                "srt": convert_and_respect_annotation_metadata(object_=srt, annotation=SrtSettings, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateIngressStreamResponse,
                    parse_obj_as(
                        type_=CreateIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetIngressStreamResponse]:
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
        AsyncHttpResponse[GetIngressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/video/ingress_streams/{encode_path_param(ingress_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetIngressStreamResponse,
                    parse_obj_as(
                        type_=GetIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_ingress_stream(
        self, ingress_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteIngressStreamResponse]:
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
        AsyncHttpResponse[DeleteIngressStreamResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/video/ingress_streams/{encode_path_param(ingress_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteIngressStreamResponse,
                    parse_obj_as(
                        type_=DeleteIngressStreamResponse,  # type: ignore
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        GoogleRpcStatus,
                        parse_obj_as(
                            type_=GoogleRpcStatus,  # type: ignore
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
