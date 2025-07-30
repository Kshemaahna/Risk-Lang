import sys
from parser import parse, simulate

def main():
    if len(sys.argv) != 2:
        print("Usage: risklang <file.risk>")
        return
    with open(sys.argv[1], "r") as f:
        dsl = f.read()
    parsed = parse(dsl)
    results = simulate(parsed)
    print("Simulation Results:")
    print(results)

if __name__ == "__main__":
    main()
