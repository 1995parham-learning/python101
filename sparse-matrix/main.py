"""
Write a SparseMatrix class that implements the following two methods:

1) add - return a new SparseMatrix with the results of adding two SparseMatrix objects. Results should be the same
for all positions in the matrix as if we were adding two dense matrices naively. 

2) matrix multiplication
"""

from __future__ import annotations


class SparseMatrix:
    def __init__(self, matrix: list[list[int]] | None = None):
        self.matrix: dict[tuple[int, int], int] = {}
        self.row = 0
        self.col = 0

        if matrix is not None:
            self.row = len(matrix)
            self.col = len(matrix[0])

            for i, row in enumerate(matrix):
                for j, cell in enumerate(row):
                    if cell != 0:
                        self.matrix[(i, j)] = cell

    def __add__(self, other: SparseMatrix) -> SparseMatrix:
        if self.row != other.row:
            raise ValueError()
        if self.col != other.col:
            raise ValueError()

        result = SparseMatrix()
        result.row = self.row
        result.col = self.col

        keys = set(self.matrix.keys()) | set(other.matrix.keys())
        for key in keys:
            result.matrix[key] = self.matrix.get(key, 0) + other.matrix.get(key, 0)

        return result


if __name__ == "__main__":
    # 1 0 1
    # 0 0 0
    sm1 = SparseMatrix([[1, 0, 1], [0, 0, 0]])
    # 1 0 1
    # 0 1 0
    sm2 = SparseMatrix([[1, 0, 1], [0, 1, 0]])

    sm_sum = sm1 + sm2
    print(sm_sum.matrix)
