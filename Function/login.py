# -- coding: utf-8 --
'''
Created on 2019年7月4日

@author: lyc
'''


def login(WebDriver,url):   
    if WebDriver:
        WebDriver.getUrl(url)   
        WebDriver.send_keys(locator = ('id','userName'),text = 'superadmin')
        WebDriver.send_keys(locator = ('id','password'),text = '123456')    
        WebDriver.click(locator = ('xpath','//*[@id="root"]/div/div/article/form/div[4]/div/div/span/button'))  
        if WebDriver.is_text_in_element(locator=('id','login'), text='superadmin') == True:     
            WebDriver.log.debug('success login by user {name}'.format(name='superadmin'))
            return WebDriver
    else:           
        return None
    
        
    