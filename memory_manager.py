class MemoryManager:
    def __init__(self, memory_size):
        self.buffer = {}
        self.memory_size = memory_size

    def get_sizeof_free_block(self):
        return self.memory_size - self.get_sizeof_used_memory()

    def get_sizeof_used_memory(self):
        return len(self.buffer.keys())

    def _save_single_byte(self, b):
        index = -1
        while index < self.memory_size-1:
            index = index + 1
            if self.buffer.get(index) is None:
                self.buffer[index] = b
                return index
        raise Exception(
            f"Something went error can find free index while _sizeof_free_block is{self.get_sizeof_free_block}")

    def alloc(self, memory_block: list):
        print(self.get_sizeof_free_block())
        if self.get_sizeof_free_block() == 0 or self.get_sizeof_free_block() < len(memory_block) - 1:
            raise Exception(f"There is no enough memory {len(memory_block)} > {self.get_sizeof_free_block}")
        data_index = -1
        save_block ={}
        while data_index < len(memory_block) - 1:
            data_index = data_index + 1
            memory_block_index = self._save_single_byte(memory_block[data_index])
            save_block[data_index] = memory_block_index
        return save_block

    def read(self, memory_block: dict):
        if memory_block is None:
            raise Exception(" Memory Block is None")
        result = []
        for key in memory_block.keys():
            result.append(self.buffer[memory_block.get(key)])
        return result

    def free(self, memory_indexes: list):
        if memory_indexes is None:
            raise Exception(" Memory Block is None")
        for index in memory_indexes:
            del self.buffer[index]

    def print_memory_buffer(self):
        result = []
        index = -1
        while index < self.memory_size-1:
            index = index+1
            if self.buffer.get(index):
                result.append(self.buffer.get(index))
            else:
                result.append('_')

        print(result)
        print(f"free size {self.get_sizeof_free_block()} , used size {self.get_sizeof_used_memory()}")
