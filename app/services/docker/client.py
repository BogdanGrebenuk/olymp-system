from services.docker import client


class Client:

    def __init__(self, client):
        self._client = client

    def build(self, tag, dockerfile, context):
        return self._client.images.build(
            tag=tag,
            rm=True,
            dockerfile=dockerfile,
            path=context
        )

    def run(self, tag, volumes=None):
        if volumes is None:
            volumes = {}
        volumes = {
            host_path: {"bind": container_path, "mode": "rw"}
            for host_path, container_path in volumes.items()
        }
        return self._client.containers.run(
            tag,
            auto_remove=True,
            volumes=volumes
        )

    def remove(self, tag):
        return self._client.images.remove(image=tag, force=True)

    @classmethod
    def from_env(cls):
        return cls(client)
