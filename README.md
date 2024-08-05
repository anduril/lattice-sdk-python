# anduril-sdk-python

## Quick Start

```bash
mkdir cmd
touch main.py
python3 -m venv .venv
pip3 install git+https://{USER}:{GH_KEY}@github.com/anduril/anduril-python.git@main -U
```

main.py

```python
from anduril.entitymanager.v1 import Entity, PublishEntitiesRequest, EntityManagerApiStub

from grpclib.client import Channel

def main():
    entity = Entity()
    entity.entity_id = "abasd"
    channel = Channel(host="127.0.0.1", port=443)
    service = EntityManagerApiStub(channel)
    response = service.publish_entities(PublishEntitiesRequest(entity = entity))
    print(response)
    # don't forget to close the channel when done!
    channel.close()

if __name__ == "__main__":
    main()
```
