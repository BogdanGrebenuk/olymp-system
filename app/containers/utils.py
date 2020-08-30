from dependency_injector import containers


def combine_containers(*provided_containers):
    container = containers.DynamicContainer()

    for provided_container in provided_containers:
        populate_container(container, provided_container)

    return container


def populate_container(container, provided_container):
    for key, provider in provided_container.providers.items():
        setattr(container, key, provider)
