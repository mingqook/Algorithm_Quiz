class MyHashSet:

    def __init__(self):
        self.set = []

    def add(self, key: int) -> None:
        if not self.set:
            self.set = [key]
        else:
            self.set.append(key)

    def remove(self, key: int) -> None:
        if self.set != None:
            if key in self.set:
                self.set = list(set(self.set) - set([key]))

    def contains(self, key: int) -> bool:
        
        if not self.set:
            return False
        else:
            if key in self.set:
                return True
            else:
                return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)