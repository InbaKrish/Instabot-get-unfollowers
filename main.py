try:

    import selenium
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.chrome.options import Options
    import os

    
except expression as identifier:
    print("\n Error:", identifier)
    print("\n Some of the required modules are not found.. :(")

def getfollowing():

    #sets to the profile page of ur account
    browser.get(u)
    sleep(2)

    #gets to the following box 
    browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    sleep(3)

    browser.get(u)

    sleep(3)

    #Reopen following box in order to get the infinite scroll box
    browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
    sleep(2)

    sb = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    #scrolls untill the end of the followers/followig box
    lh,nh = 0,1
    while lh != nh:
        lh = nh
        sleep(3)
        nh = browser.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
        return arguments[0].scrollHeight;""",sb)

    links = sb.find_elements_by_tag_name('a')
    names = [i.text for i in links if i.text != '']
    browser.get(u)
    return names

def getfollowers():

    #sets to the profile page of ur account
    browser.get(u)
    sleep(2)

    #gets to the followers box
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(2)
    browser.get(u)
    sleep(1.5)

    #Reopen followers box in order to get the infinite scroll box
    browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
    sleep(2)
    sb = browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
    
    #scrolls untill the end of the followers/followig box
    lh, nh = 0, 1
    while lh != nh:
        lh = nh
        sleep(3)
        nh = browser.execute_script("""arguments[0].scrollTo(0,arguments[0].scrollHeight);
        return arguments[0].scrollHeight;""", sb)

    links = sb.find_elements_by_tag_name('a')
    names = [i.text for i in links if i.text != '']
    browser.get(u)
    return names

if __name__ == "__main__":

    print('\n---------------AUTOMATED INSTA BOT----------------\n_____Developed by Inba_krish_____')

    #sets ur path of chrome driver , i guess it should be in your current working dir 
    #orelse change according to your wish
    path = os.getcwd() + "\chromedriver.exe"
    print("\n\nChromedriver path (make sure its in current working directory):",path)
    un = input('\n\nUsername of your account:')
    pwd = input('\nPassword of your account:')
    print('\n\t.....Loading.......\n\nYour Chrome Browser will automatically do certain things , Don"t panic :)')
    
    #sets the driver for chrome
    browser = webdriver.Chrome(executable_path=path)
    
    #used to make explicit wait
    wait = WebDriverWait(browser, 7)
    
    #gets the url
    browser.get('https://www.instagram.com/')
    sleep(2.5)

    try:

        #Automatically sets user credentials and sign in
        browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input').send_keys(un)

        browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input').send_keys(pwd)

        browser.find_element_by_xpath(
            '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div').click()
        sleep(1.5)
    except expression as identifier:
        print("Error:", identifier)
        print("\n User credentials not correct...rerun the program")

    


    while True:

        #waits for the starting save credentials page and clicks not now 
        ele = wait.until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
        if ele.is_displayed():
            ele.click()
            break
        else:
            break

    sleep(2)
    browser.find_element_by_xpath(
        '/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    sleep(1)

    browser.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a').click()
    sleep(2)
    u = browser.current_url
    getflwng = getfollowing()
    getflwrs = getfollowers()
    unfollowers = [user for user in getflwng if user not in getflwrs]
    
    #quits the browser window
    browser.quit()
    print('\nUnfollowers from following:\n')
    for i in unfollowers:
        print('\t',i)
