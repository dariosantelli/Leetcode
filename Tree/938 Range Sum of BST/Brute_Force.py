def rangeSumBST(self, root, low, high):
    resultSum = 0
    result = self.helper(root, low, high, [])

    for item in result:
        if item <= high and item >= low:
            resultSum += item
    return resultSum


def helper(self, root, low, high, result):
    if root is None:
        return
    else:
        self.helper(root.left, low, high, result)
        result.append(root.val)
        self.helper(root.right, low, high, result)

    return result