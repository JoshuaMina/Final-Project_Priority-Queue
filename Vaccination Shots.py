# During the surge of COVID-19 pandemic, the local government of Taytay, Rizal is Administering
# COVID-19 vaccine shots for the first 50 people in line. Given the circumstance the LGU should
# give prioritization to Senior Citizen, Persons with Disability and Frontline workers respectively.
# The line should only accomodate 5 people at a time because of covid restrictions in the municipality.
# Create a Program that will help to distribute vaccine effectively.



class Builder:
    def __init__(self, data, ority):
        self.data = data
        self.ority = ority


class PriorityQueue:
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





pq = PriorityQueue()
k = 0

while (pq.size()<=5):

    k += 1
    while True:
        try:
            user = ""
            name = input("Enter the name of patient: ").capitalize()
            age = int(input("Enter his/her age: "))
            status = input("Enter the his/her status: ")
        except TypeError:
            print("Invalid Input")
        else:
            special = input("Are you Senior Citizen (SC), Persons with Disability (PWD) and Frontliner workers (FW) otherwise type NO : ").upper()
            if special == "FW":
                prio = "1"
            elif special == "SC":
                prio = "2"
            elif special == "PWD":
                prio = "3"
            else:
                prio = "4"
            user = Builder(dict(patientNo= k,name=name, age=age, status=status),prio)
            pq.insert(user)
            pq.show()
            print(pq.size())

#
#
# b1 = Builder("C", "3")
# b2 = Builder("D", "1")
# b3 = Builder("B", "2")
# b4 = Builder("A", "4")
#
# pq = PriorityQueue()
# pq.insert(b1)
# pq.insert(b2)
# pq.insert(b3)
# pq.insert(b4)
#
# print("After insertion")
# pq.show()
#
# pq.delete()
#
# print("After deleting one element.")
# pq.show()
# print(pq.size())
