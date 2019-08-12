# -- coding: utf-8 --
'''
Created on 2019年7月19日

@author: lyc
''' 
import pytest,time
import allure   
is_skip = 1

@pytest.mark.usefixtures('Sys_user_manage_page')
@allure.feature('系统设置-用户管理-用户启用/禁用/重置密码')  #feature定义功能
class Test_user_forbidden_unfreeze_reset(object):    
            
    @pytest.mark.run(order=26)
    @pytest.mark.skipif(False,reason = '调试原因')    
    @allure.story('禁用用户')
    def test_forbidden_user(self,Sys_user_manage_page):  
        '''
            测试用例编号:
            测试用例标题:禁用用户 
            前置条件：打开编辑账号信息界面
            步骤：
            "
            1.点击禁用用户
            2.选择确定
    
            预期：
            1. 弹出禁用用户提示框
            2.用户状态变为禁用
            
        ''' 

        #点击禁用按钮
        allure.step('点击禁用按钮')
        Sys_user_manage_page.forbidden_btn_click() 
        #点击对话框中的确定        
        allure.step('点击禁用按钮')
        Sys_user_manage_page.forbidden_determine_click()
        #判断用户状态    
        allure.step('判断用户状态 ')  
        time.sleep(5)
        assert '禁用' in Sys_user_manage_page.get_User_table_value_by_key(key = '状态', index = 1)
        
        

    @pytest.mark.run(order=27)
    @pytest.mark.skipif(False,reason = '调试原因')
    @allure.story('启用用户')
    def test_unfreeze_user(self,Sys_user_manage_page):  
        '''
            测试用例编号:
            测试用例标题:启用用户
            前置条件：打开编辑账号信息界面
            步骤：
            "
            1.点击启用用户
            2.选择确定
    
            预期：
            1. 弹出禁用用户提示框
            2.用户状态变为启用
            
        ''' 
        #点击禁用按钮    
        allure.step('点击禁用按钮')
        Sys_user_manage_page.unfreeze_btn_click()
        #点击对话框中的确定    
        allure.step('点击对话框中的确定')
        Sys_user_manage_page.unfreeze_determine_click()  
        #判断用户状态    
        allure.step('判断用户状态')   
        time.sleep(5)
        assert '启用' in Sys_user_manage_page.get_User_table_value_by_key(key = '状态', index = 1)
        
        

    @pytest.mark.run(order=28)
    @pytest.mark.skipif(False,reason = '调试原因')   
    @allure.story('重置用户密码')
    def test_reset_user_pwd(self,Sys_user_manage_page):  
        '''
                  测试用例编号:
                  测试用例标题:重置用户密码
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.点击重置密码
                  2.选择确定
          
                  预期：
                  1. 弹出重置用户密码提示框
                  2. 用户密码重置为 123456
                  
        ''' 
        #点击重置密码    
        allure.step('点击重置密码')
        Sys_user_manage_page.resetpwd_btn_click()  
        
        #点击对话框中的确定    
        allure.step('点击对话框中的确定  ')
        Sys_user_manage_page.resetpwd_determine_click()
        
        
if __name__ == '__main__':
    import shutil,os    
    if os.path.exists(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result'):      
        shutil.rmtree(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')  
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')   
    else:   
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')
       
    result_pth=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."),'result').replace('\\','/')      
    pytest.main(['-s', '-q', 'Test_forbidden_unfreeze_reset.py','--alluredir', result_pth])
    os.system('allure serve {path}'.format(path = result_pth ))
    
    