# -- coding: utf-8 --
'''
Created on 2019年7月10日

@author: lyc
'''
import math
from Common.Browser import PageBase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains    
from selenium.common.exceptions import StaleElementReferenceException
class Chengxing(PageBase):  
    
    def __init__(self,Browser_type): 
        super(Chengxing, self).__init__(Browser_type)       
        
        #左侧导航栏
        self.Menu_locator = ('tag name',"li")
        
        self.headerMenu_locator = ('xpath',"//ul[@class='ant-menu headerMenu ant-menu-dark ant-menu-root ant-menu-horizontal']/li")
        
        self.ChildMenu_locator = ('xpath',"//ul[@class='ant-menu ant-menu-sub ant-menu-inline']/li")
        
        #按钮
        self.btn = ('tag name','button')    
        
        #table th    
        self.table_th = ('tag name','th')  
        
        #table td      
        self.table_td = ('tag name','td')   
        
        #对话框    
        self.rcDialogTitle = ('css selector',"div[id ^='rcDialogTitle']")
    
        #车型平台页面上方点击导航超链接
    def click_href(self,locator,name,timeout=10):  
        elements = self.find_elements(locator, timeout)     
        if elements:
            for _element in elements:          
                if name in _element.text:
                    self.click_By_element(_element)
                    
    
            
    def click_menu_li(self,name,timeout=10):    
        '''
            点击左导航栏菜单
        '''     
        elements = self.find_elements(self.Menu_locator, timeout)      
        if elements:            
            for _element in elements:   
                try:  
                    if name == _element.get_attribute('title'):       
                        self.click_By_element(_element) 
                except Exception as  StaleElementReferenceException:    
                    self.log.debug('前端页面变动,当前元素不在页面中')    
                    
                    
                          
                    
        
    
    def click_headerMenu_li(self,name,timeout=10):  
        '''
                        点击页面上方导航栏
        '''             
        elements = self.find_elements(self.headerMenu_locator, timeout)      
        if elements:
            for _element in elements:         
                if name in _element.text:
                    self.click_By_element(_element) 
                    
        
        self.child_elements = self.find_elements(self.ChildMenu_locator) 
    
    def click_child_menu_li(self,name):   
        '''
        点击菜单下的子菜单
        '''         
        Flag = False
        if self.child_elements: 
            for child_element in self.child_elements:     
                if name == child_element.text:  
                    self.click_By_element(child_element)        
                    Flag = True 
        
        if Flag == False:   
            self.log.error('can not click {child_menu_li}'.format(child_menu_li = name))
            
            
    
    def select_by_index(self,locator,index = 1):        
        '''通过index选择下拉框'''
        _element = self.find_element(locator)   
        self.click(locator = locator)    
        for _i in range(index):  
            ActionChains(self.webdriver).send_keys(Keys.DOWN).perform() 
        ActionChains(self.webdriver).send_keys(Keys.ENTER).perform()
        

    
    
    def click_btn(self,btn_name = None):
        '''
        针对车型平台封装的点击按钮方法
        '''     
        _elements = self.find_elements(locator = self.btn, timeout = 10)    
        if btn_name :
            for _element in _elements:      
                if btn_name in _element.text.replace(' ','') in btn_name:       
                    self.click_By_element(_element)     
                    break
        else:       
            for _element in _elements:   
                self.click_By_element(_element)
    

            

        
    def get_table_value(self):  
        '''
        获取table中的属性
        '''
        th = [] #列名
        td = [] #行数据
        return_result = [] #返回数据
        _elements_th = self.find_elements(locator = self.table_th, timeout = 10)    
          
        if _elements_th:  
            for _element in _elements_th:  
                th.append(_element.text.replace('\n',''))   
        _elements_td = self.find_elements(locator = self.table_td, timeout = 10)    
        if _elements_td:    
            for _element in _elements_td:   
                td.append(_element.text)    
                
        length_td = len(td)           
        length_th = len(th) 
        n = length_td/length_th     
        for i in range(int(n)):  
            one_list = td[math.floor(i / n * length_td):math.floor((i + 1) / n * length_td)]
            _ = dict(map(lambda x,y:[x,y],th,one_list))
            return_result.append(_)
        return return_result
    
    
    def check_table_by_value(self,expect_value,col_name = None): 
        '''核对列表信息,查找到返回True,未找到返回False
           expect_value 为期望的字符串名    
           col_name 为列名
        '''    
        name_list = [] 
        if expect_value:    
            for line in self.get_table_value():    
                name_list.append(line.get(col_name))  
        
        return expect_value in name_list

            
        
    
    
        




