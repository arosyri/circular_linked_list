import unittest
from circular_linked_list.circular_linked_list import CircularLinkedList

class TestCircularLinkedList(unittest.TestCase):

    def test_append_and_length(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.append('b')
        self.assertEqual(clist.length(), 2)

    def test_insert(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.insert('b', 0)
        self.assertEqual(clist.get(0), 'b')
        self.assertEqual(clist.get(1), 'a')

    def test_delete(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.append('b')
        removed = clist.delete(0)
        self.assertEqual(removed, 'a')
        self.assertEqual(clist.get(0), 'b')

    def test_deleteAll(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.append('b')
        clist.append('a')
        clist.deleteAll('a')
        self.assertEqual(clist.length(), 1)
        self.assertEqual(clist.get(0), 'b')

    def test_get_invalid_index(self):
        clist = CircularLinkedList()
        clist.append('a')
        with self.assertRaises(IndexError):
            clist.get(5)

    def test_clone(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.append('b')
        clone = clist.clone()
        self.assertEqual(clone.get(0), 'a')
        self.assertEqual(clone.get(1), 'b')

    def test_reverse(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.append('b')
        clist.append('c')
        clist.reverse()
        self.assertEqual(clist.get(0), 'X')
        self.assertEqual(clist.get(2), 'a')

    def test_findFirst_and_findLast(self):
        clist = CircularLinkedList()
        clist.append('x')
        clist.append('y')
        clist.append('x')
        self.assertEqual(clist.findFirst('x'), 0)
        self.assertEqual(clist.findLast('x'), 2)

    def test_clear(self):
        clist = CircularLinkedList()
        clist.append('a')
        clist.clear()
        self.assertEqual(clist.length(), 0)

    def test_extend(self):
        a = CircularLinkedList()
        b = CircularLinkedList()
        a.append('1')
        b.append('2')
        a.extend(b)
        self.assertEqual(a.length(), 2)
        self.assertEqual(a.get(0), '1')
        self.assertEqual(a.get(1), '2')

if __name__ == '__main__':
    unittest.main()
