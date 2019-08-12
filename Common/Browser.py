# -- coding: utf-8 --
'''
Created on 2019年6月12日

@author: lyc
'''

#封装Browser 对象
from selenium import webdriver  
from selenium.webdriver.chrome.options import Options
from Common.Log import MyLog
from selenium.webdriver.support.wait import WebDriverWait   
from selenium.webdriver.support import expected_conditions as EC    
from selenium.common.exceptions import TimeoutException,WebDriverException,StaleElementReferenceException
from selenium.webdriver.support.ui import Select        
from selenium.webdriver.common.keys import Keys
from Conf.Config import Config
import allure
import time
class PageBase(object):  
    def __init__(self,Browser_type):    
        self.log = MyLog()
        self.webdriver = self.get_Browser_Type(Browser_type)    
        self.set_Browser_size() 
        self.conf = Config()    
        self.Browser_type = Browser_type
        
        
        
    def get_Browser_Type(self,Browser_type):   
        self.Browser = None 
        
        if Browser_type :      
            try:
                if Browser_type == 'Chrome':   
                    self.Browser = webdriver.Chrome()
                    self.log.debug('get_Browser {type}'.format(type='Chrome'))   
                    self.type_name = 'Chrome'
                    
                if Browser_type == 'Firefox':  
                    self.Browser = webdriver.Firefox()      
                    self.log.debug('get_Browser {type}'.format(type='Firefox'))  
                    self.type_name = 'Firefox'
                    
                if Browser_type == 'Ie':   
                    self.Browser = webdriver.Ie()           
                    self.log.debug('get_Browser {type}'.format(type='Ie')) 
                    self.type_name = 'Ie'   
                    
                if Browser_type == 'headless':    
                    opt = Options() 
                    opt.add_argument('headless')  
                    self.Browser = webdriver.Chrome(options=opt)

            except Exception as e:  
                MyLog.error(str(e))     
                return None
            return self.Browser 
        else:   
            return None
    
    def set_Browser_size(self):     
        #默认全屏显示
        try:
            self.webdriver.maximize_window()      
        
        except Exception as e:    
            self.log.error(e)       
            return None
            
    
    def close_Browser(self):    
        try:        
            self.webdriver.quit()   
            self.log.debug('close_Browser {Browser_type}'.format(Browser_type=self.type_name))
        except Exception as e:    
            self.log.error(e)   
            return None
            
    
    def getUrl(self,url):   
        try:    
            self.webdriver.get(url)      
            self.log.debug('Browser get {url}'.format(url=url)) 
        except Exception as e:    
            self.log.error(e)       
            self.allure_pic_report()
            return None
        
    
    def get_screenshot_as_file(self):       
        '''在本地截图函数'''  
        try:            
            pic_pth = self.conf.pic_path
            filename = pic_pth +str(time.time()).split('.')[0]+'.png'       
            filename = filename.replace('\\','/')
            self.webdriver.get_screenshot_as_file(filename)   
            self.log.debug('get_screenshot_as_file {filename}'.format(filename=filename))
            return filename
        except Exception as e:    
            self.log.error(e)   
            return None
    
    def allure_pic_report(self,msg = None):    
        '''在allure-report报告中保存截图'''
        f = self.get_screenshot_as_file()   
        self.log.error('失败的用例，已在异常处截图 :{filename} {msg}'.format(filename = f,msg =msg )) 
        allure.attach.file(f,'失败的用例，已在异常处截图 :{filename} {msg}'.format(filename = f,msg =msg ),allure.attachment_type.PNG)
        
        
    
    def find_element(self,locator,timeout = 10):    
        '''
                    定位元素，参数locator是元祖类型
        Usage:
        locator = ("id","xxx")
        locator = ()
        driver.find_element(locator)
        '''     
        try:
            element = WebDriverWait(self.webdriver, timeout).until(EC.presence_of_element_located(locator))
            return element  
        except Exception as e:  
            self.log.error("not find element by '{way}' ,element name is '{name}'".format(way=locator[0],name=locator[1]))      
            self.allure_pic_report(msg = '没有找到元素  by {way},element name is {name}'.format(way=locator[0],name=locator[1]))
            self.restart()
            self.log.error("restar Login")  
            return None
            raise e

    
    def find_elements(self, locator, timeout=10):
        '''定位一组元素'''    
        try:
            elements = WebDriverWait(self.webdriver, timeout, 1).until(EC.presence_of_all_elements_located(locator))
            return elements 
        except Exception as e:  
            self.log.error("not find elements by '{way}' ,elements name is '{name}'".format(way=locator[0],name=locator[1]))    
            self.allure_pic_report(msg = '没有找到元素  by {way},elements name is {name}'.format(way=locator[0],name=locator[1]))
            self.restart()  
            self.log.error("restar Login")  
            return []
            raise e


            
    
    def click(self, locator):
        '''
                   点击操作
       Usage:
       locator = ("id","xxx")
       driver.click(locator)
       '''
        element = self.find_element(locator)
        if element is not None:
            try:
                element.click()         
                self.log.debug('click by locator {locator}'.format(locator = locator))  
                time.sleep(1)   
            except Exception as e:  
                self.log.error(e)   
                self.allure_pic_report()      
                return 
        else:   
            return 
            
            
    def clear(self,locator,timeout):    
        try:   
            _element = self.find_element(locator, timeout)  
#             _element.clear()    
            _element.send_keys(Keys.CONTROL+'a')
            _element.send_keys(Keys.BACKSPACE)   
        except Exception as e:  
            self.log.error(e)       
            return 
        else:   
            return 
    
    def click_By_element(self,element): 
        if element:     
            try:    
                element.click()         
                self.log.debug('click {element}'.format(element = element.__dict__))    
                allure.attach('click {element}'.format(element = element.__dict__))
                time.sleep(1)   
            except Exception as e:  
                self.log.error(e)
                allure.attach('click {element}'.format(element = element.__dict__))
                return 
        
    
        
    def refresh(self): 
        '''刷新界面'''  
        self.webdriver.refresh()    
        self.log.debug('刷新界面')   
        
    
    
    def is_text_in_element(self, locator, text, timeout=10):    
        '''
                    判断文本在元素里,没定位到元素返回False，查找到返回True
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.webdriver, timeout, 1).until(EC.text_to_be_present_in_element(locator, text))
        except TimeoutException:
            self.log.error("元素没定位到："+str(locator))  
            return False
        else:
            return result
        
    
    def is_text_in_value(self, locator, value, timeout=10): 
        '''
                    判断元素的value值，没定位到元素返回false,定位到返回判断结果布尔值
        result = driver.text_in_element(locator, text)
        '''
        try:
            result = WebDriverWait(self.webdriver, timeout, 1).until(EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            self.log.error("元素没定位到："+str(locator))  
            self.allure_pic_report()
            return False
        else:
            return result 
        
    
    def is_title(self, title, timeout=10):
        '''判断title完全等于'''
        result = WebDriverWait(self.webdriver, timeout, 1).until(EC.title_is(title))
        return result   
    
    
    def is_alert_present(self, timeout=10):
        '''判断页面是否有alert，有返回alert(注意这里是返回alert,不是True)没有返回False'''
        result = WebDriverWait(self.webdriver, timeout, 1).until(EC.alert_is_present())
        return result
    
    
    def Select_by_value(self,locator,value,timeout=10):      
        _element = self.find_element(locator)    
        try:
            s = Select(_element)         
            s.select_by_value(value) 
            self.log.debug('select {value}'.format(value = value))   
            time.sleep(1)         
        except Exception as e:  
            self.log.error(e)   
            self.allure_pic_report()
            return 
            
    
    def get_text(self, locator,timeout = 3):
        '''获取文本'''
        try:
            element = WebDriverWait(self.webdriver, timeout, 0.5).until(EC.presence_of_element_located(locator))
            return element.text
        except TimeoutException :      
            self.log.debug('元素 {element} 没有找到'.format(element = locator))   
            self.allure_pic_report()
            return ''
        
        
    def get_attribute(self, locator, name):
        '''获取属性'''
        element = self.find_element(locator)
        return element.get_attribute(name)  
    
    def get_element_attribute(self,element,name):    
        '''获取某个元素的属性值'''
        return element.get_attribute(name)
        
    
    
    def get_login_url(self):    
        '''获取登陆url'''
        return str(self.conf.login_url_debug)   
                
                    
    

        
    def login(self,username,password): 
        '''用户登陆'''      
        if self.webdriver:  
            self.webdriver.delete_all_cookies()
            self.getUrl(self.get_login_url())       
            self.send_keys(locator = ('id','userName'),text = username)     
            self.send_keys(locator = ('id','password'),text = password)     
            self.click(locator = ('xpath','//*[@id="root"]/div/div/article/form/div[4]/div/div/span/button'))  
            if self.is_text_in_element(locator=('id','login'), text=username) == True:     
                self.log.debug('success login by user {name}'.format(name=username))
                return self.webdriver
        else:           
            return None
    
    
    def send_keys(self,locator,text):        
        element = self.find_element(locator)    
        if element is not None: 
            try:    
                element.clear()         
                self.log.debug('clear')
                element.send_keys(text)     
                self.log.debug('send {text}'.format(text = text))   
            except WebDriverException:      
                self.log.debug('元素  {element}不可编辑'.format(element = locator))   
                self.allure_pic_report()
                return        

    

    
    def restart(self):   
        '''
        关闭浏览器重新打开
        '''     
        allure.attach('重新打开浏览器')
        self.webdriver.delete_all_cookies()
        self.webdriver.close()
        self.webdriver = self.get_Browser_Type(self.Browser_type)   
        self.webdriver.maximize_window() 
        self.get_login_url()    
        self.login(username = 'superadmin', password = '123456')

    
if __name__ == '__main__':
    obj = PageBase('Chrome')     
    obj.getUrl('http://192.168.102.109:8080/bss/#/')        
    obj.allure_pic_report()     


    
    
    
             
        
    
            
            
        
        
        
        
        

        
    