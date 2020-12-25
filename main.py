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
import sys, traceback, tempfile, os
try:
    from modules import seq, cpr_note, errhandle
except ImportError:
    print("Modules not found, did you forgot to put it into the same folder as this program?")
    sys.exit(128)
exit = sys.exit
cpr_note.show()
seqs = seq.seqs
debug = False

class JustForTestingError(Exception):
    pass

def screen_clear():
    # for mac and linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # for windows platfrom
        _ = os.system('cls')

print("Sequence Version v2.0.0")
print("Type \":l\", \":h\" for more information.")
while True:
    try:
        command = str(input("> ")).split(" ",1)
        if debug == True:
            print("[DEBUG] Issued command: "+str(command))
        if command == [] or command == [""]:
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
            print("e == Raise an error (Dev tool)")
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
                print("debug: Extra debug informations")
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
            elif args[0] == "debug":
                if args[1] == "True" or args[1] == "true" or args[1] == "1":
                    debug = True
                elif args[1] == "False" or args[1] == "false" or args[1] == "0":
                    debug = False
                else:
                    print("Invalid bollen")
            else:
                print("Unknown setting")
        elif command[0] == ":e":
            raise JustForTestingError()
        elif command[0] == ":c":
            screen_clear()
        elif command[0].startswith(":"):
            print("No such command")
        else:
            try:
                sf = seqs[command[0].upper()]
                n = int(command[1])
                if n <= 0:
                    raise ValueError
                res = sf(n)
                if debug == True:
                    print("[DEBUG] Feedback type: "+str(type(res)))
                print("Result: "+str(res))
            except seq.SequenceInterrupt:
                continue
            except IndexError:
                print("Missing Arg: term(int)")
            except KeyError:
                print("No such sequence")
            except ValueError:
                print("Please enter a possitive int")
    except KeyboardInterrupt:
        print()
        pass
    # except EOFError:
    #     print()
    #     exit(1)
    except SystemExit:
        print()
        print("Bye")
        sys.exit()
    except Exception as e:
        #info = sys.exc_info()
        #tmpdir = tempfile.mkdtemp()
        #err_path = str(os.getpid())+"_sequences_err.txt"
        #err_file = open(err_path,"w+")
        errhandle.handler(e)
        #err_file.write(traceback.print_tb(sys.exc_info()[2]))
        #print("The error messages have been written into \""+err_path+"\"")
        raise
