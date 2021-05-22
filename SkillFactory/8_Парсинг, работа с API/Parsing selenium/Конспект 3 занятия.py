from selenium import webdriver
from selenium.webdriver.common.keys import Keys ## Подмодуль библиотеки Selenium, отвечающий за 
driver = webdriver.Chrome("c:/Python27/ArcGIS10.2/chromedriver.exe")

driver.get('https://www.aeroflot.ru/') ## Заходим на главную страницу авиакомпании Аэрофлот

button = driver.find_element_by_xpath("//label[@for='booking']") ##Нашли галочку "За мили" рядом с кнопкой "Найти" по тегу label С аттрибутом for='booking'.
button.click() ## С помощью метода .click() нажали на эту галочку

origin = driver.find_element_by_id("city-departure-0-booking") ##Нашли поле на странице по его ID. Это поле отвечает за ввод города отправления
origin.clear() ## С помощью метода .clear() очистили поле
origin.send_keys("Санкт-Петербург") ## с помощью метода .send_keys() записали в поле текстовое занчение "Санкт-Петербург"

destination = driver.find_element_by_id("city-arrival-0-booking") ##Аналогично находим поле города прибытия
destination.send_keys("Краснодар") ## с помощью метода .send_keys() записали в поле текстовое занчение "Краснодар"

body = driver.find_element_by_xpath("//body")## Получили всё тело нашей веб-страницы
body.send_keys(Keys.ENTER)## Передали веб-странице нажатие кнопки Enter. Этой командой мы имитируем нажатие на кнопку Enter, когда находимся на странице.

submit = driver.find_element_by_xpath("//button[@class='main-module__button main-module__button--wide main-module__button--lg']") ## Нашли кнопку "Найти билеты"
submit.click() ## Нажали на эту кнопку 
		
		
from urllib.request import urlretrieve ## Из библиотеки urllib импортировали подмодуль urlretrieve
driver.get("https://ru.wikipedia.org/wiki/%D0%93%D0%BE%D1%80%D0%BE%D0%B4%D0%B0_%D0%A3%D0%BA%D1%80%D0%B0%D0%B8%D0%BD%D1%8B") ## Вернёмся к городам Украины
image = driver.find_element_by_xpath("//img[@alt='Lesser Coat of Arms of Ukraine.svg']") ## Получили объект картинки - герба Украины
img_url = image.get_attribute("src") ## Получили аттрибут src считанного нами тега img. В аттрибуте src содержится ссылка на саму картинку в формате png
urlretrieve(img_url, "G:/Python 2020/img.jpg") ## с помощью импортированной функции urlretrieve сохраняем картинку по пути "G:/Python 2020/img.jpg"

import time ## импортируем библиотеку time
time.sleep(1) ## Задаём паузу в выполнении кода длительностью 1 сек.

driver.quit() ## Остановить работу драйвера и закрыть окно браузера