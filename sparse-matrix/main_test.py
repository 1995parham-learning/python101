from main import SparseMatrix


def test_add():
    # 1 0 1
    # 0 0 0
    sm1 = SparseMatrix([[1, 0, 1], [0, 0, 0]])
    assert sm1.matrix == {(0, 0): 1, (0, 2): 1}

    # 1 0 1
    # 0 1 0
    sm2 = SparseMatrix([[1, 0, 1], [0, 1, 0]])
    assert sm2.matrix == {(0, 0): 1, (0, 2): 1, (1, 1): 1}

    sm_sum = sm1 + sm2
    assert sm_sum.matrix == {(0, 0): 2, (0, 2): 2, (1, 1): 1}
