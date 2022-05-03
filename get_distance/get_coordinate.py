from import_for_crawler import webdriver, options, time

def get_coordinate(addr):
    browser = webdriver.Chrome(executable_path='./chromedriver',options=options)
    browser.get("http://www.map.com.tw/")
    search = browser.find_element_by_id("searchWord")
    search.clear()
    search.send_keys(addr)
    browser.find_element_by_xpath("/html/body/form/div[10]/div[2]/img[2]").click()
    time.sleep(10)
#     iframe = browser.find_elements_by_tag_name("iframe")[1] This will be thrown error due to the number of iframes changed
    iframe = browser.find_elements_by_class_name("winfoIframe")[0]
    browser.switch_to.frame(iframe)
    coor_btn = browser.find_element_by_xpath("/html/body/form/div[4]/table/tbody/tr[3]/td/table/tbody/tr/td[2]")
    coor_btn.click()
    coor = browser.find_element_by_xpath("/html/body/form/div[5]/table/tbody/tr[2]/td")
    coor = coor.text.strip().split(" ")
    lat = coor[-1].split("：")[-1]
    log = coor[0].split("：")[-1]
    browser.quit()
    return (lat, log)