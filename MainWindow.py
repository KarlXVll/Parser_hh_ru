from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal
from SearchThread import SearchThread
from TelegramThread import TelegramThread
from ConfigDialog import ConfigDialog
from Logger import Logger

class MainWindow(QMainWindow):
    def __init__(self, keywords, token, chat_id):
        super().__init__()
        self.keywords = keywords
        self.token = token
        self.chat_id = chat_id
        self.setWindowTitle('Парсер вакансий')
        self.setFixedSize(600, 400)

        self.logger = Logger('log.txt')

        self.search_thread = SearchThread(self.keywords)
        self.search_thread.vacancy_found.connect(self.handle_vacancy_found)
        self.search_thread.finished.connect(self.handle_search_finished)

        self.telegram_thread = TelegramThread(self.token, self.chat_id)
        self.telegram_thread.message_sent.connect(self.handle_message_sent)

        self.vacancies_list = QListWidget()
        self.status_label = QLabel('Статус: ожидание')
        self.start_button = QPushButton('Старт')
        self.start_button.clicked.connect(self.handle_start_button_clicked)
        self.stop_button = QPushButton('Стоп')
        self.stop_button.clicked.connect(self.handle_stop_button_clicked)
        self.config_button = QPushButton('Настройки')
        self.config_button.clicked.connect(self.handle_config_button_clicked)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.config_button)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.vacancies_list)
        main_layout.addWidget(self.status_label)
        main_layout.addLayout(button_layout)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

    def handle_vacancy_found(self, title, company, salary):
        message = f'Найдена вакансия: {title} ({company}), зарплата: {salary}'
        self.logger.log(message)
        self.vacancies_list.addItem(message)

    def handle_search_finished(self):
        self.status_label.setText('Статус: завершено')

    def handle_message_sent(self, message):
        QMessageBox.information(self, 'Уведомление', message)

    def handle_start_button_clicked(self):
        self.vacancies_list.clear()
        self.status_label.setText('Статус: поиск вакансий...')
        self.search_thread.start()

    def handle_stop_button_clicked(self):
        if self.search_thread.isRunning():
            self.search_thread.terminate()
            self.status_label.setText('Статус: остановлено')

    def handle_config_button_clicked(self):
        dialog = ConfigDialog(self.keywords, self.token, self.chat_id)
        if dialog.exec_() == QDialog.Accepted:
            self.keywords = dialog.get_keywords()
            self.token = dialog.get_token()
            self.chat_id = dialog.get_chat_id()

    def closeEvent(self, event):
        if self.search_thread.isRunning():
            reply = QMessageBox.question(self, 'Предупреждение', 'Поиск вакансий все еще выполняется. Вы действительно хотите выйти?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.Yes:
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()
