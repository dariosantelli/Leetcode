def getLonelyNodes(self, root):
    stack = []
    results = []

    while stack or root:
        while root:
            stack.append(root)
            root = root.left

        root = stack.pop()
        if root.left is not None and root.right is None:
            results.append(root.left.val)
        elif root.left is None and root.right is not None:
            results.append(root.right.val)
        root = root.right

    return results