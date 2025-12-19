from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(self, root = Optional[TreeNode]) -> int:
    self.maxDiameter = 0
    def height(node):
        if not node:
            return 0
        leftH = height(node.left)
        rightH = height(node.right)
        currentHeight = leftH + rightH
        self.maxDiameter = max(self.maxDiameter, currentHeight)
        return 1 + max(leftH, rightH)
    height(root)
    return self.maxDiameter

if __name__ == "__main__":
    myTree = TreeNode()