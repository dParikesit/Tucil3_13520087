def takeCost(elem):
    return elem[2],elem[1]


class PriorityQueue(object):
    def __init__(self):
        self.queue = []
        self.count = 0

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def simpulCount(self):
        return self.count

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)
        self.queue.sort(key=takeCost)
        self.count += 1
        

    # for popping an element based on Priority
    def pop(self):
        item = self.queue[0]
        del self.queue[0]
        return item