import os


def run(action, type_, value):
    action = (action or "").strip()
    if action in ("-h", "-help", "help"):
        print("HC-KOS kos commands:\n  -help       Show this help\n  -version    Show version\n  -quit       Exit the shell\n  -clear      Clear the screen\n  -disk       Disk management help")
    elif action == "-version" or action == "version":
        print("HC-KOS v0.1")
    elif action in ("-quit", "-exit"):
        print("Use 'kos -quit' or type 'quit' at the prompt to exit.")
    elif action in ("-clear", "clear"):
        os.system("clear")
    elif action == "-disk":
        print("disk commands:\n  disk -list !        List mounted disks\n  disk -use @ <L>     Switch to disk L\n  disk -mount @ L P   Map disk L to path P")
    elif action == "":
        print("kos: missing action. Use 'kos -help' for usage.")
    else:
        print(f"Unknown kos action: {action}")
