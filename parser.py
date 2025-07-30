from lark import Lark, Transformer

grammar = """
    start: portfolio scenario metrics

    portfolio: "portfolio" "{" asset+ "}"
    asset: "asset" ESCAPED_STRING "qty:" NUMBER

    scenario: "scenario" ESCAPED_STRING "{" scenario_line+ "}"
    scenario_line: ESCAPED_STRING ":" ("drop" SIGNED_NUMBER "%" | "drop" SIGNED_NUMBER "%" | "correlation:" "increase" "all" "to" NUMBER | "liquidity:" "reduce" "by" NUMBER)

    metrics: "metrics" "{" metric+ "}"
    metric: "pnl" | "var" "confidence:" NUMBER

    %import common.ESCAPED_STRING
    %import common.NUMBER
    %import common.SIGNED_NUMBER
    %import common.WS
    %ignore WS
"""

class RiskTransformer(Transformer):
    def start(self, items):
        return {"portfolio": items[0], "scenario": items[1], "metrics": items[2]}
    
    def portfolio(self, assets):
        return [dict(name=a[0], qty=a[1]) for a in assets]
    
    def asset(self, items):
        return (items[0][1:-1], float(items[1]))
    
    def scenario(self, items):
        name = items[0][1:-1]
        details = items[1:]
        return {"name": name, "actions": details}
    
    def scenario_line(self, items):
        if "correlation" in items:
            return {"type": "correlation", "value": float(items[-1])}
        elif "liquidity" in items:
            return {"type": "liquidity", "value": float(items[-1])}
        else:
            asset = items[0][1:-1]
            drop = float(items[2])
            return {"type": "drop", "asset": asset, "value": drop}
    
    def metrics(self, items):
        return items

    def metric(self, items):
        if len(items) == 1:
            return items[0]
        return {"var": float(items[1])}

parser = Lark(grammar, parser="lalr", transformer=RiskTransformer())

def parse(text):
    return parser.parse(text)

def simulate(parsed):
    portfolio = {a["name"]: a["qty"] for a in parsed["portfolio"]}
    prices = {k: 100.0 for k in portfolio}  # mock price
    drops = {}
    correlation = 0.0
    liquidity = 1.0

    for act in parsed["scenario"]["actions"]:
        if act["type"] == "drop":
            drops[act["asset"]] = act["value"]
        elif act["type"] == "correlation":
            correlation = act["value"]
        elif act["type"] == "liquidity":
            liquidity -= act["value"]

    pnl = sum(
        portfolio[a] * prices[a] * (drops.get(a, 0.0) / 100.0)
        for a in portfolio
    )

    var = abs(pnl) * (1 + correlation) * liquidity
    return {"pnl": pnl, "var_approx": var}
