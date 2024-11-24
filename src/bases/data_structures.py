

my_list = [1, 2, 3, 4]
my_list.append(5)  # Add an element
my_list.pop()      # Remove the last element


my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3  # Add a key-value pair
print(my_dict.get('a'))  # Safe key lookup



my_set = {1, 2, 3}
my_set.add(4)  # Add an element
my_set.remove(2)  # Remove an element



from collections import deque
queue = deque()
queue.append(1)  # Enqueue
queue.popleft()  # Dequeue


import heapq
pq = []
heapq.heappush(pq, (1, 'task1'))
heapq.heappop(pq)  # Pop the highest-priority item



from collections import defaultdict
graph = defaultdict(list)
graph['A'].append('B')  # Add edge


from collections import Counter
counts = Counter([1, 1, 2, 3])
print(counts)