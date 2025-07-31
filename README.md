# RiskLang: A Domain Specific Language for Portfolio Risk Management

RiskLang is a lightweight domain-specific language (DSL) designed for specifying and simulating portfolio risk scenarios. It provides a structured and human-readable syntax to define assets, market shocks, and risk metrics for quantitative risk analysis and stress testing. This is an ongoing project at this moment.

---

## Language Overview

A `.risk` file includes three main components:

- **Portfolio**: Defines a collection of assets with associated quantities.
- **Scenario**: Describes market events such as asset price drops, changes in correlation, and liquidity adjustments.
- **Metrics**: Specifies risk measures to compute, such as profit and loss (PnL) and Value-at-Risk (VaR).

An example .risk file can be found in example_Risk.risk in this repository. In general, it would suffice to follow the format and save your own data as a .risk file from any text editor.

---

## Usage

### Install dependencies

```pip install -r requirements.txt  ```
or  
```pip install lark```

### Run simulation

python cli.py example_risk.risk

---

## Architecture

RiskLang operates in three stages:

1. **Parsing**: The DSL input is parsed using a Lark grammar into an abstract syntax tree (AST).  
2. **Transformation**: The AST is converted into structured Python data types representing the portfolio, scenarios, and metrics.  
3. **Simulation**: The simulation engine applies specified shocks to the portfolio and computes requested risk metrics.

---

## Supported Risk Metrics

- **Profit and Loss (PnL)**: Calculates portfolio losses/gains based on scenario price drops.  
- **Value-at-Risk (VaR) Approximation**: Provides a rough estimate of portfolio risk incorporating scenario-induced correlation and liquidity effects.

---

## Project Structure

| File                     | Description                                            |
|--------------------------|--------------------------------------------------------|
| `cli_risklang.py`        | Command-line interface to run RiskLang simulations.    |
| `parser.py`              | DSL parser and AST transformer implemented with Lark.  |
| `engine.py`              | Coordinates parsing and simulation execution.          |
| `simulator.py`           | Core simulation logic applying scenarios to portfolios.|
| `example_risk.risk`      | Sample RiskLang script demonstrating usage.            |
| `setup.py`               | Package installation and CLI entry point configuration.|

---

## Extensibility and Future Work

RiskLang is designed as a modular and extensible framework. Potential enhancements include:

- Integration with real market data for dynamic pricing.  
- Advanced risk metrics such as conditional VaR, expected shortfall, and scenario aggregation.  
- Support for time-series modeling and multi-period simulations.  
- Interactive REPL and visualization dashboards.  
- Formal DSL validation and richer grammar constructs for complex scenario definitions.

---




## Contact

For questions or contributions, please open an issue or submit a pull request.
