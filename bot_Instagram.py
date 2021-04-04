from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(
            executable_path=r"D:\geckodriver\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(10)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(5)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        time.sleep(8)
        self.curtir_fotos('')  # Local para inserir Hashtag

    # Digitar como humano para não dar bug

    @staticmethod
    def digite_humano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    def curtir_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)
        for i in range(1, 3):
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            time.sleep(5)
            driver.get(pic_href)
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            try:
                # Seguir
                time.sleep(5)
                btn_seguir = driver.find_element_by_class_name('bY2yH')
                btn_seguir.click()
                # Curtidas
                time.sleep(5)
                btn_curtir = driver.find_element_by_class_name(
                    'fr66n')
                btn_curtir.click()
                time.sleep(3)
                # Comentarios
                comentarios = [
                    "Feliz Páscoa!"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(5, 8))
                self.digite_humano(random.choice(
                    comentarios), campo_comentario)
                time.sleep(random.randint(40, 120))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]").click()
                time.sleep(19)
            except Exception as e:
                time.sleep(5)


# Inserir Usuario e Senha
jailsonBot = InstagramBot('', '')
jailsonBot.login()
