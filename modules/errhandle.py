def handler(e):
    print()
    errname = e.__class__.__name__
    print("[ERROR] "+errname)
    if errname == "EOFError":
        print("[INFO] This error may cause by a Ctrl+D typing. Please use `:q` command to exit.\n[INFO] If you received EOFError with Ctrl+D, this is not a bug.")
        return
    elif errname == "JustForTestingError":
        print("[INFO] You toggled an error for deployer. If you toggled it by using `:e` command, this is not a bug.")
    #elif errname == ""
    print("[ERROR] If this is a bug, please report this error to https://github.com/Emojigit/sequences/issues/new with what did you do before this error.")
    return
