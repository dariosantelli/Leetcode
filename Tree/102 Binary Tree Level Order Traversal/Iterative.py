def levelOrder(self, root):
    results = []
    if not root:
        return results
    que = [root]
    temp = []
    level = 0

    while que:
        results.append([])
        for i in range(len(que)):
            results[level].append(que[i].val)
            if que[i].left:
                temp.append(que[i].left)
            if que[i].right:
                temp.append(que[i].right)
        que = []
        if len(temp) > 0:
            for i in range(len(temp)):
                que.append(temp.pop(0))
        level += 1

    return results