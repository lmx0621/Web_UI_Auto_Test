# -- coding: utf-8 --
'''
Created on 2019年7月11日

@author: lyc
'''

   
from Common.tool import getString
import pytest,time
import allure   
is_skip = 1

@pytest.mark.usefixtures('Sys_user_manage_page')
@allure.feature('系统设置-用户管理-用户新增编辑查询')
class Test_user_add_update_query(object):
    
   
    
    @pytest.mark.run(order=1)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
     
    @allure.story('新增用户')
    def test_add_account_Ok(self,Sys_user_manage_page):    
        '''
        测试用例编号:
        测试用例标题:新增账号，点击"确定"
        前置条件：已输入合法的姓名，合法账号，合法手机号，角色
        步骤：1. 点击"确定"
        预期：1. 当成功提交后，关闭弹窗，并刷新角色角色列表，新增账号出现在列表中（出现在最后？）
    
        '''
        #点击新增按钮
        Sys_user_manage_page.add_btn_click()  
        #判断是否存在新增用户弹出框  
          
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
        
        #编辑用户信息
        user_name = 'name'+ getString(num = 4)
        Account = 'Account'+ getString(num = 4)  
        iphone = '17309013038'
        
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
        
        
        #选择用户角色
        
        Sys_user_manage_page.add_role(name = '测试')
        
        #点击保存按钮
        Sys_user_manage_page.add_user_save()
           
        #判断用户列表    
        assert Sys_user_manage_page.check_user_by_name(username = user_name)
        
        
    
    
    
    
    @pytest.mark.run(order=2)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('新增用户')
    def test_add_account_error_noRole(self,Sys_user_manage_page):    
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面，判断角色是否为空
        前置条件：打开编辑账号信息界面
        步骤："
        1. 输入姓名
        2. 输入账号
        3. 输入手机号
        4. 不勾选角色，点击确定"
 
        预期："1. 当未选角色时，复选框后红字提示“请选择角色”
        ''' 
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        user_name = 'name'+getString(num = 4)  
        Account = 'Account'+getString(num = 4)  
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #不选择用户角色,输入为空
        Sys_user_manage_page.add_role(name = '#############')
         
        #点击保存按钮
        Sys_user_manage_page.add_user_save()
         
        assert Sys_user_manage_page.get_form_explain() == '请选择角色'  
         
        #点击取消
        Sys_user_manage_page.add_cancel_click()
        
    
    
    @pytest.mark.run(order=3)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
      
    @allure.story('新增用户')
    def test_add_account_error_noPhone(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面，判断手机号是否为空
        前置条件：打开编辑账号信息界面
        步骤：
        1. 输入姓名
        2. 输入账号
        3. 选择角色
        4. 不输入手机，点击确定"

 
        预期："1. 当手机号为空时，文本框后红字”请输入手机号“
        ''' 
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        user_name = 'name'+getString(num = 4)  
        Account = 'Account'+getString(num = 4) 
        #手机号为空 
        iphone = ''
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择角色
        Sys_user_manage_page.add_role(name = '测试')
         
        #点击保存按钮
        Sys_user_manage_page.add_user_save()
         
        assert Sys_user_manage_page.get_form_explain() == '请输入手机号'  
         
        #点击取消
        Sys_user_manage_page.add_cancel_click()
    
    
    @pytest.mark.run(order=4)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
     
    @allure.story('新增用户')
    def test_add_account_error_noAccount(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面，判断账号是否为空
        前置条件：打开编辑账号信息界面
        步骤：
        1. 输入姓名
        2. 输入手机
        3. 选择角色
        4. 不输入账号，点击确定

 
        预期："1. 当账号为空时，文本框后红字“请填写账号名称”
        ''' 
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        user_name = 'name'+getString(num = 4)
        #账号为空
        Account = ''
        #手机号码
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择角色
        Sys_user_manage_page.add_role(name = '测试')
         
        #点击保存按钮
        Sys_user_manage_page.add_user_save()
         
        assert Sys_user_manage_page.get_form_explain() == '请输入账号'  
         
        #点击取消
        Sys_user_manage_page.add_cancel_click()

    
    
    @pytest.mark.run(order=5)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
      
    @allure.story('新增用户')
    def test_add_account_error_noRealName(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面，判断姓名是否为空
        前置条件：打开编辑账号信息界面
        步骤：
        1. 输入账号
        2. 输入手机
        3. 选择角色
        4. 不输入姓名，点击确定

 
        预期："1. 当账号为空时，文本框后红字“请填写账号名称”
        ''' 
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为空
        user_name = ''
        #输入账号
        Account = 'Account'+getString(num = 4) 
        #手机号码
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择角色
        Sys_user_manage_page.add_role(name = '测试')
         
        #点击保存按钮
        Sys_user_manage_page.add_user_save()
         
        assert Sys_user_manage_page.get_form_explain() == '请输入姓名'  
         
        #点击取消
        Sys_user_manage_page.add_cancel_click()
    
    
    @pytest.mark.run(order=6)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
      
    @allure.story('新增用户')
    def test_add_account_select_role_more(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面选择角色测试
        前置条件：打开编辑账号信息界面
        步骤：
        1. 展示角色列表
        2. 选择一个角色
        3. 选择多个角色

 
        预期：
        1. 展示角色列表
        2. 可以选择一个角色
        3. 可以选择多个角色
        '''
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为空
        user_name = 'test'+getString(num = 4) 
        #输入账号
        Account = 'Account'+getString(num = 4) 
        #手机号码
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择第一个角色
        Sys_user_manage_page.add_role(name = '测试')
        
        #选择第二个角色
        Sys_user_manage_page.add_role(name = '开发')
        
        #点击保存按钮
        Sys_user_manage_page.add_user_save()   
        
        
    
        
    @pytest.mark.run(order=7)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
      
    @allure.story('新增用户')
    def test_add_account_input_error_relname(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
        1. 姓名分别输入特殊字符_，~，@
    

 
        预期：
        1.失去焦点后，文本框提示'不允许使用特殊字符'
        '''
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为特殊字符
        user_name = '_~@'+getString(num = 4) 
        #账号为数字加英文字符
        Account = 'test'+getString(num = 4) 
        #手机号码为特殊字符
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择第一个角色
        Sys_user_manage_page.add_role(name = '测试')
        
        #选择第二个角色
        Sys_user_manage_page.add_role(name = '开发')
        
        #点击保存按钮
        Sys_user_manage_page.add_user_save()       
        
        assert Sys_user_manage_page.get_form_explain() == '不允许使用特殊字符'  
        
        #新增点击取消
        Sys_user_manage_page.add_cancel_click()  
    
    
    @pytest.mark.run(order=8)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
      
    @allure.story('新增用户')
    def test_add_account_input_error_account(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：      
        1. 账号分别输入特殊字符_，~，@


 
        预期：    
        1.失去焦点后，文本框提示'账号只允许使用数字、字母、下划线'
        '''
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为特殊字符
        user_name = 'test'+getString(num = 4) 
        #账号为特殊字符
        Account = '_@~'+getString(num = 4) 
        #手机号码为正常
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择第一个角色
        Sys_user_manage_page.add_role(name = '测试')
        
        #选择第二个角色
        Sys_user_manage_page.add_role(name = '开发')
        
        #点击保存按钮
        Sys_user_manage_page.add_user_save()       
        
        assert Sys_user_manage_page.get_form_explain() == '账号只允许使用数字、字母、下划线'   
        
        #新增点击取消
        Sys_user_manage_page.add_cancel_click()  
        
        
    
        
    
    
    @pytest.mark.run(order=9)    
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('新增用户')
    def test_add_account_input_error_iphone(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
    
        1. 手机分别输入特殊字符_，~，@，-

 
        预期：
        1. 失去焦点后，文本框提示'请输入手机号'
        '''
    
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为数字加英文字符
        user_name = 'test'+getString(num = 4) 
        #账号为数字加英文字符
        Account = 'test'+getString(num = 4) 
        #手机号码为特殊字符
        iphone = '@~-'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #选择第一个角色
        Sys_user_manage_page.add_role(name = '测试')
        
        #选择第二个角色
        Sys_user_manage_page.add_role(name = '开发')
        
        #点击保存按钮
        Sys_user_manage_page.add_user_save()       
        
        assert Sys_user_manage_page.get_form_explain() == '请输入手机号'     
        
        #点击取消
        Sys_user_manage_page.add_cancel_click()
        

    
    
    @pytest.mark.run(order=10)  
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('新增用户')
    @pytest.mark.parametrize("realname,expected",
                             [('中移物联网中国移动',''),
                              ('中移物联网中国移动一',''),
                              ('中移物联网中国移动一二','姓名最大长度为10'),
                              ('cmiottest',''),
                              ('cmiottestY',''),
                              ('cmiottestYY','姓名最大长度为10')])
    def test_add_account_inputrelname_max_lenth(self,realname,expected,Sys_user_manage_page):  
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
        "
        1. 输入姓名：9个汉字
        2. 输入姓名：10个汉字
        3. 输入姓名：11个汉字
        4. 输入姓名：输入9个英文字符
        5. 输入姓名：输入10个英文字符
        6. 输入姓名：输入11个英文字符"

        预期：
        "1. 可以输入
        2. 可以输入
        3. 只能输入到第10个汉字，无法输入第11个汉字
        4. 可以输入
        5. 可以输入
        6. 只能输入到第10个英文字符，无法输入第11个英文字符"    
        
    '''
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为数字加英文字符
        user_name = realname 
        #账号为数字加英文字符
        Account = 'test'+getString(num = 4) 
        #手机号码为特殊字符
        iphone = '17309013038'
        
        #期望
        test_expected = expected
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         

        
        
        
        #选择测试角色
        Sys_user_manage_page.add_role('测试')    
        
        #不点击保存
        Sys_user_manage_page.add_user_save()
        
        time.sleep(3)
        #断言
        assert Sys_user_manage_page.get_form_explain() == test_expected   
         
        
#         点击取消按钮        
        if test_expected != '':
            Sys_user_manage_page.add_cancel_click()
         



    
    @pytest.mark.run(order=11)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('新增用户')
    @pytest.mark.parametrize("account,expected",
                             [('123456789'+getString(10),''),
                              ('123456789'+getString(11),''),
                              ('123456789'+getString(12),'账号最大长度为20'),
                              ('cmiottest'+getString(10),''),
                              ('cmiottest'+getString(11),''),
                              ('cmiottest'+getString(12),'账号最大长度为20')])
    def test_add_account_inputaccount_max_lenth(self,account,expected,Sys_user_manage_page):  
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
        "
        1. 输入账号：19个数字+字符
        2. 输入账号：20个数字+字符
        3. 输入账号：21个数字+字符
        4. 输入账号：输入19个英文字符
        5. 输入账号：输入20个英文字符
        6. 输入账号：输入21个英文字符"

        预期：
        "1. 可以输入
        2. 可以输入
        3. 只能输入到第20个汉字，无法输入第21个汉字
        4. 可以输入
        5. 可以输入
        6. 只能输入到第20个英文字符，无法输入第21个英文字符"    
        
    '''
        Sys_user_manage_page.add_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='添加用户') == True
         
        #编辑用户信息
        
        #姓名为数字加英文字符
        user_name = 'test'+ getString(num = 4) 
        #账号
        Account = account
        #手机号码为特殊字符
        iphone = '17309013038'
        
        #期望
        test_expected = expected
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         

        
        
        
        #选择测试角色
        Sys_user_manage_page.add_role('测试')
        #点击保存
        Sys_user_manage_page.add_user_save()   
        time.sleep(3)
        #断言
        assert Sys_user_manage_page.get_form_explain() == test_expected   
        
        
#         点击取消按钮       
        if test_expected != '':
            Sys_user_manage_page.add_cancel_click()

    
    
    
    
    @pytest.mark.run(order=12)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('编辑用户')
    def test_update_account_Ok(self,Sys_user_manage_page):   
        '''                       
                测试用例编号:
                测试用例标题:新增账号，点击"确定"
                前置条件：已输入合法的姓名，合法账号，合法手机号，角色
                步骤：1. 点击"确定"
                预期：1. 当成功提交后，关闭弹窗，并刷新角色角色列表，新增账号出现在列表中（出现在最后？）               
        '''
        #点击新增按钮
        Sys_user_manage_page.update_btn_click()  
        #判断是否存在新增用户弹出框    
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
        
        #编辑用户信息
        user_name = 'name'+ getString(num = 4)
        Account = ''
        
        iphone = '17309013038'
        
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
        
        
        #选择用户角色    
        Sys_user_manage_page.add_role(name = '测试')
        Sys_user_manage_page.add_role(name = '开发') 
        Sys_user_manage_page.add_role(name = '运维')
        #点击保存按钮
        Sys_user_manage_page.update_user_save()
           
        #判断用户列表    
        assert Sys_user_manage_page.check_user_by_name(username = user_name)    
    
    
    
    
    @pytest.mark.run(order=13)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('编辑用户')
    def test_update_account_error_noRole(self,Sys_user_manage_page):    
        '''
        测试用例编号:
        测试用例标题:编辑账号信息界面，判断角色是否为空
        前置条件：打开编辑账号信息界面
        步骤："
        1. 输入姓名
        2. 输入账号
        3. 输入手机号
        4. 不勾选角色，点击确定"
 
        预期："1. 当未选角色时，复选框后红字提示“请选择角色”
        '''     
        already_selected_role = Sys_user_manage_page.get_User_table_value_by_key(key = '角色', index = 1)
        
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
         
        #编辑用户信息
        user_name = 'name'+getString(num = 4)  
        Account = 'Account'+getString(num = 4)  
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #不选择用户角色,输入为空
        for role in already_selected_role:
            Sys_user_manage_page.add_role(name = role)
         
        #点击保存按钮
        Sys_user_manage_page.update_user_save()
         
        assert Sys_user_manage_page.get_form_explain() == '请选择角色'  
         
        #点击取消
        Sys_user_manage_page.update_cancel_click()
        
        
    
    
    
    @pytest.mark.run(order=14)
    @pytest.mark.skipif(is_skip == 0 ,reason = 'test')  
     
    @allure.story('编辑用户')
    def test_update_account_error_noPhone(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:编辑账号信息界面，判断手机号是否为空
        前置条件：打开编辑账号信息界面
        步骤：
        1. 输入姓名
        2. 输入账号
        3. 选择角色
        4. 清空手机号码，点击确定"

 
        预期："1. 当手机号为空时，文本框后红字”请输入手机号“
        ''' 
    
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
         

        #手机号为空 
        Sys_user_manage_page.clear_addAccountForm_tel()
        time.sleep(5)
        #点击保存按钮
        Sys_user_manage_page.update_user_save()    
        
         
        assert Sys_user_manage_page.get_form_explain() == '请输入手机号'  
         
        #点击取消
        Sys_user_manage_page.update_cancel_click()



    @pytest.mark.run(order=15)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('编辑用户')
    def test_update_account_error_noRealName(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:编辑账号信息界面，判断姓名是否为空
        前置条件：打开编辑账号信息界面
        步骤：
        1. 输入账号
        2. 输入手机
        3. 选择角色
        4. 清空姓名，点击确定

 
        预期："1. 当账号为空时，文本框后红字“请填写账号名称”
        ''' 
    
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
         
        #编辑用户信息
        
        #姓名为空
        Sys_user_manage_page.clear_addAccountForm_realName()         

         
        #点击保存按钮
        Sys_user_manage_page.update_user_save()    
        time.sleep(5)
         
        assert Sys_user_manage_page.get_form_explain() == '请输入姓名'  
         
        #点击取消
        Sys_user_manage_page.update_cancel_click()
        
        
    
    
    @pytest.mark.run(order=16)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('编辑用户')
    def test_update_account_input_error_relname(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:编辑账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
        1. 姓名分别输入特殊字符_，~，@
    

 
        预期：
        1.失去焦点后，文本框提示'不允许使用特殊字符'
        '''
    
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
         
        #编辑用户信息
        
        #姓名为特殊字符
        user_name = '_~@'+getString(num = 4) 
        #账号为数字加英文字符
        Account = 'test'+getString(num = 4) 
        #手机号码为特殊字符
        iphone = '17309013038'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #使用默认角色        
        #点击保存按钮
        Sys_user_manage_page.update_user_save()       
        
        assert Sys_user_manage_page.get_form_explain() == '不允许使用特殊字符'  
        
        #编辑点击取消
        Sys_user_manage_page.update_cancel_click()  
    
    
    
    @pytest.mark.run(order=17)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
      
    @allure.story('编辑用户')
    def test_update_account_input_error_iphone(self,Sys_user_manage_page): 
        '''
        测试用例编号:
        测试用例标题:编辑账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
    
        1. 手机分别输入特殊字符_，~，@，-

 
        预期：
        1. 失去焦点后，文本框提示'请输入手机号'
        '''
    
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.addDialog_title,
                                                 text='编辑用户') == True
         
        #编辑用户信息
        
        #姓名为数字加英文字符
        user_name = 'test'+getString(num = 4) 
        #账号为数字加英文字符
        Account = 'test'+getString(num = 4) 
        #手机号码为特殊字符
        iphone = '@~-'
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         
        #默认使用原来角色
        
        #点击保存按钮
        Sys_user_manage_page.update_user_save()       
        
        assert Sys_user_manage_page.get_form_explain() == '请输入手机号'     
        
        #点击取消
        Sys_user_manage_page.update_cancel_click()
        
    
    
    @pytest.mark.run(order=18)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')
    @pytest.mark.parametrize("realname,expected",
                             [('中移物联网中国移动',''),
                              ('中移物联网中国移动一',''),
                              ('中移物联网中国移动一二','姓名最大长度为10'),
                              ('cmiottest',''),
                              ('cmiottestY',''),
                              ('cmiottestYY','姓名最大长度为10')]) 
      
    @allure.story('编辑用户')
    def test_update_account_inputrelname_max_lenth(self,realname,expected,Sys_user_manage_page):  
        '''
        测试用例编号:
        测试用例标题:新增账号信息界面输入框特殊字符测试
        前置条件：打开编辑账号信息界面
        步骤：
        "
        1. 输入姓名：9个汉字
        2. 输入姓名：10个汉字
        3. 输入姓名：11个汉字
        4. 输入姓名：输入9个英文字符
        5. 输入姓名：输入10个英文字符
        6. 输入姓名：输入11个英文字符"

        预期：
        "1. 可以输入
        2. 可以输入
        3. 只能输入到第10个汉字，无法输入第11个汉字
        4. 可以输入
        5. 可以输入
        6. 只能输入到第10个英文字符，无法输入第11个英文字符"    
        
    '''
        Sys_user_manage_page.update_btn_click()   
        assert Sys_user_manage_page.is_text_in_element(locator=Sys_user_manage_page.updateDialog_title,
                                                 text='编辑用户') == True
         
        #编辑用户信息
        
        #姓名为数字加英文字符
        user_name = realname 
        #账号使用默认
        Account = ''
        #手机号码为默认
        iphone = '17309013038'
        
        #期望
        test_expected = expected
         
        Sys_user_manage_page.input_add_user_data(name = user_name, 
                                                  loginAccount = Account, 
                                                  iphone = iphone)
         

        
        
        
        #使用默认角色
        #Sys_user_manage_page.add_role('测试')
        
         
        
        Sys_user_manage_page.update_user_save()    
        
        assert Sys_user_manage_page.get_form_explain() == test_expected  
        
#         点击取消按钮       
        if test_expected != '':
            Sys_user_manage_page.update_cancel_click()
        
             
    

        
    

    @pytest.mark.run(order=21)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
    @allure.story('通过用户名称查询')
    def test_query_by_username(self,Sys_user_manage_page):   
        '''
                  测试用例编号:
                  测试用例标题:验证姓名查询
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.输入姓名"superadmin"
                  2.点击查询按钮
          
                  预期：
                  1. 可以输入
                  2. 返回模糊查询结果
                  
        '''
        #刷新界面
        Sys_user_manage_page.refresh()
        
        #用户姓名输入框输入"superadmin"     
        Sys_user_manage_page.input_name(username = 'superadmin')   
        
        #点击查询按钮
        Sys_user_manage_page.query_click()     
        
        #断言用户名是否在列表中
        assert 'superadmin' in Sys_user_manage_page.get_User_table_value_by_key(key = '姓名', index = 1)    
        
    
    
    @pytest.mark.run(order=22)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
    @allure.story('通过角色查询')
    def test_query_by_role(self,Sys_user_manage_page):   
        '''
                  测试用例编号:
                  测试用例标题:验证角色查询
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.选择角色“测试”
                  2.点击查询按钮
          
                  预期：
                  1. 可以选择
                  2. 返回模糊查询结果
                  
        '''
        #刷新界面
        Sys_user_manage_page.refresh()
        
        #角色选择"测试"       
        Sys_user_manage_page.select_role_by_index(index = 1)   
        
        #点击查询按钮
        Sys_user_manage_page.query_click() 
        
        #断言"测试"是否在列表中
        assert '测试' in Sys_user_manage_page.get_User_table_value_by_key(key = '角色', index = 1)
        
        
        

    @pytest.mark.run(order=23)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
    @allure.story('通过状态查询已启用角色')
    def test_query_by_status_Ok(self,Sys_user_manage_page):   
        '''
                  测试用例编号:
                  测试用例标题:通过状态查询已启用角色
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.选择状态“已启用”
                  2.点击查询按钮
          
                  预期：
                  1. 可以选择
                  2. 返回模糊查询结果
                  
        '''
        
        #刷新界面
        Sys_user_manage_page.refresh()
        #选择状态“已启用”       
        Sys_user_manage_page.select_status_by_index(index = 1) 
        
        #点击查询按钮
        Sys_user_manage_page.query_click() 
        
        #断言"启用"是否在列表中
        assert '启用' in Sys_user_manage_page.get_User_table_value_by_key(key = '状态', index = 1)   
        
        

    @pytest.mark.run(order=24)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
    @allure.story('通过状态查询已禁用角色')
    def test_query_by_status_No(self,Sys_user_manage_page):   
        '''
                  测试用例编号:
                  测试用例标题:通过状态查询已启用角色
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.选择状态“已禁用”
                  2.点击查询按钮
          
                  预期：
                  1. 可以选择
                  2. 返回模糊查询结果
                  
        '''
        
        #刷新界面
        Sys_user_manage_page.refresh()
        
        #选择状态“已禁用”      
        Sys_user_manage_page.select_status_by_index(index = 2) 
        
        #点击查询按钮
        Sys_user_manage_page.query_click() 
        
        #断言"禁用"是否在列表中
        assert '禁用' in Sys_user_manage_page.get_User_table_value_by_key(key = '状态', index = 1)     
     

        
    
    @pytest.mark.run(order=25)
    @pytest.mark.skipif(is_skip == 0,reason = 'test')   
    @allure.story('验证联合查询')
    def test_query_by_all(self,Sys_user_manage_page):    
        '''
                  测试用例编号:
                  测试用例标题:验证联合查询
                  前置条件：打开编辑账号信息界面
                  步骤：
                  "
                  1.姓名输入“superadmin”
                  2.角色输入“全部”
                  3.状态选择“已启用”
          
                  预期：
                  1. 可以输入
                  2. 可以选择
                  3.返回联合查询结果
                  
        '''
        #刷新界面
        Sys_user_manage_page.refresh()
        
        #姓名输入“superadmin”
        Sys_user_manage_page.input_name(username = 'superadmin')
        #角色输入“全部”
        Sys_user_manage_page.select_role_by_index(index = 0)
        #状态选择“已启用”
        Sys_user_manage_page.select_status_by_index(index = 1) 
        
        #点击查询按钮
        Sys_user_manage_page.query_click() 
        
        #断言"禁用"是否在列表中
        assert 'superadmin' in Sys_user_manage_page.get_User_table_value_by_key(key = '姓名', index = 1) 
        
        
        #断言"启用"是否在列表中
        assert '启用' in Sys_user_manage_page.get_User_table_value_by_key(key = '状态', index = 1) 
        
    
        
        
        
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
    
    
    
    