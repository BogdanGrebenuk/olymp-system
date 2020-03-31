from commandbus.bus import Bus


_REGISTRY = {
    'default': Bus('default')
}


def get_bus(tag):
    bus_ = _REGISTRY.get(tag)
    if bus_ is None:
        bus_ = Bus(tag)
        _REGISTRY[tag] = bus_
    return bus_

