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

urls = ["https://www.kifli.hu/16552-zoldfarm-bio-uht-tej-2-8"
        , "https://www.kifli.hu/76483-cserpes-epres-joghurt"
        , "https://www.kifli.hu/14317-poco-loco-lagy-tortilla-wraps"
        # , "https://www.kifli.hu/58652-wein-s-fekete-erdei-sonka"
        , "https://www.kifli.hu/90112-ariel-folyekony-mososzer-color-clean-fresh-2-4l"
        # , "https://www.kifli.hu/36328-barilla-fusilli-durum-szarazteszta"
        , "https://www.kifli.hu/22996-wiesbauer-premium-becsi-virsli-2x200g"
        ]

ShopList = []
ProductList = []
PriceList = []
UrlList = []

for i in urls:
    driver.get(i)
    ShopList.append(["kifli.hu"])
    UrlList.append(i)
    ProductName = driver.find_element(By.XPATH, "//a[@class='redirect_link disabled']").text
    # print(ProductName)
    ProductList.append(ProductName)
    currentPrice = driver.find_element(By.XPATH, "//div[@class='u-displayInlineBlock currentPrice']").text
    currentPrice = currentPrice.split('Ft', 1)[0].replace(" ", "")
    # print(currentPrice)
    PriceList.append(currentPrice)

dfkifli = pd.DataFrame({
    "Shop": ShopList,
    "Product": ProductList,
    "Price": PriceList,
    "URL": UrlList
})
dfkifli

dfkifli.to_pickle("dfkifli.pkl")

driver.close()



