class CacheNode:
    def __init__(self, val):
        self.next = None
        self.val = val

class Cache:
    def __init__(self, this_node=None):
        self.last = this_node
        self.first = this_node
        self.map = {}

    def enqueue(self, NewCacheNode):
        self.last.next = NewCacheNode
        self.last = NewCacheNode

    def requeue(self):
        pop_node = self.first
        self.first = self.first.next

        pop_node.next = None
        self.enqueue(pop_node)
        self.last = pop_node

    def findLocation(self, val):
        

def printCache(C):
    head = C.first
    while(head != None):
        print(head.val)
        head = head.next
    print(">>>>>>>>>>>>>>")


# def printCacheBackwards(C):
#     tail = C.last
#     while tail != None:
#         print(tail)
#         print(tail.val)
#         tail = tail.prev
#     print("<<<<<<<<<<<<<<")




if __name__ == '__main__':

    first = CacheNode(1)
    second = CacheNode(2)
    third = CacheNode(3)

    C = Cache(first)
    C.enqueue(second)
    C.enqueue(third)
    C.requeue()
    C.requeue()

    printCache(C)
    # printCacheBackwards(C)


