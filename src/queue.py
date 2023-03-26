from src.node import Node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head: Node | None = None
        self.tail: Node | None = None

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next_node = node
            self.tail = node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next_node
        return data

    def __str__(self):
        """Магический метод для строкового представления объекта"""
        head = self.head
        data = []
        while head:
            data.append(head.data)
            head = self.head.next_node
        return '\n'.join(data)
