import collections
class LRUCache(object):
    items = {}
    capacity = 0
    my_list = collections.deque([])
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.my_list = collections.deque([])
        self.items = {}
        #print(self.my_list)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items:
            self.my_list.remove(key)
            self.my_list.appendleft(key)
            return self.items[key]
           
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if len(self.items) <= self.capacity:
            if key not in self.items.keys():
                self.my_list.appendleft(key)
            else:
                self.my_list.remove(key)
                self.my_list.appendleft(key)
            self.items[key] = value
                
                
        if len(self.items) == self.capacity+1 and self.my_list:
            key = self.my_list.pop()
            if key in self.items:
                del self.items[key]
    
    def getAll(self):
        return self.items, self.my_list
        
        