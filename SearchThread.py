from PyQt5.QtCore import QThread, pyqtSignal
import requests
from bs4 import BeautifulSoup

class SearchThread(QThread):
    vacancy_found = pyqtSignal(str, str, str)

    def __init__(self, keywords):
        super().__init__()
        self.keywords = keywords

    def run(self):
        url = 'https://hh.ru/search/vacancy'
        params = {'text': self.keywords}
        response = requests.get(url, params=params)

        soup = BeautifulSoup(response.text, 'html.parser')
        vacancies = soup.find_all('div', {'class': 'vacancy-serp-item'})

        for vacancy in vacancies:
            title = vacancy.find('a', {'class': 'bloko-link'}).text
            company = vacancy.find('a', {'class': 'bloko-link bloko-link_secondary'}).text
            salary = vacancy.find('div', {'class': 'vacancy-serp-item__compensation'})
            if salary:
                salary = salary.text
            else:
                salary = 'Не указано'
            self.vacancy_found.emit(title, company, salary)
