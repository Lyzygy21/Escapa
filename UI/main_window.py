import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Escapa Chatbot')
        self.setGeometry(100, 100, 600, 400)  # X position, Y position, Width, Height

        # Chat history area
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)  # Make the text area read-only
        self.chat_history.setGeometry(10, 10, 580, 300)  # X, Y, Width, Height

        # User input area
        self.user_input = QLineEdit(self)
        self.user_input.setGeometry(10, 320, 580, 40)  # X, Y, Width, Height

# The code below is the standard boilerplate for running a PyQt application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
