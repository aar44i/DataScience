import os, shutil

os.mkdir("G:/Python 2020/flrd") ## Создали новую папку fldr в папке G:/Python 2020
os.listdir("G:/Python 2020/flrd") ## Получили содержимое папки fldr. Нам вернётся список элементов, находящихся в папке
os.rmdir("G:/Python 2020/flrd") ## Удалили новую папку fldr в папке G:/Python 2020. Так можно удалить только пустую папку
shutil.rmtree("G:/Python 2020/flrd") ## Удалили папку fldr вместе со всем её содержимым.
os.path.exists("G:/Python 2020/flrd") ## Проверили существование папки fldr в папке G:/Python 2020. Нам вернётся True, если папка существует и False, если её там нет.


## Считали файл Ukraine cities.csv и записали его в переменную table. Теперь table - это список из строк нашей таблицы.
with open("G:/Python 2020/Ukraine cities.csv",'r') as out:
	table = out.readlines()


import datetime	

some_date = datetime.date(2020, 5, 22) ## Создаём объект date. В него передаём дату - 22 мая 2020 г.
some_time = datetime.datetime(2020, 5, 22, 4, 20, 0) ## Создаём объект datetime. В него передаём точное время - 4 ч. 20 мин. 0 сек. 22 мая 2020 г.
today = datetime.date.today() ## Получаем дату сегодняшнего дня. Результат операции - объект datetime
now = datetime.datetime.now() ## Аналогично, можно получить текущий момент времени с точностью до милисекунд
formated_today = datetime.date.today().strftime("%Y-%m-%d") ## Отформатировали дату сегодняшнего дня в виде гггг-мм-дд
now.strftime("%H:%M:%S") ## Отформатировали текущий момент времени в виде чч-мм-сс
tomorrow = today + datetime.timedelta(1) ## узнали дату завтрашнего дня, прибавив к сегодняшнему дню дельту в 1 день.

## Получаем разницу во времени между двумя моментами: start и end
start = datetime.datetime.now()
end = datetime.datetime.now()
difference = str(end - start) ## Разница между двумя моментами с точностью до милисекунд
difference = (end - start).seconds ## Число секунд, составляющих разницу между моментами end и start

## В список dates записываем даты следующих 10 дней после сегодняшнего и форматируем эти даты в виду дд.мм.гггг
dates = []
for x in range(10):
	next = today + datetime.timedelta(x+1)
	dates.append(next.strftime("%d.%m.%Y"))
