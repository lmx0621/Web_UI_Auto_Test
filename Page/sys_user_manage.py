# -- coding: utf-8 --
'''
Created on 2019年1月24日

@author: lyc
'''

#from Common.Browser import PageBase    
from Common.ChexingPage import Chengxing     
import allure   

@allure.feature('系统设置 -用户管理')
class Sys_user_manage(Chengxing):  
    

    def __init__(self,Browser_type): 
        super(Sys_user_manage, self).__init__(Browser_type)   
        #查询姓名输入框 
        self.rel_name = ('id','realName')    
        #角色选择框
        self.role_select = ('id','roleList')  
        #状态选择框 
        self.status_select = ('id','sysUserStatus')   
        #添加用户姓名输入框
        self.addAccountForm_realName = ('id','addAccountForm_realName') 
        #加添用户账号输入框
        self.addAccountForm_loginAccount = ('id','addAccountForm_loginAccount')
        #加添用户手机输入框 
        self.addAccountForm_tel = ('id','addAccountForm_tel')   
        #添加用户角色列表
        self.addRoleCheckBoxList = ('class name','ant-checkbox-input')    
    
        #新增用户对话框
        self.addDialog_title = ('css selector',"div[class = 'ant-modal-title'][id ^='rcDialogTitle']")
        #编辑用户对话框
        self.updateDialog_title = ('css selector',"div[class = 'ant-modal-title'][id ^='rcDialogTitle']")  
        
  
        #异常提示
        self.form_explain = ('class name','ant-form-explain')   
        
        #禁用对话框
        self.forbidden_Dialog = ('class name','ant-modal-confirm-content') 
        
        #启用对话框
        self.unfreeze_Dialog = ('class name','ant-modal-confirm-title') 
        #重置密码对话框
        self.resetpwd_Dialog = ('class name','ant-modal-confirm-content')
        
    
    def input_name(self,username):
        '''输入框输入角色名字'''
        self.send_keys(locator = self.rel_name, text = username)
        
    def query_click(self):
        '''点击查询按钮'''    
        self.click_btn(btn_name = '查询')  

    
    def add_btn_click(self):   
        '''点击新增按钮'''        
        self.click_btn(btn_name = '新增')    
          
        
    
    def update_btn_click(self): 
        '''点击编辑按钮'''    
        self.click_btn(btn_name = '编辑')

    
    def add_role(self,name):    
        '''根据角色名字选择角色'''
        rolelist_elements = self.find_elements(locator=self.addRoleCheckBoxList)  
          
        if rolelist_elements is not None:
               
            for role_element in rolelist_elements: 
                         
                if name in self.get_element_attribute(role_element, 'value'):
                    
                    self.click_By_element(element = role_element)
                
                
                
    def add_user_save(self):  
        '''点击新增用户弹窗中的保存按钮'''    
        self.click_btn(btn_name = '保存')
   
        
    def update_user_save(self):     
        '''点击编辑用户弹窗中的保存按钮'''    
        self.click_btn(btn_name = '保存')

        
    def input_add_user_data(self,name,loginAccount,iphone):    
        #输入姓名   
        self.send_keys(locator =self.addAccountForm_realName, text = name)  
        #输入用户账号    
        self.send_keys(locator = self.addAccountForm_loginAccount, text = loginAccount) 
        #输入手机号    
        self.send_keys(locator = self.addAccountForm_tel, text = iphone)        

    def clear_addAccountForm_realName(self):       
        self.clear(locator = self.addAccountForm_realName,timeout = 10)
      
    def clear_addAccountForm_loginAccount(self):
        self.clear(locator =self.addAccountForm_loginAccount,timeout= 10)  
         
    def clear_addAccountForm_tel(self,):
        self.clear(locator =self.addAccountForm_tel,timeout= 10)
        
          
    
    def forbidden_btn_click(self):  
        '''点击禁用按钮'''    
        self.click_btn(btn_name = '禁用')

    
    def forbidden_determine_click(self):    
        '''点击禁用对话框中的确定按钮'''         
        self.click_btn(btn_name = '确定')
     
        
    def forbidden_cancel_click(self):    
        '''点击禁用对话框中的确定按钮'''     
        self.click_btn(btn_name = '确定') 
    
    
    def unfreeze_btn_click(self):   
        '''点击启用按钮'''    
        self.click_btn(btn_name = '启用')
    
    def unfreeze_determine_click(self): 
        '''点击启用用户对话框中的确定按钮'''     
        self.click_btn(btn_name = '确定') 
        
    def unfreeze_cancel_click(self): 
        '''点击启用用户对话框中的取消按钮'''     
        self.click_btn(btn_name = '取消') 
        
    def resetpwd_btn_click(self):   
        '''点击重置密码按钮'''  
        self.click_btn(btn_name = '重置密码') 
    
    def resetpwd_determine_click(self): 
        '''点击重置密码对话框确定按钮'''
        self.click_btn(btn_name = '确定')    
        
    def resetpwd_cancel_click(self):    
        '''点击重置对话框中的取消按钮''' 
        self.click_btn(btn_name = '取消')   
    
    def select_role_by_index(self,index):  
        '''选择用户角色'''  
        self.select_by_index(locator = self.role_select, index = index)
        
    def select_status_by_index(self,index): 
        '''选择用户状态'''
        self.select_by_index(locator = self.status_select, index = index)
        
    
    def get_DialogTitle(self,locator):      
        return self.find_element(locator, timeout = 3).text
        
        
    def get_User_table_value(self):      
        '''返回所有用户列表值'''
        return self.get_table_value()
    
    def get_form_explain(self): 
        '''返回form_explain列表值'''
        return self.get_text(locator = self.form_explain)
    
    
    def add_cancel_click(self): 
        '''点击添加用户对话框中的取消按钮'''       
        
        self.click_btn(btn_name = '取消')
    

    def update_cancel_click(self):  
        '''点击编辑用户对话框中的取消按钮'''   
        self.click_btn(btn_name = '取消')
    
    
    def get_User_table_value_by_key(self,key,index = 1):  
        '''返回用户表中某一个属性值'''          
        result = []       
        if key: 
            if self.get_User_table_value():      
                for line in self.get_User_table_value():    
                    if line.get(key):       
                        result.append(line.get(key))    
                if key != '角色': 
                    return result[index - 1]    
                
                else:   
                    return result[index - 1].split('；') 
            else:   
                return []
        return []
    
        
    
    def click_btn_by_name(self,name):   
        '''通过按钮名称点击按钮'''
        elements = self.find_elements(locator = self.btns, timeout = 10)       
        for element in elements:    
            if name in element.text:    
                self.click_By_element(element)
        
        
    
    
    def check_user_by_name(self,username,idnex = 1):  
        '''核对用户列表信息,查找到返回True,未找到返回False'''    
        name_list = [] 
        if username:    
            for line in self.get_User_table_value():    
                name_list.append(line.get('姓名'))  
        
        return username in name_list
        
              
        


    


if __name__ == '__main__':  
    obj = Sys_user_manage('headless') 
    obj.login('superadmin', '123456')   
#     obj.input_name(username = 'superadmin') 
#     obj.click_btn(btn_name = '查询')
    print(obj.get_table_value())
    
#     obj.click_btn_by_name('确 定')
    

      
    


   
    
    
    

    
    
    


