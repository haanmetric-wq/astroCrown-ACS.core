def f_pure(reserve_value_btc: float, defended_qty: float) -> float:
    if defended_qty <= 0:
        raise ValueError("Defended quantity must be > 0")
    return reserve_value_btc / defended_qty

def lcr(reserve_value_btc: float, defended_qty: float) -> float:
    fp = f_pure(reserve_value_btc, defended_qty)
    denom = fp * defended_qty
    if denom <= 0:
        raise ValueError("Invalid denominator for LCR")
    return reserve_value_btc / denom
