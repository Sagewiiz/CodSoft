import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class TodoApp(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Todo App")
        self.setFixedSize(400, 500)
        
        self.setAutoFillBackground(True)
        p = self.palette()
        p.setColor(self.backgroundRole(), QColor('#81c784'))
        self.setPalette(p)

        self.titleLabel = QLabel("My Todo List")
        self.titleLabel.setAlignment(Qt.AlignCenter) 
        self.titleLabel.setStyleSheet("font-size: 24px; font-weight: bold; color: #fff;")
        
        self.inputBox = QLineEdit()
        self.inputBox.setStyleSheet("background: #fff; border: 2px solid #444; border-radius: 5px; padding: 5px;")
        
        self.addButton = QPushButton("Add") 
        self.addButton.setStyleSheet("background: #303f9f; color: #fff; border: none; padding: 10px; border-radius: 5px;")
        
        self.updateButton = QPushButton("Update")
        self.updateButton.setStyleSheet("background: #ff4081; color: #fff; border: none; padding: 10px; border-radius: 5px;")

        self.todoList = QListWidget()
        self.todoList.setStyleSheet("background: #fff; border-radius: 5px; padding: 10px;")
        
        self.mainLayout = QVBoxLayout()
        self.buttonLayout = QHBoxLayout()
        
        self.mainLayout.addWidget(self.titleLabel)
        self.mainLayout.addWidget(self.inputBox)
        
        self.buttonLayout.addWidget(self.addButton)
        self.buttonLayout.addWidget(self.updateButton)
        
        self.mainLayout.addLayout(self.buttonLayout)
        self.mainLayout.addWidget(self.todoList)
        
        self.setLayout(self.mainLayout)

        self.addButton.clicked.connect(self.addTodo)  
        self.updateButton.clicked.connect(self.updateTodo)

    def addTodo(self):
        text = self.inputBox.text() 
        item = QListWidgetItem(text)
        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
        item.setCheckState(Qt.Unchecked)  
        self.todoList.addItem(item)
        self.inputBox.clear()

    def updateTodo(self):
        curItem = self.todoList.currentItem()
        if curItem:
            text = self.inputBox.text()
            curItem.setText(text)
            self.inputBox.clear()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TodoApp()
    window.show()
    app.exec()
