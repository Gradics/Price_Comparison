import selenium
selenium.__version__

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#-- Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pandas as pd

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service = service, options = options)

driver.implicitly_wait(10) # seconds

urls = ["https://online.auchan.hu/shop/zoldfarm-bio-uht-tej-28percent-1-l.p-182510"
        , "https://online.auchan.hu/shop/cserpes-joghurt-epres-elofloras-250-g.p-400116"
        , "https://online.auchan.hu/shop/poco-loco-original-lagy-tortilla-lapok-buzalisztbol-25-cm-6-db-370-g.p-811677"
        , "https://online.auchan.hu/shop/ariel-folyekony-mososzer-35l-70-mosashoz-color-clean-and-fresh.p-689088"
        # , "https://online.auchan.hu/shop/wein-fekete-erdei-szeletelt-fustolt-sonka-100-g.p-844695"
        # , "https://online.auchan.hu/shop/ariel-folyekony-mososzer-48-mosashoz-color.p-469370"
        # , "https://online.auchan.hu/shop/barilla-fusilli-apro-durum-szarazteszta-500-g.p-13654"
        # , "https://online.auchan.hu/shop/wiesbauer-premium-becsi-sertesvirsli-400-g.p-529813"
        ]

import pandas as pd
ShopList = []
ProductList = []
PriceList = []
UrlList = []

for i in urls:
    driver.get(i)
    ShopList.append(["auchan.hu"])
    UrlList.append(i)
    ProductName = driver.find_element(By.XPATH, "//h1[@class='gtuFPjTO ATt8cOCX HvLWs3VB']").text
    
    # print(ProductName)
    ProductList.append(ProductName)
    currentPrice = driver.find_element(By.XPATH, "//div[@class='_98UwMZjS']").text
    currentPrice = currentPrice.split('FT', 1)[0].replace(" ", "")
    # print(currentPrice)
    PriceList.append(currentPrice)

dfAuchan = pd.DataFrame({
    "Shop": ShopList,
    "Product": ProductList,
    "Price": PriceList,
    "URL": UrlList
})
print(dfAuchan)

dfAuchan.to_pickle("dfAuchan.pkl")

driver.close()




