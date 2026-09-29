class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = {}
        cols = {}
        boxes = {}

        for i in range(9):

            rows[i] = set()
            cols[i] = set()
            boxes[i] = set()

        for row in range(9):
            for col in range(9):

                num = board[row][col]

                if num == ".":
                    continue

                # Check row
                if num in rows[row]:
                    return False

                rows[row].add(num)

                # Check column
                if num in cols[col]:
                    return False

                cols[col].add(num)

                # Find which 3x3 box
                box = (row // 3) * 3 + (col // 3)

                # Check box
                if num in boxes[box]:
                    return False

                boxes[box].add(num)

        return True