# Sequences
This is an python app with sequences calcuate.
## Command line
### Commands
All commands have a `:` prefix.
 - `:h` Show the help
 - `:l` Show licensing details
 - `:s` Settings with 1-2 arguments:
   - `help` List all changable Settings
   - `rl <limit>`  Set recursion limit
 - `:q` Quit
### Sequences
Use `:h` command to get a list of sequences. Use `SEQUENCE_NAME n` to get the *n*th of the sequence.

## Keyboard Shortcut
 - `^C KeyboardInterrupt`: Interrupt
 - `^D EOFError`: Quit (Not working on Windows)
 - `Up key`: Last execution (Not working on Linux, tested on Windows Anaconda)

## API
### Sequences API
all sequences are under `modules.seq`
### Exceptions
#### `modules.seq.SequenceInterrupt(reason=None)`
Interrupt the current sequence calcuate (toggle by the sequence calcuater)
#### `__main__.JustForTestingError()`
Test the resopnse when an error happend (toggle by `:e` command)
