import time
import random
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

query = input("Введите поисковый запрос: ")

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org")

assert "Википедия" in browser.title

search_box = browser.find_element(By.ID, 'searchInput')
search_box.send_keys(query.strip())
search_box.send_keys(Keys.RETURN)
time.sleep(3)

while True:
    print("\nВыберите действие:")
    print("1. Листать параграфы текущей статьи")
    print("2. Перейти на одну из связанных страниц")
    print("3. Выйти из программы")

    choice = input("Ваш выбор: ")

    if choice == '1':
        paragraphs = browser.find_elements(By.TAG_NAME, 'p')
        for paragraph in paragraphs:
            print(paragraph.text)
            input()
    elif choice == '2':
        hatnotes = []
        for element in browser.find_elements(By.TAG_NAME, "div"):
            cl = element.get_attribute("class")
            if cl == "mw-search-result-heading":
                hatnotes.append(element)

        hatnote = random.choice(hatnotes)
        link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
        browser.get(link)
    elif choice == '3':
        print('Выход из программы.')
        break
    else:
        print("Неверный выбор, попробуйте снова.")

browser.quit()