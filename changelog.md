# Changelog

## [4.30.0] - 2026-09-03

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

