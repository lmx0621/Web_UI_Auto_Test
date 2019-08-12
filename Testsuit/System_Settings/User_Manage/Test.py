# -- coding: utf-8 --
'''
Created on 2019年8月6日
  
@author: lyc
'''
# -- coding: utf-8 --
'''
Created on 2019年8月6日
  
@author: lyc
'''
from Common.tool import getString   
# from Common.Screen import screen
from Page.sys_user_manage import Sys_user_manage
import pytest,os,shutil
  
class Test_demo(object):   
    
    Test_user_manage = Sys_user_manage('Chrome') #全局变量
          
    @classmethod
    def setup_class(self):              
#         self.Test_user_manage = Sys_user_manage('Chrome') #全局变量
        self.Test_user_manage.login('superadmin', '123456')
      

#     def test_add_account_Ok(self):    
#         '''
#         测试用例编号:
#         测试用例标题:新增账号，点击"确定"
#         前置条件：已输入合法的姓名，合法账号，合法手机号，角色
#         步骤：1. 点击"确定"
#         预期：1. 当成功提交后，关闭弹窗，并刷新角色角色列表，新增账号出现在列表中（出现在最后？）
#      
#         '''
#         #点击新增按钮
#         allure.attach('点击新增按钮')
#         self.Test_user_manage.add_btn_click()  
#         #判断是否存在新增用户弹出框  
#            
#         assert self.Test_user_manage.is_text_in_element(locator=self.Test_user_manage.addDialog_title,
#                                                  text='添加用户') == True
#          
#         #编辑用户信息
#         user_name = 'name'+ getString(num = 4)
#         Account = 'Account'+ getString(num = 4)  
#         iphone = '17309013038'
#          
#         self.Test_user_manage.input_add_user_data(name = user_name, 
#                                                   loginAccount = Account, 
#                                                   iphone = iphone)
#          
#          
#         #选择用户角色
#          
#         self.Test_user_manage.add_role(name = '测试')
#          
#         #点击保存按钮
#         self.Test_user_manage.add_user_save()
#             
#         #判断用户列表    
#         assert self.Test_user_manage.check_user_by_name(username = user_name)
          
if __name__ == '__main__':
     
    if os.path.exists(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result'):      
        shutil.rmtree(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')  
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')   
    else:   
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')
         
    result_pth=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."),'result').replace('\\','/')      
    pytest.main(['-s', '-q', 'test.py','--alluredir', result_pth])
    os.system('allure serve {path}'.format(path = result_pth ))