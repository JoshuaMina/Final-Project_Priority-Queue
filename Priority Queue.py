class Builder:
    def __init__(self, data, ority):
        self.data = data
        self.ority = ority


class PQueue:
    def __init__(self):
        self.q = list()

    def insert(self, node):
        if (self.size() == 0):
            self.q.append(node)
        else:
            for i in range(0, self.size()):
                if (node.ority >= self.q[i].ority):
                    if (i == (self.size() - 1)):
                        self.q.insert(i + 1, node)
                    else:
                        continue
                else:
                    self.q.insert(i, node)

    def show(self):
        for i in self.q:
            print("{} - {}".format(i.data, i.ority))

    def delete(self):
        return self.q.pop(0)

    def size(self):
        return len(self.q)


b1 = Builder("C", "3")
b2 = Builder("D", "1")
b3 = Builder("B", "2")
b4 = Builder("A", "4")

pq = PQueue()
pq.insert(b1)
pq.insert(b2)
pq.insert(b3)
pq.insert(b4)

print("After insertion")
pq.show()

pq.delete()

print("After deleting one element.")
pq.show()
