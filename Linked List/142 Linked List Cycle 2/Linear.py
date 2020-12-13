def detectCycle(self, head):
    if not head:
        return None
    checkSet = set()

    while True:
        if head not in checkSet:
            checkSet.add(head)
        elif head in checkSet:
            return head

        # if there's no cycle
        if head.next == None:
            return None

        head = head.next