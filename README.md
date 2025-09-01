# AstroCrown ACS Core

Mission-first simulation engine for the Anti-Crash System (ACS) with NOVA governance.

- Pure floor policy: F_pure = V_reserves / Q_defended
- LCR invariant: always 1.00 using the pure floor (no fees included)
- Execution is fee-aware (per-venue fees/gas/slippage adjust trigger prices), but the official floor remains fee-free

## Invariants

- LCR = 1.00 at all times (pure floor, defended quantity = circulating supply)
- Safe releases only if fee-aware feasibility holds and projected post-trade LCR ≥ 1.00
- Execution triggers on venues: P_trigger,v = F_pure - (fee_fix + fee_pct * F_pure + gas + slip)

## Layout

- `/src` — core functions (LCR, triggers, guards)
- `/config` — NOVA config (pure floor mode), discovery knobs, manifests
- `/tests` — unit tests for core invariants

## Public note on fees

Floor price is computed as total reserve value divided by defended tokens (fees not included). Actual buyback triggers on external venues may appear below the floor to account for platform fees, gas, and slippage. On the AstroCrown Platform, only gas fees apply, so buybacks may occur closer to the official floor.
