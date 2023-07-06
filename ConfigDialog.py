from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QVBoxLayout

class ConfigDialog(QDialog):
    def __init__(self, keywords, token, chat_id):
        super().__init__()
        self.keywords = keywords
        self.token = token
        self.chat_id = chat_id
        self.setWindowTitle('Настройки')
        self.setFixedSize(300, 150)

        self.keywords_label = QLabel('Ключевые слова:')
        self.keywords_edit = QLineEdit(self.keywords)

        self.token_label = QLabel('Токен бота телеграм:')
        self.token_edit = QLineEdit(self.token)

        self.chat_id_label = QLabel('ID чата телеграм:')
        self.chat_id_edit = QLineEdit(self.chat_id)

        self.save_button = QPushButton('Сохранить')
        self.save_button.clicked.connect(self.accept)

        layout = QVBoxLayout()
        layout.addWidget(self.keywords_label)
        layout.addWidget(self.keywords_edit)
        layout.addWidget(self.token_label)
        layout.addWidget(self.token_edit)
        layout.addWidget(self.chat_id_label)
        layout.addWidget(self.chat_id_edit)
        layout.addWidget(self.save_button)
        self.setLayout(layout)

    def get_keywords(self):
        return self.keywords_edit.text()

    def get_token(self):
        return self.token_edit.text()

    def get_chat_id(self):
        return self.chat_id_edit.text()