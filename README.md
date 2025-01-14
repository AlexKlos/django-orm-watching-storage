# Пульт охраны банка
Это внутренний репозиторий для сотрудников банка "Свияние". Если вы попали в этот репозиторий случайно, то вы не сможете его запустить, т.к. у вас нет доступа к БД, но можете свободно использовать код вёрстки или посмотреть, как реализованы запросы к БД.

Пульт охраны - это сайт, который можно подключить к удалённой базе данных с визитами и карточками пропуска сотрудников нашего банка.

## Установка и настройка

### 1. Клонирование репозитория

Склонируйте репозиторий на свой локальный компьютер:

```bash
git clone https://github.com/AlexKlos/django-orm-watching-storage.git
```

### 2. Установка зависимостей

Для работы приложения необходимо установить все зависимости. Убедитесь, что у вас установлен Python 3.8 или выше, затем выполните команду:

```bash
pip install --upgrade -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env` в папке `project` и добавьте в него следующие переменные окружения:

```bash
ENGINE=Движок_БД
HOST=Адрес_БД
PORT=Порт_БД
NAME=Имя_БД
USER=Имя_пользователя
PASSWORD=Пароль 
SECRET_KEY=Секретный_ключ
DEBUG=Режим_запуска # True - для отладки / False - в рабочем режиме
```

## Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).