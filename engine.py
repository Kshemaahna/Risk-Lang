from risklang.core.parser import parse
from risklang.core.simulator import simulate

def run(code: str):
    parsed = parse(code)
    result = simulate(parsed)
    return result
