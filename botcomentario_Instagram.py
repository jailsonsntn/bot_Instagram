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
        driver.get("https://www.instagram.com")
        time.sleep(10)
        campo_usuario = driver.find_element_by_xpath(
            "//input[@name='username']")
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        time.sleep(4)
        campo_senha = driver.find_element_by_xpath(
            "//input[@name='password']")
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        campo_senha.send_keys(Keys.RETURN)
        time.sleep(8)
        self.comente_nas_fotos('')  # Local para inserir Hashtag

    @staticmethod
    def digite_humano(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1, 5)/30)

    def comente_nas_fotos(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        for i in range(1, 3):
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)

        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + 'fotos' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script(
                'window.scrollTo(0, document.body.scrollHeight);')
            try:
                comentarios = [
                    "Quer ganhar + seguidores?  Me chama!", "Afim de mais seguidores? Me chama!", "Quer dobrar o número de seguidores? Me chama!"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(5, 8))
                self.digite_humano(random.choice(
                    comentarios), campo_comentario)
                time.sleep(random.randint(40, 120))
                driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]").click()
                time.sleep(8)
            except Exception as e:
                print(e)
                time.sleep(8)


# Inserir Usuario e Senha
jailsonBot = InstagramBot('', '')
jailsonBot.login()
