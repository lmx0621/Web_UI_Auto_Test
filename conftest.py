import pytest,os
from Page.sys_user_manage import Sys_user_manage    
from Page.sys_role_manege import Sys_role_manage
driver = None

@pytest.fixture(scope='class', autouse=False)
def Sys_user_manage_page():     
    print('初始化用例')
    global driver
    if driver is None:
        driver = Sys_user_manage('Chrome')      
        driver.login('superadmin', '123456')
    yield driver    
    print('结束用例')
    driver.close_Browser()  
    driver = None

@pytest.fixture(scope='class', autouse=False)    
def Sys_role_manage_page():     
    print('初始化用例')
    global driver
    if driver is None:
        driver = Sys_role_manage('Chrome')      
        driver.login('superadmin', '123456')    
        driver.click_menu_li(name = '角色管理')
    yield driver    
    print('结束用例')
    driver.close_Browser()  
    driver = None



def _picture():    
    driver.allure_pic_report()    


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    hook pytest失败
    :param item:
    :param call:
    :return:
    '''
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    # we only look at actual failing test calls, not setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        _picture()
    
    
    
