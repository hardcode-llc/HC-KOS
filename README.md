(The file `/workspaces/HC-KOS/README.md` exists, but is empty)
# HC-KOS — Hard Code LLC

Version: 0.1.0

HC-KOS is a minimal, educational, MS-DOS-like command shell implemented in Python. It was created by Hard Code LLC (HC-LLC) as a small, easily extensible environment for experimentation and learning.

This repository contains a tiny shell with basic `file`, `dir`, `disk`, and `kos` commands. It is not intended to replace a production shell — instead it is a teaching/project scaffold you can extend.

Table of Contents
-----------------
- Features
- Quick start
- Command reference
- Examples
- Internals and design
- Packaging and release notes
- Contributing
- License

Features
--------
- Small, single-file REPL entrypoint (`index.py`) that imports the `A.kos` package.
- Token-based command parser with simple type markers: `@`, `%`, `:`, `!`.
- Basic file and directory operations implemented in `A/kos/baces`.
- Minimal disk mapping (A/B/C by default) so commands can reference logical drives.
- Clear, prompt spacing, and a few convenience shortcuts to feel more shell-like.

Quick start
-----------
Requirements: Python 3.10+ (the code uses standard library only).

Clone and run:

```bash
git clone https://github.com/hardcode-llc/HC-KOS.git
cd HC-KOS
python index.py
```

You should see a prompt similar to:

```
HC-KOS [A] : . $ 
```

Type `quit` or `exit` to leave the shell.

Command reference (summary)
---------------------------
General command shape:

```
<base> <action> <type_marker> <value>
```

- `base`: `file`, `dir`, `disk`, `kos` (or `quit`/`exit`).
- `action`: `-make`, `-remove`, `-list`, `-rename`, etc.
- `type_marker`: `@` `%` `:` `!` (some actions require it; parser accepts commands without a marker).
- `value`: path or other action argument.

file commands
-------------
- `file -make @ <path>` — create empty file (creates parent directories).
- `file -remove @ <path>` — delete file.
- `file -rename @ <new-path>` — rename file (prompts for old name).
- `file -stat @ <path>` — print os.stat for the file.

dir commands
------------
- `dir -make @ <path>` — create directory (creates parents).
- `dir -remove @ <path>` — delete directory; if not empty removes recursively.
- `dir -list ! <path>` — list directory contents (default `.`).
- `dir -goto @ <path>` — walk and print tree entries.

disk commands
-------------
A simple in-memory mapping of logical disk letters to paths. Defaults: A → repo cwd, B/C → /tmp paths.
- `disk -list` — list mapped disks.
- `disk -use @ <LETTER>` — switch current disk.
- `disk -mount @ <LETTER> <path>` — mount a path to a letter (creates path).

kos commands
------------
- `kos -help` — show quick kos help.
- `kos -version` — prints HC-KOS version.
- `kos -clear` — clear screen.
- `kos -disk` — show disk helper text.

Shortcuts
---------
- `clear` — clear screen.
- `quit` / `exit` / `q` — exit the shell.

Examples
--------
- Create a file:

```
file -make @ docs/readme.txt
```

- List current directory:

```
dir -list ! .
```

- Mount a new disk and switch to it:

```
disk -mount @ D /mnt/mydisk
disk -use @ D
```

Internals and design
---------------------
- Entrypoint: `index.py` imports and runs `A.kos.main.main()`.
- Parser: `A/kos/main.py` contains `parse_command()` that recognizes the type markers and returns `(base, action, type, value)`.
- Operations: `A/kos/baces/files.py` and `A/kos/baces/dirs.py` implement the file system primitives and include basic error handling.

Packaging and release notes
--------------------------
This repo currently uses an in-memory version string and minimal metadata.
Planned next steps for a public release:

1. Add `LICENSE` (MIT recommended).
2. Add a `pyproject.toml` or `setup.py` for packaging.
3. Persist disk mappings to `.hc-kos.json` to survive restarts.
4. Add tests and CI (GitHub Actions) and automated release tagging.

Contributing
------------
Contributions are welcome. For a small project like this:

1. Fork the repo on GitHub.
2. Create a branch: `feature/<topic>`.
3. Make changes and add tests where appropriate.
4. Open a pull request and describe the change.

License
-------
This repository does not currently include a LICENSE file in the workspace. For public release, add a license (MIT is recommended) and include license text in `LICENSE`.

Security and safety
-------------------
- HC-KOS performs real FS operations. Avoid running it as root on production machines.
- There is no sandboxing; treat it as a local developer tool only.

Contact
-------
Hard Code LLC (HC-LLC) — https://github.com/hardcode-llc

