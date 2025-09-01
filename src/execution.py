from typing import Dict

def venue_trigger_price(f_pure: float, fees: Dict[str, float]) -> float:
    """
    Compute fee-aware trigger price for a venue.
    fees keys:
      - fee_fix (BTC)
      - fee_pct (fraction of price, e.g., 0.001 for 0.1%)
      - gas (BTC)
      - slippage (BTC)
    """
    fee_fix = fees.get("fee_fix", 0.0)
    fee_pct = fees.get("fee_pct", 0.0)
    gas = fees.get("gas", 0.0)
    slip = fees.get("slippage", 0.0)
    return f_pure - (fee_fix + fee_pct * f_pure + gas + slip)
