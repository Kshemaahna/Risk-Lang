# parser.py

from lark import Lark, Transformer

grammar = r"""
    start: portfolio scenario? metrics?

    portfolio: "portfolio" "{" asset+ "}"
    asset: "asset" ESCAPED_STRING "qty:" INT

    scenario: "scenario" ESCAPED_STRING "{" scenario_line+ "}"
    scenario_line: ESCAPED_STRING ":" "drop" SIGNED_NUMBER "%"
                 | "correlation:" "increase" "all" "to" SIGNED_NUMBER
                 | "liquidity:" "reduce" "by" SIGNED_NUMBER

    metrics: "metrics" "{" metric+ "}"
    metric: "pnl" -> pnl
          | "var" "confidence:" INT -> var

    %import common.INT
    %import common.SIGNED_NUMBER
    %import common.ESCAPED_STRING
    %import common.WS
    %ignore WS
"""

class RiskTransformer(Transformer):
    def start(self, items):
        result = {"portfolio": {}, "scenario": {}, "metrics": []}
        for item in items:
            result.update(item)
        return result

    def portfolio(self, items):
        return {"portfolio": dict(items)}

    def asset(self, items):
        name = items[0].value.strip('"')
        qty = int(items[1])
        return (name, qty)

    def scenario(self, items):
        name = items[0].value.strip('"')
        data = {"name": name, "drops": {}}
        for line in items[1:]:
            data.update(line)
        return {"scenario": data}

    def scenario_line(self, items):
        if len(items) == 3 and items[1] == "drop":
            asset = items[0].value.strip('"')
            drop = float(items[2])
            return {"drops": {asset: drop}}
        elif items[0] == "correlation:":
            return {"correlation": float(items[-1])}
        elif items[0] == "liquidity:":
            return {"liquidity": float(items[-1])}
        return {}

    def metrics(self, items):
        return {"metrics": items}

    def pnl(self, _):
        return "pnl"

    def var(self, items):
        return {"var": int(items[0])}

parser = Lark(grammar, parser='lalr', transformer=RiskTransformer())

def parse(text):
    return parser.parse(text)
