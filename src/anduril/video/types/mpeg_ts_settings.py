# This file was auto-generated from our API Definition.

import typing

MpegTsSettings = typing.Dict[str, typing.Any]
"""
Settings for MPEG-TS ingress. Empty by default, the service allocates a UDP port
 from a service-wide pool and returns the push URL in CreateIngressStreamResponse.

 MPEG-TS ingress may be disabled per deployment. When it is disabled, a
 CreateIngressStream request that selects mpeg_ts is rejected with a gRPC error.
"""
