from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from help import sanitizarPalabra, transformDate

def sendForm(array):
    #Use Firefox por que el chrome se me abre y se cierra no queda abierto, lei que puede ser un tema de version.
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://roc.myrb.io/s1/forms/M6I8P2PDOZFDBYYG")

    #Encontrar elementos con xpath
    dicProcess={'operaciones':"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[1]","cuentas":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[2]","riesgo":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[3]","ti":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[4]","financiero":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[5]","continuidad":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[6]","contabilidad":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[8]","gobierno":"/html/body/div/div/div/form/div/div[1]/div/div[3]/div/select/option[9]"}
    dicSeveridad={"alto":'//*[@id="severidad"]/option[1]',"medio":'//*[@id="severidad"]/option[2]',"bajo":'//*[@id="severidad"]/option[3]'}
    time.sleep(5)


    for i in array:
        driver.find_element(By.XPATH,'//*[@id="tipo_riesgo"]').clear()
        driver.find_element(By.XPATH,'//*[@id="date"]').clear()
        driver.find_element(By.XPATH,'//*[@id="res"]').clear()
        driver.find_element(By.XPATH,'//*[@id="obs"]').clear()
        driver.find_element(By.XPATH, dicProcess[sanitizarPalabra(i[0])]).click()
        driver.find_element(By.XPATH, dicSeveridad[sanitizarPalabra(i[3])]).click()
        driver.find_element(By.XPATH,'//*[@id="tipo_riesgo"]').send_keys(i[2])
        driver.find_element(By.XPATH,'//*[@id="res"]').send_keys(i[6])
        driver.find_element(By.XPATH,'//*[@id="date"]').send_keys(transformDate(i[5]))
        driver.find_element(By.XPATH,'//*[@id="obs"]').send_keys(i[1])
        time.sleep(3)
        driver.find_element(By.XPATH,'//*[@id="submit"]').click()



    driver.quit()
 