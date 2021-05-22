from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os, time, datetime
driver = webdriver.Chrome(r"C:\Python27\ArcGIS10.2\chromedriver.exe")

## Объявляем константы
origins = ["Москва"]
destinations = ["Сочи"]
today = datetime.datetime.today()
directory = "G:/Python 2020/Monitoring/"
airp_dict = {"Москва": "VKO", "Сочи": "AER"}

## Создаём структуру папок и файлов под мониторинг
if not os.path.exists(directory):
	os.mkdir(directory)
	os.mkdir(directory + "/LOG")
	with open (directory + "/LOG/durations.csv",'w') as out:
		out.write("Дата промера;Время итерации\n")

for elem in range(len(origins)):
	route = origins[elem]+" - "+ destinations[elem]	
	if not os.path.exists(directory+route):
		os.mkdir(directory+route)
		with open (directory+route+"/data.csv",'w') as out:
			out.write("Дата промера;Дата вылета;Время вылета;Время прилёта;Цена\n")

## Определяем глубину мониторинга и высчитываем даты
dates = []
for x in range(10):
	next_date = today + datetime.timedelta(x+1)
	dates.append(next_date)
	
## Функция, которая обрабатывает рейсы на конкретную дату
def pobeda_active_day(origin, destination, date):
	origin = airp_dict[origin]
	destination = airp_dict[destination]
	route = origin + " - " + destination	
	driver.get("https://www.pobeda.aero/ru/booking/select/?origin1="+origin+"&destination1="+destination+"&departure1="+date+"&adt1=1&tng1=0&chd1=0&inf1=0&currency=RUB")
	time.sleep(2)
	prices = driver.find_elements_by_xpath("//div[@class='journey_price-currency']") ## Цена
	departure_time = driver.find_elements_by_xpath("//div[@class='journey-schedule_time journey-schedule_time-departure']") ## Время отправления
	arrival_time = driver.find_elements_by_xpath("//div[@class='journey-schedule_time journey-schedule_time-departure']") ## Время прибытия
	with open (directory+route+"/data.csv",'a') as out:
		for x in range(len(prices)):
			out.write(today.strftime("%Y-%m-%d") + ";")
			out.write(date + ";")			
			out.write(departure_time[x].text + ";")
			out.write(arrival_time[x].text + ";")
			out.write(prices[x] + "\n")

			
## Запускаем мониторинг. Проходимся по направлениям и датам и запускаем нашу функцию. 
## За одно посчитаем, сколько времени уходит на обработу одного дня и запишем эту информацию в log-файл
for e in range(len(origins)):
	for elem in range(len(dates)):
		start = datetime.datetime.now()
		pobeda_active_day(origins[e], destinations[e], dates[elem].strftime("%Y-%m-%d"))
		end = datetime.datetime.now()
		duration = str(end - start)
		with open (directory + "/LOG/durations.csv",'a') as log:
			log.write(today.strftime("%Y-%m-%d") + ";")
			log.write(duration + "\n")
			
## Мониторинг завершён. Закрываем драйвер.			
driver.quit()