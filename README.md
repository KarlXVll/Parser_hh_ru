# Парсер вакансий

Программа-парсер для сайта hh.ru, которая ищет вакансии по заданным ключевым словам и отправляет уведомления в телеграм.

# Установка

Склонируйте репозиторий:
git clone https://github.com/KarlXVll/Parser_hh_ru.git

Установите зависимости:
pip install -r requirements.txt

# Использование

Запустите программу:
python main.py

Введите ключевые слова для поиска вакансий в поле "Ключевые слова" и нажмите кнопку "Старт".
Программа начнет искать вакансии по заданным ключевым словам на сайте hh.ru.
Когда программа найдет новую вакансию, она добавит ее в список найденных вакансий.
Если вы хотите остановить поиск вакансий, нажмите кнопку "Стоп".
Если вы хотите изменить настройки программы, нажмите кнопку "Настройки" и введите новые значения.

# Настройки
Вы можете изменить настройки программы, нажав кнопку "Настройки". В окне настроек вы можете изменить следующие параметры:

Ключевые слова для поиска вакансий
Токен бота телеграм
ID чата телеграм

# Логирование

Программа записывает логи работы в файл log.txt. В этом файле вы можете увидеть все найденные вакансии и ошибки, которые могут возникнуть при работе программы.

# Лицензия

Этот проект распространяется под лицензией MIT. Подробную информацию смотрите в файле LICENSE.
