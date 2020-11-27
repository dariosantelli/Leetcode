def getLonelyNodes(self, root):
    results = []
    if not root:
        return results
    self.helper(root, results)
    return results


def helper(self, root, results):
    if root is None:
        return
    else:
        self.helper(root.left, results)
        if root.left is not None and root.right is None:
            results.append(root.left.val)
        elif root.left is None and root.right is not None:
            results.append(root.right.val)
        self.helper(root.right, results)