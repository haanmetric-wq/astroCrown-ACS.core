from src.lcr import f_pure, lcr

def test_pure_floor_and_lcr_identity():
    V = 100.0
    Q = 1000.0
    Fp = f_pure(V, Q)
    assert abs(Fp - 0.1) < 1e-12
    assert abs(lcr(V, Q) - 1.0) < 1e-12
