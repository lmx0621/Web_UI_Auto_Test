# -- coding: utf-8 --
'''
Created on 2019年7月23日

@author: lyc
'''
from Common.ChexingPage import Chengxing     
import allure   
@allure.feature('系统设置 -角色管理')
class Sys_role_manage(Chengxing):   
    def __init__(self,Browser_type): 
        super(Sys_role_manage, self).__init__(Browser_type)
        
        #角色选择框
        self.role_select = ('id','role') 
        #状态选择框
        self.status_select = ('id','status') 
        #分页选择框
        self.page_split = ('css selector',"div[title = '5 条/页']")
        
        #新增角色名称输入框
        self.role_name = ('css selector',"input[id ^='roleName']")  
        
        #新增角色说明输入框
        self.role_description = ('css selector',"textarea[id ^='description']")
        
        #状态选择框
        self.status_chebox = ('tag name','label')   
        
        #权限列表    
        self.authority_list_checkbox = ('css selector',"span[class = 'ant-tree-checkbox']")      
        self.authority_list_span = ('css selector',"span[class = 'ant-tree-title']")
        #异常提示
        self.form_explain = ('class name','ant-form-explain')   
        
        
    
    def input_role_name(self,text): 
        '''输入新增角色名称'''
        self.send_keys(locator = self.role_name, text = text)   
        
    def select_role_status(self,status):        
        '''选择新增角色状态'''    
        elements = self.find_elements(locator = self.status_chebox, timeout = 10)   
        for element in elements:    
            if status == element.text:
                self.click_By_element(element)  
                break
    
    
    def select_role_authority(self,name):   
        '''选择角色权限'''        
        _ = {}
        _list_checkbox = self.find_elements(locator = self.authority_list_checkbox, timeout = 10)    
        _list_span = self.find_elements(locator = self.authority_list_span, timeout = 10)  
        if len(_list_checkbox) == len(_list_span):  
            for i in range(len(_list_checkbox)):    
                _[_list_span[i].text] = _list_checkbox[i]
        for _k,_v in _.items(): 
            if _k == name:  
                self.click_By_element(_v)
                
    
    def input_role_description(self,text):      
        '''输入新增角色描述'''
        self.send_keys(locator = self.role_description, text = text)    
        
    
    def select_page_split(self,index):  
        '''调整分页'''  
        self.select_by_index(locator = self.page_split,index = index)   
        
    def add_click(self):    
        '''点击新增按钮'''    
        self.click_btn(btn_name = '新增')
    def determin_click(self):   
        '''点击确定按钮'''    
        self.click_btn(btn_name = '确定')
    
    def get_Role_table_value(self):      
        '''返回所有用户列表值'''
        return self.get_table_value()
    

    
  

if __name__ == '__main__':
    obj = Sys_role_manage('Chrome') 
    obj.login('superadmin', '123456')
    obj.click_menu_li(name = '角色管理')    
    obj.click_btn(btn_name = '新增')
    obj.is_text_in_element(locator = ('css selector',"input[id ^='rcDialogTitle']"), text = '增加角色')        
    
#     obj.select_page_split(index = 1)    
#     print(obj.check_table_by_value(expect_value = 'hahaha', col_name = '角色'))
      

    

