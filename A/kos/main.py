import os
import A.kos.baces.files as files
import A.kos.baces.dirs as dirs
import A.kos.baces.kos as kos


def parse_command(cmd: str):
    """Parse a command and locate a type marker among tokens (@, %, :, !).

    Accepts both forms:
      file -make @ path/to/file
      dir -list ! .

    Returns (base, action, type, value)
    """
    markers = {"@", "%", ":", "!"}
    parts = cmd.strip().split()
    if not parts:
        return None, None, None, None
    base = parts[0]
    action = parts[1] if len(parts) > 1 else None

    type_ = None
    value = ""
    # search for a type marker token in the rest
    for i in range(2, len(parts)):
        if parts[i] in markers:
            type_ = parts[i]
            # value is everything after the marker
            value = " ".join(parts[i+1:])
            break
    else:
        # no explicit marker found; treat everything after action as value
        if len(parts) > 2:
            value = " ".join(parts[2:])

    return base, action, type_, value


def main():
    # simple disk map: letter -> path
    disks = {
        "A": os.getcwd(),
        "B": "/tmp/HC-KOS-B",
        "C": "/tmp/HC-KOS-C",
    }
    # ensure disk paths exist
    for p in disks.values():
        try:
            os.makedirs(p, exist_ok=True)
        except Exception:
            pass

    current_disk = "A"
    cwd = disks[current_disk]
    # ensure working directory matches
    try:
        os.chdir(cwd)
    except Exception:
        pass
    while True:
        try:
            # show disk letter, then path (short)
            short = os.path.relpath(cwd, start=disks[current_disk]) if cwd.startswith(disks[current_disk]) else cwd
            prompt = f"HC-KOS [{current_disk}] : {short} $ "
            cmd = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not cmd:
            continue

        base, action, type_, value = parse_command(cmd)
        if base is None:
            continue
        base = base.lower()

        # allow quick clear by typing 'clear'
        if base == "clear":
            os.system("clear")
            continue

        # convenience shortcuts
        if base in ("exit", "quit", "q"):
            break

        # disk management
        if base == "disk":
            # actions: -list !  -> list disks
            #          -use @ <LETTER> -> switch to disk
            #          -mount @ <LETTER> <path> -> set mapping
            action = (action or "").strip()
            if action in ("-list", "-ls"):
                for k, v in disks.items():
                    print(f"{k}: {v}")
            elif action == "-use" and (type_ == "@"):
                letter = (value or "").strip().upper()
                if letter in disks:
                    current_disk = letter
                    cwd = disks[current_disk]
                    try:
                        os.chdir(cwd)
                    except Exception as e:
                        print(f"Could not change dir: {e}")
                else:
                    print(f"Unknown disk: {letter}")
            elif action == "-mount" and (type_ == "@"):
                parts = (value or "").split(None, 1)
                if len(parts) == 2:
                    letter = parts[0].upper()
                    path = parts[1]
                    disks[letter] = path
                    try:
                        os.makedirs(path, exist_ok=True)
                    except Exception:
                        pass
                    print(f"Mounted {letter} -> {path}")
                else:
                    print("Usage: disk -mount @ <LETTER> <path>")
            else:
                print("Unknown disk command. Use 'disk -list !' or 'disk -use @ <LETTER>'")
            continue

        # file command
        if base == "file":
            files.run(action or "", type_ or "", value or "")
            continue

        # dir command
        if base == "dir":
            # default value for list is current directory
            if (action == "-list" or action == "-ls") and (type_ == "!" or type_ is None) and not value:
                value = "."
            dirs.run(action or "", type_ or "", value or "")
            continue

        # kos command
        if base == "kos":
            if action in ("-quit", "-exit"):
                break
            # handle clear shortcut at kos level
            if action in ("-clear", "clear"):
                os.system("clear")
                continue
            kos.run(action or "", type_ or "", value or "")
            continue

        print(f"Unknown base: {base}")


if __name__ == "__main__":
    main()
