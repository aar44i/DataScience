{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Необходимо написать функцию, которая принимает на вход 2 аргумента: логин и пароль. По ним функция будет авторизироваться на mail.ru (можно взять и другую почту, если больше нравится), а именно, вводить логин, пароль, снимать галочку \"Запомнить пользователя\" и нажимать кнопку \"Войти\"."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "NoSuchElementException",
     "evalue": "Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"passp-field-passwd\"]\"}\n  (Session info: chrome=83.0.4103.97)\n",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNoSuchElementException\u001b[0m                    Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-38ee0c3d232a>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     18\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     19\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 20\u001b[1;33m \u001b[0mpswd\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"passp-field-passwd\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     21\u001b[0m \u001b[0mpswd\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msend_keys\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"272551981Ar\"\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     22\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element_by_id\u001b[1;34m(self, id_)\u001b[0m\n\u001b[0;32m    358\u001b[0m             \u001b[0melement\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdriver\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'foo'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    359\u001b[0m         \"\"\"\n\u001b[1;32m--> 360\u001b[1;33m         \u001b[1;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfind_element\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mID\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mid_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    361\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    362\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_elements_by_id\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mid_\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mfind_element\u001b[1;34m(self, by, value)\u001b[0m\n\u001b[0;32m    976\u001b[0m         return self.execute(Command.FIND_ELEMENT, {\n\u001b[0;32m    977\u001b[0m             \u001b[1;34m'using'\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 978\u001b[1;33m             'value': value})['value']\n\u001b[0m\u001b[0;32m    979\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    980\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0mfind_elements\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mby\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mBy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mID\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;32mNone\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\u001b[0m in \u001b[0;36mexecute\u001b[1;34m(self, driver_command, params)\u001b[0m\n\u001b[0;32m    319\u001b[0m         \u001b[0mresponse\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcommand_executor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mdriver_command\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mparams\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    320\u001b[0m         \u001b[1;32mif\u001b[0m \u001b[0mresponse\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 321\u001b[1;33m             \u001b[0mself\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0merror_handler\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mcheck_response\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresponse\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    322\u001b[0m             response['value'] = self._unwrap_value(\n\u001b[0;32m    323\u001b[0m                 response.get('value', None))\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\u001b[0m in \u001b[0;36mcheck_response\u001b[1;34m(self, response)\u001b[0m\n\u001b[0;32m    240\u001b[0m                 \u001b[0malert_text\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mvalue\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;34m'alert'\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mget\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'text'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    241\u001b[0m             \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malert_text\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m--> 242\u001b[1;33m         \u001b[1;32mraise\u001b[0m \u001b[0mexception_class\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mmessage\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mscreen\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mstacktrace\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m    243\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m    244\u001b[0m     \u001b[1;32mdef\u001b[0m \u001b[0m_value_or_default\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mself\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mobj\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mkey\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdefault\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNoSuchElementException\u001b[0m: Message: no such element: Unable to locate element: {\"method\":\"css selector\",\"selector\":\"[id=\"passp-field-passwd\"]\"}\n  (Session info: chrome=83.0.4103.97)\n"
     ]
    }
   ],
   "source": [
    "from selenium import webdriver\n",
    "\n",
    "# def authorization (login, passsword):\n",
    "\n",
    "driver = webdriver.Chrome()\n",
    "driver.get(\"https://passport.yandex.ru/auth/add?from=mail&origin=hostroot_homer_auth_L_ru&retpath=https%3A%2F%2Fmail.yandex.ru%2F&backpath=https%3A%2F%2Fmail.yandex.ru%3Fnoretpath%3D1\")\n",
    "\n",
    "lg = driver.find_element_by_id(\"passp-field-login\")\n",
    "lg.send_keys(\"aar44i@yandex.ru\")\n",
    "\n",
    "\n",
    "button_lg = driver.find_element_by_xpath(\"//button[@class='control button2 button2_view_classic button2_size_l button2_theme_action button2_width_max button2_type_submit passp-form-button']\")\n",
    "button_lg.click()\n",
    "\n",
    "# window_before = driver.window_handles[0]\n",
    "# window_after = driver.window_handles[1]\n",
    "# driver.switch_to.window(window_after)\n",
    "\n",
    "    \n",
    "pswd = driver.find_element_by_id(\"passp-field-passwd\")\n",
    "pswd.send_keys(\"\")\n",
    "\n",
    "button_pswd = driver.find_element_by_xpath(\"//button[@type='submit']\")\n",
    "button_pswd.click()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
