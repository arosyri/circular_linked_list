import unittest
from array_list.array_list import ArrayList

class TestArrayList(unittest.TestCase):

    def test_append_and_length(self):
        alist = ArrayList()
        alist.append('a')
        alist.append('b')
        self.assertEqual(alist.length(), 2)

    def test_insert(self):
        alist = ArrayList()
        alist.append('a')
        alist.insert('b', 0)
        self.assertEqual(alist.get(0), 'b')
        self.assertEqual(alist.get(1), 'a')

    def test_delete(self):
        alist = ArrayList()
        alist.append('a')
        alist.append('b')
        removed = alist.delete(0)
        self.assertEqual(removed, 'a')
        self.assertEqual(alist.get(0), 'b')

    def test_deleteAll(self):
        alist = ArrayList()
        alist.append('a')
        alist.append('b')
        alist.append('a')
        alist.deleteAll('a')
        self.assertEqual(alist.length(), 1)
        self.assertEqual(alist.get(0), 'b')

    def test_get_invalid_index(self):
        alist = ArrayList()
        alist.append('a')
        with self.assertRaises(IndexError):
            alist.get(5)

    def test_clone(self):
        alist = ArrayList()
        alist.append('a')
        alist.append('b')
        clone = alist.clone()
        self.assertEqual(clone.get(0), 'a')
        self.assertEqual(clone.get(1), 'b')

    def test_reverse(self):
        alist = ArrayList()
        alist.append('a')
        alist.append('b')
        alist.append('c')
        alist.reverse()
        self.assertEqual(alist.get(0), 'c')
        self.assertEqual(alist.get(2), 'a')

    def test_findFirst_and_findLast(self):
        alist = ArrayList()
        alist.append('x')
        alist.append('y')
        alist.append('x')
        self.assertEqual(alist.findFirst('x'), 0)
        self.assertEqual(alist.findLast('x'), 2)

    def test_clear(self):
        alist = ArrayList()
        alist.append('a')
        alist.clear()
        self.assertEqual(alist.length(), 0)

    def test_extend(self):
        a = ArrayList()
        b = ArrayList()
        a.append('1')
        b.append('2')
        a.extend(b)
        self.assertEqual(a.length(), 2)
        self.assertEqual(a.get(0), '1')
        self.assertEqual(a.get(1), '2')

if __name__ == '__main__':
    unittest.main()
