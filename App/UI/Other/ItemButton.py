from PyQt5.QtWidgets import QPushButton


class ItemButton(QPushButton):
    def __init__(self, func, data):
        super(ItemButton, self).__init__(None)
        self.data = data
        self.setAcceptDrops(True)
        self.clicked.connect(lambda: func(self.data))
