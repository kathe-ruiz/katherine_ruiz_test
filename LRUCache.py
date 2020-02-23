import collections
import threading


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

    def remove_expired_item(self, key):
        if key in self.items.keys():
            del self.items[key]
            self.my_list.remove(key)

    def get(self, key):
        """
        :type key: int
        :rtype: int
        if the key in dict exists then return value and remove the item from
        the current deque position and push it again to the top left 
        """
        if key in self.items:
            self.my_list.remove(key)
            self.my_list.appendleft(key)
            return self.items[key]

        return -1

    def put(self, key, value, time_limit=0):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        """
        If the length dict items are less of capacity, then add/update the item 
        to the dict and append left to the deque.
        """
        if len(self.items) <= self.capacity:
            if key not in self.items.keys():
                self.my_list.appendleft(key)
            else:
                self.my_list.remove(key)
                self.my_list.appendleft(key)
            self.items[key] = value

        """
        If the dict items are greater than capacity then I pop the last item
        and delete the item from dict
        """
        if len(self.items) == self.capacity + 1 and self.my_list:
            key = self.my_list.pop()
            if key in self.items:
                del self.items[key]
        """
        If the item expired, then trigger the function to remove it in the time limit
        """
        if time_limit > 0:
            threading.Timer(time_limit, self.remove_expired_item, [key]).start()

    def get_all(self):
        return self.items, self.my_list
