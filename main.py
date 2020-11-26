#!/usr/bin/python3
"""
This file is a part of sequences.
Copyright (C) 2020 Cato Yiu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from modules import seq
__import__('modules', globals(), locals(), ['cpr_note'], 0).cpr_note.show()
seqs = seq.seqs

print("Sequence Version alpha 1")
print("Type \":l\", \":h\" for more information.")
while True:
    try:
        command = str(input("> ")).split(" ",1)
        if command == []:
            continue
        elif command[0] == ":h":
            print("List of sequences:")
            for s in seqs:
                print(s)
            print("---------------------")
            print("List of commands:")
            print("h == Get this help")
            print("l == see license details")
            print("q == Quit")
            print("Note: all commands have a `:` prefix")
            print("---------------------")
            print("Keyboard Shortcuts:")
            print("^C: Interrupt")
            print("^D: Quit")
        elif command[0] == ":l":
            print("License under GNU GPLv3, see LICENSE.txt and COPYING.txt")
        elif command[0] == ":q":
            exit()
        elif command[0].startswith(":"):
            print("No such command")
        else:
            try:
                sf = seqs[command[0]]
                n = int(command[1])
                if n <= 0:
                    raise ValueError
                print("Result: "+str(sf(n)))
            except IndexError:
                print("Missing Arg: term(int)")
            except KeyError:
                print("No such sequence")
            except ValueError:
                print("Please enter a possitive int")
    except KeyboardInterrupt:
        print()
        pass
    except EOFError:
        print()
        exit(1)