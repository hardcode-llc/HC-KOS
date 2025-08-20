import os

def touch(filename):
    dirname = os.path.dirname(filename)
    if dirname and not os.path.exists(dirname):
        os.makedirs(dirname, exist_ok=True)
    if os.path.exists(filename):
        os.utime(filename, None)
    else:
        with open(filename, 'w'):
            pass

def cheakValueType(input_type, valueType):
    if input_type != valueType:
        print(f"""
HC-KOS Error!
ValueType {input_type} != {valueType}
ErrorType Value (string)
            """)
        return False
    else:
        return True

def run(action, type_, value):
    try:
        if action == "-make" and cheakValueType(type_, "@"):
            touch(value)
        elif action == "-remove" and cheakValueType(type_, "@"):
            os.remove(value)
        elif action == "-rename" and cheakValueType(type_, "@"):
            old = input("old file name: ")
            os.rename(old, value)
        elif action == "-stat" and cheakValueType(type_, "@"):
            print(os.stat(value))
        elif action == "-replace" and cheakValueType(type_, "@"):
            old = input("old file path: ")
            os.replace(old, value)
        else:
            print(f"Unknown file action: {action}")
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error: {e}")
