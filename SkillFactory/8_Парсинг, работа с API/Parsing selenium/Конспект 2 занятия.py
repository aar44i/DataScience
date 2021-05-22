<h1 id="firstHeading" class="firstHeading" lang="en">S7 Airlines</h1> ## Тег заголовка первого уровня <h1>. Сам заголовок - S7 Airlines. Тег имеет атрибуты id="firstHeading", class="firstHeading", а также lang="en"

## Тег <h1> сидит внутри тега <div>. <div> - это невидимый блок (контейнер), в который можно сажать элементы страницы. Так ими проще управлять при вёрстке (располагать друг относительно друга целые куски страницы, а не каждый элемент в отдельности)
<div id="content" class="mw-body">
	<h1 id="firstHeading" class="firstHeading" lang="en">S7 Airlines</h1> 
</div>

from selenium import webdriver ## Из библиотеки selenium импортируем подбиблиотеку webdriver
driver = webdriver.Chrome("c:/Python27/ArcGIS10.2/chromedriver.exe") ## Запускаем драйвер Google Chrome, который будет автотизированно управлять браузером и имитировать наши действия в нём.
driver.get("https://en.wikipedia.org/wiki/S7_Airlines") ## Зашли на страницу с адресом https://en.wikipedia.org/wiki/S7_Airlines

## Метод find_element_by возвращает ПЕРВЫЙ ПО СЧЁТУ элемент с заданными свойствами (названием тега, классом, id ...). Нам вернётся объект.
title = driver.find_element_by_id('firstHeading') ##Со страницы считали элемент с id = 'firstHeading'
title = driver.find_element_by_class_name('firstHeading') ##Со страницы считали элемент с class = 'firstHeading'
title = driver.find_element_by_xpath("//h1[@class='firstHeading']") ##Со страницы считали тег <h1>, у которого class = 'firstHeading'
print(title.text) ##Получили текст элемента
print(title.get_attribute("class")) ##Получили значение класса элемента
print(title.get_attribute("id")) ##Получили значение id элемента

## Метод find_elements_by возвращает СПИСОК ВСЕХ элементов с заданными свойствами (названием тега, классом, id ...). Нам вернётся список объектов.
title = driver.find_elements_by_id('firstHeading') ##Со страницы считали элементы с id = 'firstHeading'
title = driver.find_elements_by_class_name('firstHeading') ##Со страницы считали элементы с class = 'firstHeading'
title = driver.find_elements_by_xpath("//h1[@class='firstHeading']") ##Со страницы считали теги <h1>, у которых class = 'firstHeading'
print(title[0].text) ##Получили тескт нулевого элемента списка
print(title[0].get_attribute("class")) ##Получили значение класса элемента
print(title[0].get_attribute("id")) ##Получили значение id элемента

##Прописываем относительный путь к искомому элементу страницы. Считываем тег <h1> с классом 'firstHeading', который лежит внутри тега <div> с id = 'content'
title = driver.find_elements_by_xpath("//div[@id='content']/h1[@class='firstHeading']")

##Считываем вторую по счёту таблицу на странице городов Украины. Находим <table> с классом 'wikitable sortable jquery-tablesorter' и обращаемся к ней.
# В пути к элементу можем прописывать индексы. В данном случае будет индекс [2] , т.к. нас интересует 2 по счёту таблица.
table = driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][2]")

##Считываем вторую ячейку каждой строки таблицы. В таблице table проваливаемся в тело таблицы <tbody>, в нём обращаемся к строке таблицы <tr> и из неё вытаскиваем вторую по счёту ячейку <td>
rows = driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][2]/tbody/tr/td[2]")

## Нам вернулся список из объектов считанных нами ячеек. Можно проверить его длину
print(len(rows))

## Напечатаем то, что мы считали
for elem in range(len(rows)):
	print(rows[elem].text)
	
## Также можно очистить считанные значения	от ненужных символов. Это можно сделать путём разбиения строковой переменной на части по набору символов
print(rows[elem].text.split("\n")[0].split("[")[0]) ## Сначала разделили по "\n" и взяли левую часть от того, что разбилось, а затем её поделили по символу "[" и от того, на что эта строка развалилась взяли левую часть (нулевой элемент)

## Напечатаем считанные ячейки таблицы, очищенные от "мусора"
for elem in range(len(rows)):
	print(rows[elem].text.split("\n")[0].split("[")[0])
	
	
## теперь считаем колонку с названиям городов и датами их основания. Полученные значения запишем в списки
cities = []
names = driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][2]/tbody/tr/td[2]")
for elem in range(len(names)):
	cities.append(names[elem].text)

years = []
found = driver.find_elements_by_xpath("//table[@class='wikitable sortable jquery-tablesorter'][2]/tbody/tr/td[6]")
for elem in range(len(found)):
	years.append(found[elem].text)
	
	
## В файл "G:/Python 2020/Cities.csv" записали содержимое списков cities и years. 
with open("G:/Python 2020/Cities.csv",'w') as out:
	for x in range(len(tds)):
		out.write(cities[x].text+";")## ";" - разделитель столбцов
		out.write(years[x].text+"\n")## "\n" - перенос на новую строку