# Changelog

## [5.0.0] - 2026-09-04

### Breaking Changes
- **`VideoClient` / `AsyncVideoClient`** — the nested `client.video.video.*` namespace was removed; call stream methods directly on `client.video` (e.g. `client.video.list_egress_streams()`).
- **`RawVideoClient` / `AsyncRawVideoClient`** — removed entirely; migrate to the standard video client methods that return parsed responses directly.
- **Video types relocated** — response and stream types such as `CreateEgressStreamResponse`, `CreateIngressStreamResponse`, `IngressStream`, `EgressStream`, and `IngressStreamStatus` moved from `anduril.video.types` to the top-level `anduril.types`; update imports accordingly.

### Added
- **Video streaming types** — `IngressStream`, `EgressStream`, `RtspSettings`, `SrtSettings`, `MpegTsSettings`/`MpegTsIngress`, and their create/get/list/delete response types are now exported from the top-level `anduril` and `anduril.types` namespaces.
- **Video stream methods** — `list`, `create`, `get`, and `delete` operations for both egress and ingress streams (supporting RTSP, SRT, and MPEG-TS settings) are available on the video client.
- **Typed error responses** — video stream operations now return typed errors including `BadRequestError`, `UnauthorizedError`, `NotFoundError`, `ConflictError`, and `InternalServerError`.
- **`PlatformSubcomponents`** — new model describing a platform group composed of subcomponent entities, exposed via the new optional `platformSubcomponents` field on `GroupDetails`.
- **`requireAcknowledgement`** — optional field on `DeliveryConstraints` requiring agent receipt confirmation, plus the new `DELIVERY_ERROR_CODE_NOT_ACKNOWLEDGED` value on `DeliveryErrorCode`.

### Changed
- **`CreateIngressStreamResponse.mpeg_ts`** — documentation clarified that MPEG-TS ingress is supported only at the edge in closed networks and may be disabled in cloud deployments.

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

