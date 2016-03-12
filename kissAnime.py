#created by Tyro
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from selenium.common.exceptions import NoSuchElementException

class episodeList:
    def main(self):
        chromeDriverLoc = 'C:\\chromedriver.exe'  #change chrome driver location here
        fileLoc = "C:\\Users\Sarath\Desktop\links.txt"  #change destination file location here
        url = "https://kissanime.to/Anime/Haikyuu-Second-Season/Episode-002?id=117991"
        user = raw_input("Enter Username: ")
        passwrd = raw_input("Enter Password: ")
        quality = raw_input("Choose quality (1 ->1080p, 2 ->720p, 3-> 480, 4 ->360)")
        if (quality == "1"):
            qlty = "x1080.mp4"
        elif (quality == "2"):
            qlty = "720.mp4"
        elif (quality == "3"):
            qlty = "x480.mp4"
        elif (quality == "4"):
            qlty = "x360.mp4"
        else:
            qlty = "x720.mp4"
        # 1920x1080.mp4 1280x720.mp4 854x480.mp4 640x360.mp4
        length = int(raw_input("Enter length of series:(input more if unsure) "))
        browser = webdriver.Chrome(chromeDriverLoc) # Get local session of chrome
        browser.get("https://kissanime.to/Login") # Load page
        time.sleep(10)  # Let the page load, will be added to the API
        assert "Login" in browser.title
        userName = browser.find_element_by_name("username") # Find the query box
        userName.send_keys(user)
        passWord = browser.find_element_by_name("password")
        passWord.send_keys(passwrd + Keys.RETURN)
        browser.get(url)
        linksList = []
        for i in range(length):
                HD = browser.find_element_by_xpath(".//a[contains(text(), '"+qlty+"')]")
                name = browser.title.replace(" ","%20")
                linksList.append(HD.get_attribute("href")+"&title="+name)
                print linksList[i]
                try:
                    next = browser.find_element_by_id("btnNext")
                    next.click()
                except:
                    break
        with open(fileLoc,'a') as links:
            for i in linksList:
                links.write(i)
                links.write('\n')
        browser.close()

if __name__ == '__main__':
    episodeList().main()
	