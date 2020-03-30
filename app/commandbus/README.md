`commandbus` package is a naive attempt to implement `tactician`-like CommandBus bundle.

Creating a bus is a simple - just create an instance of `commandbus.bus.Bus` class:
 
 `>>> bus = Bus()`
 
 Also you can pass to constructor 
custom `resolver` object for filling `command - handler` mapping dict and pass this mapping dict too:

`>>> bus = Bus(resolver=CustomResolver(), command_map={...})`

`resolver` object has to implement `resolve` method with one argument (dict)
that **must be changed**. 

For creating new `command` class be sure to inherit command class from `commandbus.base_command.Command` class. 
You can store it anywhere you want, just be sure your module is already run at the resolving moment.
 
Rules for creating new `commandhandler` class are same: inherit your class from 
`commandbus.command_handlers.base_command_handler` and be sure module is already run at the moment of resolving.    

TODO: 
- add middleware chain;
- detect **all** subclasses of base classes, not only first 
direct descendant.