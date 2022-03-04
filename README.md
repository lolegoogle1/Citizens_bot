# Inform_bot

Цей бот створений для протидії дезінформації та ДРГ російської федерації в Україні.
Основне призначення бота:
Надсилати інформацію про підозрілих осіб, мітку, розкрадання майна до  відповідних оганів.

Що потрібно мати для використання Бота?
  1. Telegram API TOKEN: ось посилання на інформацію про те як його можна отримати https://leagueofchatbots.com/blog-3/yak-otrymaty-api-token-bota-v-telegram
  2. ID каналу адміністратора для отримання інформації від користувачів.
        *Детальніше по цьому пункту:
          1. Створіть власний приватний канал у телеграмі;
          2. Додатйте бота у цей канал;
          3. Виконайте інструкції з фото ![image](https://user-images.githubusercontent.com/91202498/156794424-3604cb3a-f54e-404b-ac7c-39888585dc00.png);
  3. Python 3.7+;
  4. Бажання;

--------------------------------------------------------------------------------------------------------------------------------------------------------------

### Завантажте PYTHON для Windows з офіційної сторінки та Встановіть його.
УВАГА! При встановленні ОБОВ'ЯЗКОВО поставте галочку у пункті "ADD PYTHON to PATH" \
Посилання: https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe
--------------------------------------------------------------------------------------------------------------------------------------------------------------


Встановлення бота та налаштування бота(Windows):\
&nbsp;&nbsp;&nbsp;&nbsp;1. Створити віртуальне середовище:\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Натискаєте комбінацію клавіш WIN+R; В полі для вводу пишете "cmd";\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Створюєте папку для бота, за допомогою команди "mkdir".\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Наприклад: якщо ви хочете назвати папку "Test" - використайте команду "mkdir Test";\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(Назву для папки пишіть без пробілів та латиницею.) \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Переходите в папку через команду, де збираєтесь зберігати ваш проект \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"cd <тут введіть назву папки, яку ви створили>" \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Приклад: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"cd Test"; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Введіть команду "pip install virtualenv" \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*Тепер створіть віртуальне середовище за допомогою команди "virtualenv venv" \
&nbsp;&nbsp;&nbsp;&nbsp;2. Активуйте віртуальне середовище командою - ".\venv\Scripts\activate". \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Після активації зліва має з'явитись надпис "(venv)" - це означає, що серидовище успішно &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;активовано. \
&nbsp;&nbsp;&nbsp;&nbsp;3. Тепер скачайте проект за допомогою наступних команд: \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Скачайте архів за цим посиланням та розпакуйте його в папку для бота.\
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;У нашому  прикладі це папка "Test"; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Якщо ви знайомі з системою GIT: "git clone https://github.com/lolegoogle1/Inform_bot.git"; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Перейдіть в папку, використовуючи командну стрічку, за допомогою команди - "cd"; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Введіть команду, шоб встановити всі потрібні модулі для функціонування бота. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Команда "pip install -r requirements.txt"; \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5. Відкрийте файл "creds.py" та вставте свій TELEGRAM_API_KEY, та ADMIN_CHANNEL_ID. \
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Дивіться як отримати в розділі "Що потрібно мати для використання Бота?";
    
Запуск Бота: \
&nbsp;&nbsp;&nbsp;&nbsp;1. За допомогою команди "cd" зайдіть в папку, де розсташований файл "bot_main.py"; \
&nbsp;&nbsp;&nbsp;&nbsp;2. Запустіть бота за допомогою команди "python3 bot_main.py"
    
    



