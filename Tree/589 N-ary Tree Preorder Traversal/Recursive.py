def preorder(self, root):
    results = []
    self.helper(root, results)
    return results


def helper(self, root, results):
    if root is None:
        return
    else:
        results.append(root.val)
        if root.children:
            for i in range(len(root.children)):
                self.helper(root.children[i], results)

    return results