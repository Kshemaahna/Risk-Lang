# simulator.py

def simulate(parsed):
    portfolio = parsed.get("portfolio", {})
    scenario = parsed.get("scenario", {})
    metrics = parsed.get("metrics", [])

    results = {}

    # Very basic PnL simulation
    if "pnl" in metrics:
        pnl_result = {}
        for asset, qty in portfolio.items():
            drop_pct = scenario.get("drops", {}).get(asset, 0)
            pnl_result[asset] = qty * drop_pct / 100.0
        results["pnl"] = pnl_result

    # Very basic VaR stub
    for metric in metrics:
        if isinstance(metric, dict) and "var" in metric:
            results["var"] = {"value": -123.45, "confidence": metric["var"]}

    return results



