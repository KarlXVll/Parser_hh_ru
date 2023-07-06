from PyQt5.QtCore import QThread, pyqtSignal
import telegram

class TelegramThread(QThread):
    message_sent = pyqtSignal(str)

    def __init__(self, token, chat_id):
        super().__init__()
        self.token = token
        self.chat_id = chat_id

    def run(self):
        bot = telegram.Bot(token=self.token)
        message = 'Найдены новые вакансии!'
        try:
            bot.send_message(chat_id=self.chat_id, text=message)
            self.message_sent.emit('Уведомление отправлено в телеграм!')
        except telegram.error.TelegramError as e:
            self.message_sent.emit(f'Ошибка отправки уведомления: {e}')
