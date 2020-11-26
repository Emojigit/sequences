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
from modules import seq, cpr_note
import sys
exit = sys.exit
cpr_note.show()
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
                print(s,end=": ")
                print(seq.helps[s])
            print("---------------------")
            print("List of commands:")
            print("h == Get this help")
            print("l == see license details")
            print("q == Quit")
            print("s == settings (Use `:s help` to get all settings)")
            print("Note: all commands have a `:` prefix")
            print("---------------------")
            print("Keyboard Shortcuts:")
            print("^C: Interrupt")
            print("^D: Quit (Not working on windows)")
        elif command[0] == ":l":
            print("License under GNU GPLv3, see LICENSE.txt and COPYING.txt in the source code")
        elif command[0] == ":q":
            exit()
        elif command[0] == ":s":
            try:
                args = command[1].split(" ",1)
                tmp = args[0]
            except IndexError:
                print("Mssing args, use `:s help` to see settings")
                continue
            if args[0] == "help":
                print("Subcommands of settings:")
                print("rl: Set recursion limit")
                continue
            try:
                tmp = args[1]
            except IndexError:
                print("Mssing args, use `:s help` to see settings")
                continue
            if args[0] == "rl":
                print("WARNING: CHANGE IT MAY CAUSE A STACK OVERFLOW!")
                try:
                    if int(args[1]) < 1000:
                        print("Arg too small!")
                        continue
                    sys.setrecursionlimit(int(args[1]))
                except ValueError:
                    print("Arg not int!")
                except OverflowError:
                    print("Arg too big!")
            else:
                print("Unknown setting")
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
