class ListNode():
    def __init__(self, key=-1, val=-1, next = None):
        self.key = key 
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]
        
    def hash(self, key: int) -> int:
        # simple modulo operation ensures that the index value is within the
        # bounds of the array size. In this case, 0-999.
        h = key % 1000
        return h
    
    def put(self, key: int, value: int) -> None:
        # get the current node from the map, this is a dummy head
        #
        cur = self.map[self.hash(key)]
        
        # we want to end up at the last node in the linked list, so using
        # curr.next. If we used cur, when the loop ends, cur would be None.
        #
        while cur.next:
            # if the key already exists, update the value and return
            # chaining is happening here, so for same index, we can have
            # multiple keys with different values
            #
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
            
        # if key does not exist, add a new node to the end of the list
        #
        cur.next = ListNode(key, value)
        

    def get(self, key: int) -> int:
        cur = self.map[self.hash(key)]
        
        while cur:
            if cur.key == key:
                return cur.val
            cur = cur.next
        return -1
    
    def remove(self, key: int) -> None:
        curr = self.map[self.hash(key)]
        
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        


