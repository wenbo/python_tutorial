<a href="https://docs.python.org/2/library/pdb.html">https://docs.python.org/2/library/pdb.html</a>

## The typical usage to break into the debugger from a running program is to insert

# import pdb; pdb.set_trace()
at the location you want to break into the debugger. You can then step through the code following this statement, and continue running without the debugger using the c command.

# pdb.set_trace()
Enter the debugger at the calling stack frame. This is useful to hard-code a breakpoint at a given point in a program, even if the code is not otherwise being debugged (e.g. when an assertion fails).

### Debugger Commands
The debugger recognizes the following commands. Most commands can be abbreviated to one or two letters; e.g. h(elp) means that either h or help can be used to enter the help command (but not he or hel, nor H or Help or HELP). Arguments to commands must be separated by whitespace (spaces or tabs). Optional arguments are enclosed in square brackets ([]) in the command syntax; the square brackets must not be typed. Alternatives in the command syntax are separated by a vertical bar (|).

Entering a blank line repeats the last command entered. Exception: if the last command was a list command, the next 11 lines are listed.

# h(elp) [command]
Without argument, print the list of available commands. With a command as argument, print help about that command.
