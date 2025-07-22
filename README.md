# Anduril Python Library

![](https://www.anduril.com/lattice-sdk/)

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Fanduril%2Flattice-sdk-python)
[![pypi](https://img.shields.io/pypi/v/anduril-lattice-sdk-test)](https://pypi.python.org/pypi/anduril-lattice-sdk-test)

The Anduril Python library provides convenient access to the Anduril API from Python.

## Documentation

API reference documentation is available [here](https://developer.anduril.com/).

## Requirements

To use the SDK please ensure you have the following installed:

* [Python 3](https://www.python.org/doc/versions)

## Installation

```sh
pip install anduril-lattice-sdk-test
```

## Support

For support with this library please reach out to your Anduril representative.

## Reference

A full reference for this library is available [here](https://github.com/anduril/lattice-sdk-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from anduril import Lattice

client = Lattice(
    token="YOUR_TOKEN",
)
client.entities.long_poll_entity_events(
    session_token="sessionToken",
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from anduril import AsyncLattice

client = AsyncLattice(
    token="YOUR_TOKEN",
)


async def main() -> None:
    await client.entities.long_poll_entity_events(
        session_token="sessionToken",
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from anduril.core.api_error import ApiError

try:
    client.entities.long_poll_entity_events(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Pagination

Paginated requests will return a `SyncPager` or `AsyncPager`, which can be used as generators for the underlying object.

```python
from anduril import Lattice

client = Lattice(
    token="YOUR_TOKEN",
)
response = client.objects.list_objects()
for item in response:
    yield item
# alternatively, you can paginate page-by-page
for page in response.iter_pages():
    yield page
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from anduril import Lattice

client = Lattice(
    ...,
)
response = client.entities.with_raw_response.long_poll_entity_events(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
pager = client.objects.list_objects(...)
print(pager.response.headers)  # access the response headers for the first page
for item in pager:
    print(item)  # access the underlying object(s)
for page in pager.iter_pages():
    print(page.response.headers)  # access the response headers for each page
    for item in page:
        print(item)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.entities.long_poll_entity_events(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from anduril import Lattice

client = Lattice(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.entities.long_poll_entity_events(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from anduril import Lattice

client = Lattice(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
