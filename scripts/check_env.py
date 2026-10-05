import sys
import platform

def check_environment():
    print(f"Python version: {sys.version}")
    print(f"OS: {platform.system()} {platform.release()}")

if __name__ == "__main__":
    check_environment()