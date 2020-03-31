class CommandHandler:
    """Base command handler class

    Used by resolver for detecting command handlers.
    Inherit your command handler class from this class.
    Also be sure handler has `{CommandClassName}Handler` name format

    The only way to obtain bus in handler - get it from attr `bus`

    """

    BUS_NAME = 'default'

    def __init__(self):
        from commandbus import get_bus
        # Import is here because of solving cyclic imports.
        # Command handlers may need bus instance but it can't be retrieved
        # in module-level due to resolving this command handlers while instantiating package
        self.bus = get_bus(self.BUS_NAME)

    @classmethod
    def supports(cls, bus_tag):
        return bus_tag == cls.BUS_NAME
