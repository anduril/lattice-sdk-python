# Anduril SDK Python

The official [Anduril](https://www.anduril.com/) client library.

## Requirements

Python 3

## Installation

### Authentication

To authenticate with the Github package repository, you will need to generate a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic). This should have at least `read:packages` scope. Please keep the token safe for the next stage of the setup procedure.

### Pip

Install the SDK with Pip. 

```
pip install git+https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/anduril/anduril-python.git -U
```

**Note:** To use gRPC's in Python, you must install the
[`grpclib`](https://grpclib.readthedocs.io/en/latest/index.html) dependency

```
pip install "grpclib[protobuf]"
```

You'll also need
[`certifi`](https://grpclib.readthedocs.io/en/latest/client.html#secure-channels)
to setup a secure connection to gRPC server:

```
pip install certifi
```
## Usage

main.py

```python
from anduril.entitymanager.v1 import EntityManagerApiStub, GetEntityRequest
from grpclib.client import Channel
import asyncio

metadata = {
    'authorization': 'Bearer <YOUR BEARER TOKEN>'
}

async def get_entity(entity_id):
    # open secure channel
    channel = Channel(host="HOSTNAME", port=443, ssl=True)

    # create service instance
    entity_manager_stub = EntityManagerApiStub(channel)

    # make request with auth header
    response = await entity_manager_stub.get_entity(GetEntityRequest(entity_id = entity_id), metadata=metadata)

    channel.close() # don't forget to close the channel!
    return response

if __name__ == "__main__":
    print(asyncio.run(get_entity("<ENTITY ID>")))
```

## Support

For support with this library please [file an issue](https://github.com/anduril/anduril-python/issues/new) or reach out to your Anduril representative. 



