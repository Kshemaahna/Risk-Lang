from parser import parse
from simulator import simulate

def run(code: str):
    parsed = parse(code)
    result = simulate(parsed)
    return result
