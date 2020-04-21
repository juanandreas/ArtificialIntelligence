class LinkedList:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def get_val(self):
        return self.val