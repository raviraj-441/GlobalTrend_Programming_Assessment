class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def delete(self):
        if len(self.heap) > 1:
            self._swap(0, len(self.heap) - 1)
            max_val = self.heap.pop()
            self._heapify_down(0)
        elif self.heap:
            max_val = self.heap.pop()
        else:
            max_val = None
        return max_val

    def get_max(self):
        return self.heap[0] if self.heap else None

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        largest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] > self.heap[largest]:
            largest = left_child
        if right_child < len(self.heap) and self.heap[right_child] > self.heap[largest]:
            largest = right_child
        if largest != index:
            self._swap(index, largest)
            self._heapify_down(largest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

max_heap = MaxHeap()
max_heap.insert(10)
max_heap.insert(4)
max_heap.insert(15)
max_heap.insert(20)
print(max_heap.get_max())
print(max_heap.delete()) 
print(max_heap.get_max())
