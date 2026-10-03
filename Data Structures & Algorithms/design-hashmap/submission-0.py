class MyHashMap:

    def __init__(self):
        self.data = []

    def put(self, key: int, value: int) -> None:
        for i in self.data:
            if key == i[0]:
                i[1] = value
                return

        self.data.append([key, value])

    def get(self, key: int) -> int:
        for i in self.data:
            if key == i[0]:
                return i[1]
        return -1

    def remove(self, key: int) -> None:
        for i in self.data:
            if key == i[0]:
                self.data.remove(i)
                return
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)