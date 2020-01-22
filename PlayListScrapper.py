from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#import time 
driver = webdriver.Chrome(ChromeDriverManager().install())
#Link that you wish to scrape from:
driver.get("https://www.jiosaavn.com/")

search = driver.find_element_by_name("q")

#enter scraping criteria:
search.send_keys("Gryffin")

#below statement performs clicking enter functionality:
search.send_keys(Keys.ENTER)

f = open("MyPlayList.txt", "w")

for vari in range(1,10):
    title = driver.find_element_by_xpath("/html/body/div[8]/div/section/div/ol/li["+str(vari)+"]/div[3]/div/div[1]/div/div/span")
    singers = driver.find_element_by_xpath("/html/body/div[8]/div/section/div/ol/li["+str(vari)+"]/div[3]/div/div[2]")
    print("Song : ",title.text)
    print("Singers : ", singers.text,"\n")
    f.write("Song : ")
    f.write(title.text)
    f.write("\nSingers : ")
    f.write(singers.text)
    f.write("\n\n")
    
f.close()



