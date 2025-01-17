# Лабораторная работа 7. Использование шаблона «Наблюдатель»

### Цель работы
Необходимо создать программу на языке Python, которая использует паттерн проектирования "Наблюдатель" для отслеживания изменений курсов валют через API Центробанка РФ. Программа должна запрашивать курсы валют и уведомлять зарегистрированных наблюдателей о изменении курсов в реальном времени или через заданные интервалы времени.
Структура реализованного задания должна представлять

Объект — веб-сервер Flask или FastAPI, Tornado.
Наблюдатели - клиенты, представляющие HTML-страницы, связывающиеся с объектом с помощью веб-сокетов. На странице должен отображаться идентификатор клиента.

### Реализация
Веб-сервер Flask

# Результат
Интерфейс наблюдателя:
![alt text](image.png)

Фиксация подключения:
![alt text](image-1.png)

Фиксация подписки:
![alt text](image-2.png)

Получеие курса:
![alt text](image-3.png)