# Design a number container system that can do the following:

# Insert or Replace a number at the given index in the system.
# Return the smallest index for the given number in the system.
# Implement the NumberContainers class:

# NumberContainers() Initializes the number container system.
# void change(int index, int number) Fills the container at index with the number. If there is already a number at that index, replace it.
# int find(int number) Returns the smallest index for the given number, or -1 if there is no index that is filled by number in the system.
 
import heapq

class NumberContainers:
    def __init__(self):
        self.index_to_number = {}  # {index: number} - хранит, какое число стоит в каждом индексе
        self.number_to_indices = {}  # {number: MinHeap of indices} - хранит индексы для каждого числа
        self.valid_entries = {}  # {number: set of valid indices} - проверяет, какие индексы актуальны

    def change(self, index: int, number: int) -> None:
        # Если индекс уже содержал другое число, удаляем старый индекс из valid_entries
        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.valid_entries:
                self.valid_entries[old_number].discard(index)

        # Запоминаем новое число в index_to_number
        self.index_to_number[index] = number
        
        # Если число встречается впервые, создаём новую кучу и множество
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
            self.valid_entries[number] = set()

        # Добавляем индекс в кучу и в множество
        heapq.heappush(self.number_to_indices[number], index)
        self.valid_entries[number].add(index)

    def find(self, number: int) -> int:
        # Если число вообще не встречалось, возвращаем -1
        if number not in self.number_to_indices:
            return -1

        # Чистим кучу от устаревших индексов
        while self.number_to_indices[number] and self.number_to_indices[number][0] not in self.valid_entries[number]:
            heapq.heappop(self.number_to_indices[number])

        # Возвращаем минимальный индекс или -1, если его нет
        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1
 


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)