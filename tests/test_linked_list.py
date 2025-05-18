import unittest
from linked_list import LinkedList

class TestLinkedList(unittest.TestCase):
    def setUp(self):
        self.ll = LinkedList()

    def test_insert_at_front(self):
        self.ll.insert_at_front(1)
        self.ll.insert_at_front(2)
        self.assertEqual(self.ll.head.data, 2)
        self.assertEqual(self.ll.head.next.data, 1)

    def test_recursive_sum_empty(self):
        self.assertEqual(self.ll.recursive_sum(), 0)

    def test_recursive_sum(self):
        self.ll.insert_at_front(10)
        self.ll.insert_at_front(20)
        self.ll.insert_at_end(5)
        # List: 20 -> 10 -> 5
        self.assertEqual(self.ll.recursive_sum(), 35)

    def test_recursive_search(self):
        self.ll.insert_at_front(10)
        self.ll.insert_at_front(20)
        self.assertTrue(self.ll.recursive_search(10))
        self.assertFalse(self.ll.recursive_search(999))


    def test_recursive_reverse(self):
        # Insert 3 items
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.ll.insert_at_end(3)
        self.ll.recursive_reverse()
        # Should be reversed: 3 -> 2 -> 1
        self.assertEqual(self.ll.head.data, 3)
        self.assertEqual(self.ll.head.next.data, 2)
        self.assertEqual(self.ll.head.next.next.data, 1)

if __name__ == '__main__':
    unittest.main()
