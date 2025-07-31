import sys
from engine import run

def main():
    if len(sys.argv) != 2:
        print("Usage: risklang <file.risk>")
        return

    filepath = sys.argv[1]
    try:
        with open(filepath, "r") as f:
            code = f.read()
    except FileNotFoundError:
        print(f"File not found: {filepath}")
        return

    try:
        results = run(code)
        print("Simulation Results:")
        print(results)
    except Exception as e:
        print("Error during execution:")
        print(e)

if __name__ == "__main__":
    main()
