from memory_manager import MemoryManager

memory_manager = MemoryManager(4)

memory_manager.alloc(['4', '4', '4'])
memory_manager.print_memory_buffer()

memory_manager.alloc(['4'])
memory_manager.print_memory_buffer()

memory_manager.alloc(['3'])


memory_manager.free([3, 2])

memory_manager.print_memory_buffer()
