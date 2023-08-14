import unittest
from memory_manager import MemoryManager


class MemoryMangerTest(unittest.TestCase):

    def test_Example(self):
        memory_manager = MemoryManager(5)
        self.assertEqual(memory_manager.get_sizeof_free_block(), 5)
        self.assertEqual(memory_manager.get_sizeof_used_memory(), 0)

        memory_manager.alloc(['X', 'X', 'X', 'X', 'X'])
        self.assertEqual(memory_manager.get_sizeof_used_memory(), 5)
        self.assertEqual(memory_manager.get_sizeof_free_block(), 0)
        memory_manager.print_memory_buffer()

        memory_manager.free([1, 3])
        self.assertEqual(memory_manager.get_sizeof_used_memory(), 3)
        self.assertEqual(memory_manager.get_sizeof_free_block(), 2)

        memory_manager.print_memory_buffer()

        memory_manager.alloc(['Y', 'Y'])

        memory_manager.print_memory_buffer()

    def test_alloc(self):
        memory_manager = MemoryManager(4)
        self.assertEqual(memory_manager.get_sizeof_free_block(), 4)
        self.assertEqual(memory_manager.get_sizeof_used_memory(), 0)

        memory_manager.alloc(['1', '2', '3'])
        self.assertEqual(memory_manager.get_sizeof_used_memory(), 3)
        self.assertEqual(memory_manager.get_sizeof_free_block(), 1)

    def test_read(self):
        memory_manager = MemoryManager(4)
        save_block = memory_manager.alloc(['R', 'a', 'm', 'i'])
        print(save_block)
        res = memory_manager.read(save_block)

        self.assertEqual(res, ['R', 'a', 'm', 'i'])

    def test_exception(self):
        memory_manager = MemoryManager(1)

        with self.assertRaises(Exception):
            memory_manager.alloc(['1', '2', '3'])


if __name__ == '__main__':
    unittest.main()
