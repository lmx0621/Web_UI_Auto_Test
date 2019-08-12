# -- coding: utf-8 --
'''
Created on 2019年8月9日

@author: lyc
'''
from Common.tool import getString
import pytest,time
import allure 
is_skip = 1
@pytest.mark.usefixtures('Sys_role_manage_page')
@allure.feature('系统设置-角色管理-角色新增编辑查询')   
class Test_role_add_update_query(object):   
    @pytest.mark.run(order=1)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
    @allure.story('新增用户')   
    def test_add_role_ok_without_info(self,Sys_role_manage_page):    
        '''
        测试用例编号:
        测试用例标题:验证新增功能
        前置条件：用户登录成功，已填写角色名称(10个字符)，已选择菜单权限
        步骤：    1. 说明为空白点击确定
        预期： 
        1. 角色创建成功，角色展示的说明栏为空
       
       '''
        #点击新增按钮
        Sys_role_manage_page.add_click()    
        #判断新增角色对话框
        assert Sys_role_manage_page.is_text_in_element(locator=Sys_role_manage_page.rcDialogTitle,
                                                 text='增加角色') == True   
        
        #填写角色名称
        role_name = 'cmiotX'+ getString(4)
        Sys_role_manage_page.input_role_name(text = role_name)     
        #添加菜单权限（系统设置）
        Sys_role_manage_page.select_role_authority(name = '系统设置')
        #不填写说明栏
        
        #点击确定
        Sys_role_manage_page.determin_click()       
        
        #显示50条数据
        Sys_role_manage_page.select_page_split(index = 3)
        
        #判断新增角色是否在列表中    
        assert Sys_role_manage_page.check_table_by_value(expect_value = role_name, col_name = '角色')
        
        

if __name__ == '__main__':
    import shutil,os    
    if os.path.exists(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result'):      
        shutil.rmtree(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')  
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')   
    else:   
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')
       
    result_pth=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."),'result').replace('\\','/')      
    pytest.main(['-s', '-q', 'Test_add_update_query.py','--alluredir', result_pth])
    os.system('allure serve {path}'.format(path = result_pth ))

       
        