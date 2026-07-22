# Changelog

## [4.23.0] - 2026-07-22

## [4.22.0] - 2026-07-21
### Added
- **`kinematics`** — new optional field on entity publish methods and the `Entity` model for higher-granularity kinematics data, preferred for Track Entities and mutually exclusive with `location`/`location_uncertainty`.
- **`Kinematics`, `KinematicsGeodetic`, `KinematicsGeocentric`** — new types for representing entity kinematics in geodetic (WGS84/ENU) and geocentric (ECEF) reference frames.
- **`Altitude`** — new altitude type with reference variants (`AltitudeAboveGroundLevel`, `AltitudeAboveWgs84Ellipsoid`, `AltitudeAboveSeaFloor`, and others) plus `AltitudeProvenance` and `AltitudeProvenanceSourceType`.
- **`LocationGeodetic`, `LocationGeocentricEcef`** — new location measurement types for WGS84 and ECEF frames.
- **`Vec3`, `TMat3`** — new math primitive types for 3D vectors and symmetric covariance matrices.

## [4.21.0] - 2026-07-16

