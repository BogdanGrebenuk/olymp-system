`commandbus` package is just simple implementation of Command Bus 'pattern' (inspired by [tactician]) 

**Basic usage**

For using command bus just create an instance of `Bus`

```
>>> bus = Bus(middlewares=[...])
>>> command = Command(...)
>>> await bus.execute(command)
```

All middlewares must support `Middleware` interface (commandbus.middlewares.Middleware). 
The last middleware usually is a `resolver` that directs command to appropriate command handlers.

**Usage in project**

Custom `Resolver` that used in `olymp` project tightly integrated with `dependency_injector` module,
so command handlers support DI.

If you want to get an instance of bus, you can:
1. Obtain it from application_container:

    `>>> bus = application_container.bus()`

    Note: if you want to inject bus into your service, follow next example:
    
    ```
    class Container(containers.DeclarativeContainer):
        service = providers.Singleton(
            service,
            bus=application_container.bus
        ) 
  
    ```
2. Obtain it from application instance (for example, in request handler):

    ```
    async def index(request):
        bus = request.app['bus']
    ```

[tactician]: https://tactician.thephpleague.com/