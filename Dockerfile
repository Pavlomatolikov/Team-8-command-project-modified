# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.10
FROM python:3.10.5

MAINTAINER Pavlo Matolikov pavlomatolikov@gmail.com

# Установим переменную окружения
ENV APP_HOME /assistant

# Установим рабочую директорию внутри контейнера
WORKDIR $APP_HOME

# Скопируем остальные файлы в рабочую директорию контейнера
COPY . .

# Установим зависимости внутри контейнера
RUN pip install -r requirements.txt

# Установим приложение
RUN pip install .

# Запустим наше приложение внутри контейнера
CMD ["smart-bot"]