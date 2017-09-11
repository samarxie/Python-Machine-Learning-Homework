# 用节点类来实现双线链表
class Node(object):
    def __init__(self, value, p = 0):
        self.data = value
        self.next = p
        self.pre = p

class DoublelyLinkList(object):
    # 带下划线的应该是重载object超类
    def __init__(self):
        self.head = 0

    # def __getitem__(self, key):
    #
    # def __setitem__(self, key, value):

    # 特有函数
    def initlist(self, data):
        # 是我们在用的时候早再去确定data到底是什么类型。现在不用管那么多
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(data[i])
            p.next = node
            node.pre = p
            p = p.next

    def getlength(self):
        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        # 直接把头结点置为0
        self.head = 0

    def append(self, item):
        q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q
            q.pre = p

    def getitem(self, index):
    #     在这类函数时，往往要确定是不是空的链表
        if self.is_empty():
            print("该链表是空的")
            return
        j = 0
        p = self.head

        # 在确定范围的时候，要更加的充分
        while p.next != 0 and j < index:
            p = p.next()
            j += 1
        if j == index:
            return p.data
        else:
            print("目标不存在")

    def insert(self, index, item):
    #     往往一开始是需要判断的
        if self.is_empty() or index < 0 or index > self.getlength():
            print("链表为空")
            return

        if index == 0:
            q = Node(index, self.head)
            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            q = Node(item, p)
            post.next = q
            q.prev = post
            q.next = p
            p.pre = q

    def delete(self, index):
    # 一开始也是需要加入点判断的，为了程序的严谨性
        if self.is_empty() or index < 0 or index > self.getlength():
            print("链表为空")
            return

        if index == 0:
            # 值得商榷
            q = Node(item, self.head)

            self.head = q

        p = self.head
        post = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next
            p.next.prev = post

    def index(self, value):
        if self.is_empty():
            print("Linklist is empty.")
            return

        p = self.head
        i = 0
        # 这地方后面的判断not值得注意，而不是用 ！=0.这种强烈的判断符号
        while p.next != 0 and not p.data == value:
            p = p.next
            i += 1
        if p.data == value:
            return i
        else:
            return -1
