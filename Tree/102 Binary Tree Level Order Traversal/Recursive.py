def levelOrder(self, root):
    results = []
    if not root:
        return results
    self.helper(root, results, 0)
    return results


def helper(self, root, results, level):
    if root is None:
        return
    else:
        if len(results) == level:
            results.append([])
        results[level].append(root.val)

        self.helper(root.left, results, level + 1)
        self.helper(root.right, results, level + 1)