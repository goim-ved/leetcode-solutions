from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    self.invertTree(root.left)
    self.invertTree(root.right)
    return root

if __name__ == "__main__":
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    root = TreeNode(2, node1, node3)
    
    print(invertTree(root))