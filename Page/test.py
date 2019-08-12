# -- coding: utf-8 --
'''
Created on 2019年8月6日

@author: lyc
'''

from Common.ChexingPage import Chengxing     
import allure,pytest,os,shutil

@allure.feature('测试类')
class Sys_user_manage(Chengxing):   
    def __init__(self): 
        super(Sys_user_manage, self).__init__()
        
    def testcase(self): 
        self.login(username = 'superadmin', password ='123456') 
        self.allure_pic_report()
        
if __name__ == '__main__':
   
    if os.path.exists(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result'):      
        shutil.rmtree(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')  
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')   
    else:   
        os.mkdir(r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result')
       
    result_pth=os.path.join(os.path.abspath(os.path.dirname(os.getcwd())+os.path.sep+".."),'result').replace('\\','/')      
    pytest.main(['-s', '-q', 'Test_forbidden_unfreeze_reset.py','--alluredir', result_pth])
    os.system('allure serve {path}'.format(path = result_pth ))