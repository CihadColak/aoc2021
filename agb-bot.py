# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# options = Options()
# options.headless = True
# driver = webdriver.Firefox(options=options,executable_path=r'/home/jinothan/CLionProjects/cclogger-id3-data-visualization/src/dataVisualisation/geckodriver')
# driver.get("https://reservierung.zlb.de/klavier/")
# reservedElems = []
# for elem in driver.find_elements_by_xpath('.//a[@class="event  available"]'):
#     reservedElems.append(elem)

# for available_elem in reservedElems:
#     print(available_elem.text)
#     eventAvailable = available_elem.find_elements_by_xpath('./span[@class="event-time"]')
#     date = eventAvailable[0].get_attribute("data-time")
#     print(date)
import requests
inp = requests.get('https://reservierung.zlb.de/klavier/').text
print("event  available" in inp)
