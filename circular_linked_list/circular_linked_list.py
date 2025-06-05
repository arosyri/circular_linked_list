class Node:
    def __init__(self, value: str):
        if len(value) != 1:
            raise ValueError("Only single characters are allowed")
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.tail = None
        self.size = 0

    def length(self) -> int:
        return self.size

    def append(self, element: str) -> None:
        new_node = Node(element)
        if not self.tail:
            self.tail = new_node
            self.tail.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def insert(self, element: str, index: int) -> None:
        if index < 0 or index > self.size:
            raise IndexError("Invalid index")
        new_node = Node(element)
        if not self.tail:
            if index != 0:
                raise IndexError("Invalid index in empty list")
            self.tail = new_node
            self.tail.next = new_node
        elif index == 0:
            new_node.next = self.tail.next
            self.tail.next = new_node
        elif index == self.size:
            self.append(element)
            return
        else:
            prev = self.tail.next
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
        self.size += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        if self.size == 1:
            value = self.tail.value
            self.tail = None
        elif index == 0:
            value = self.tail.next.value
            self.tail.next = self.tail.next.next
        else:
            prev = self.tail.next
            for _ in range(index - 1):
                prev = prev.next
            value = prev.next.value
            prev.next = prev.next.next
            if index == self.size - 1:
                self.tail = prev
        self.size -= 1
        return value

    def deleteAll(self, element: str) -> None:
        if self.size == 0:
            return
        dummy = Node('0')
        dummy.next = self.tail.next
        prev, curr = dummy, self.tail.next
        new_tail = None
        count = self.size
        removed = 0
        for _ in range(count):
            if curr.value == element:
                removed += 1
                prev.next = curr.next
                if curr == self.tail:
                    new_tail = prev
            else:
                prev = curr
            curr = curr.next
        self.size -= removed
        self.tail = new_tail if removed > 0 else self.tail
        if self.size == 0:
            self.tail = None
        else:
            self.tail.next = dummy.next

    def get(self, index: int) -> str:
        if index < 0 or index >= self.size:
            raise IndexError("Invalid index")
        curr = self.tail.next
        for _ in range(index):
            curr = curr.next
        return curr.value

    def clone(self):
        new_list = CircularLinkedList()
        if self.size == 0:
            return new_list
        curr = self.tail.next
        for _ in range(self.size):
            new_list.append(curr.value)
            curr = curr.next
        return new_list

    def reverse(self) -> None:
        if self.size < 2:
            return
        prev = self.tail
        curr = self.tail.next
        for _ in range(self.size):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.tail = curr

    def findFirst(self, element: str) -> int:
        if self.size == 0:
            return -1
        curr = self.tail.next
        for i in range(self.size):
            if curr.value == element:
                return i
            curr = curr.next
        return -1

    def findLast(self, element: str) -> int:
        if self.size == 0:
            return -1
        curr = self.tail.next
        result = -1
        for i in range(self.size):
            if curr.value == element:
                result = i
            curr = curr.next
        return result

    def clear(self) -> None:
        self.tail = None
        self.size = 0

    def extend(self, other) -> None:
        clone = other.clone()
        if clone.size == 0:
            return
        if self.size == 0:
            self.tail = clone.tail
        else:
            temp = self.tail.next
            self.tail.next = clone.tail.next
            clone.tail.next = temp
            self.tail = clone.tail
        self.size += clone.size

