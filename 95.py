class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def generateTrees(n: int) -> list[TreeNode]:
    if n == 0:
        return []

    def dfs_build(l, r):
        if l > r:
            return [None]
        res = []

        for i in range(l, r + 1):
            L_st, R_st = dfs_build(l, i - 1), dfs_build(i + 1, r)

            for L in L_st:
                for R in R_st:
                    root = TreeNode(i)
                    root.left = L
                    root.right = R
                    res.append(root)
        return res

    return dfs_build(1, n)

generateTrees(3)