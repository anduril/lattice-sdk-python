# Changelog

## [5.0.0] - 2026-09-03

### Breaking Changes
* client.video.video — the nested video subclient has been removed; call stream methods directly on client.video (e.g. use client.video.list_egress_streams() instead of client.video.video.list_egress_streams()).
* RawVideoClient and AsyncRawVideoClient — removed along with all raw egress/ingress stream methods; migrate to the higher-level methods on the sync and async video clients.

### Added
* Video stream operations — list, create, get, and delete methods for both egress and ingress streams are now available on the sync and async video clients.
* Typed error responses — video stream methods now raise specific errors such as BadRequestError, ConflictError, TooManyRequestsError, and ServiceUnavailableError, carrying GoogleRpcStatus bodies.
* PlatformSubcomponents — new top-level exported type describing a platform and its positionally-related subcomponents, available as an optional platformSubcomponents field on GroupDetails.
* requireAcknowledgement — new optional field on DeliveryConstraints requiring the agent to confirm receipt before a request is marked delivered.
* DELIVERY_ERROR_CODE_NOT_ACKNOWLEDGED — new value in the DeliveryErrorCode union returned when acknowledgement is required but not received.

### Changed
MPEG-TS ingress docs — clarified that it is supported only at the edge in closed networks and may be disabled in cloud deployments.

## [4.30.0] - 2026-09-03

**Added**

- client.video — new namespace with VideoClient and AsyncVideoClient for managing Lattice live video streams.
- Ingress and egress stream operations — list, create, get, and delete methods for both ingress and egress streams.
- RawVideoClient and AsyncRawVideoClient — low-level clients offering typed HTTP responses for the video streaming API.
- Stream transport settings — support for RTSP, SRT, and MPEG-TS via new stream, transport, and settings models (e.g. IngressStream, EgressStream, RtspSettings, SrtSettings, MpegTsSettings).
- Video error and response types — structured errors (BadRequestError, NotFoundError, ConflictError, ServiceUnavailableError, GoogleRpcStatus, GoogleProtobufAny) and request/response models for all stream operations.

## [4.29.1] - 2026-08-21

## [4.29.0] - 2026-08-20

## [4.28.0] - 2026-08-18

## [4.27.0] - 2026-08-12

## [4.26.0] - 2026-08-11

## [4.25.0] - 2026-08-03
### Added
- **`quote_path_param`** — new helper in `core.jsonable_encoder` that percent-encodes path parameter values so values containing `/` or `..` cannot change which endpoint a request resolves to.

## [4.24.0] - 2026-07-29

## [4.23.0] - 2026-07-22

## [4.22.0] - 2026-07-21
### Added
- **`kinematics`** — new optional field on entity publish methods and the `Entity` model for higher-granularity kinematics data, preferred for Track Entities and mutually exclusive with `location`/`location_uncertainty`.
- **`Kinematics`, `KinematicsGeodetic`, `KinematicsGeocentric`** — new types for representing entity kinematics in geodetic (WGS84/ENU) and geocentric (ECEF) reference frames.
- **`Altitude`** — new altitude type with reference variants (`AltitudeAboveGroundLevel`, `AltitudeAboveWgs84Ellipsoid`, `AltitudeAboveSeaFloor`, and others) plus `AltitudeProvenance` and `AltitudeProvenanceSourceType`.
- **`LocationGeodetic`, `LocationGeocentricEcef`** — new location measurement types for WGS84 and ECEF frames.
- **`Vec3`, `TMat3`** — new math primitive types for 3D vectors and symmetric covariance matrices.

## [4.21.0] - 2026-07-16

