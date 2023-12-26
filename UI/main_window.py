import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit
from app.chat_logic.get_chat_response import get_chat_response

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle('Escapa Chatbot')
        self.setGeometry(100, 100, 600, 400)

        # Chat history area
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        self.chat_history.setGeometry(10, 10, 580, 300)

        # User input area
        self.user_input = QLineEdit(self)
        self.user_input.setGeometry(10, 320, 580, 40)
        self.user_input.returnPressed.connect(self.sendMessage)  # Connect signal to function

    def sendMessage(self):
        user_message = self.user_input.text()
        self.user_input.clear()

        # Display user's message
        self.chat_history.append(f"You: {user_message}")

        # Use the centralized chat logic for the response
        chatbot_response = get_chat_response(user_message)
        self.chat_history.append(f"Escapa: {chatbot_response}")

# The code below is the standard boilerplate for running a PyQt application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
