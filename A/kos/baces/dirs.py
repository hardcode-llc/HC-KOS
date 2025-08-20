import os
import shutil

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
            os.makedirs(value, exist_ok=True)
        elif action == "-remove" and cheakValueType(type_, "@"):
            # remove dir, if not empty remove tree
            if os.path.isdir(value):
                try:
                    os.rmdir(value)
                except OSError:
                    shutil.rmtree(value)
            else:
                print(f"Not a directory: {value}")
        elif action == "-rename" and cheakValueType(type_, "@"):
            old = input("old dir name: ")
            os.rename(old, value)
        elif action == "-list" and cheakValueType(type_, "!"):
            target = value or "."
            print('\n'.join(os.listdir(target)))
        elif action == "-replace" and cheakValueType(type_, "@"):
            old = input("old dir path: ")
            os.replace(old, value)
        elif action == "-goto" and cheakValueType(type_, "@"):
            for root, dirs, files in os.walk(value):
                print(root, dirs, files)
        else:
            print(f"Unknown dir action: {action}")
    except FileNotFoundError as e:
        print(f"File error: {e}")
    except PermissionError as e:
        print(f"Permission error: {e}")
    except Exception as e:
        print(f"Error: {e}")