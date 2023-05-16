
#1zadanie

class Element:
    def __init__(self, data=None, nextE=None):
        self.data = data
        self.nextE = nextE


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        if self.size == 0:
            return "Pusta lista"
        result = ""
        current = self.head
        while current:
            result += str(current.data) + " "
            current = current.nextE
        return result.strip()

    def get(self, e):
        current = self.head
        while current:
            if current.data == e:
                return current.data
            current = current.nextE
        return None

    def delete(self, e):
        if self.head is None:
            return "Brak elementow"

        if self.head.data == e:
            self.head = self.head.nextE
            self.size -= 1
            return

        prev = None
        current = self.head
        while current:
            if current.data == e:
                prev.nextE = current.nextE
                self.size -= 1
                if current == self.tail:
                    self.tail = prev
                return
            prev = current
            current = current.nextE

    def append(self, e, func=None):
        element = Element(e)

        if self.head is None:
            self.head = element
            self.tail = element
            self.size += 1
            return

        if func is None:
            func = lambda x, y: x >= y

        current = self.head
        prev = None
        while current and not func(current.data, e):
            prev = current
            current = current.nextE

        if prev is None:
            element.nextE = self.head
            self.head = element
        elif current is None:
            self.tail.nextE = element
            self.tail = element
        else:
            prev.nextE = element
            element.nextE = current

        self.size += 1


my_list = MyLinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(5)
my_list.append(15)
print(my_list) #cala lista

result = my_list.get(15)
print(result) #pobranie elementu 15
result1 = my_list.delete(10)

print(my_list) #usuniete jest 10