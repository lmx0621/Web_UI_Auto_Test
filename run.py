import shutil,os,pytest
result_pth = r'C:\Users\lyc\workspace\Web_Automation-master\Testsuit\result'    
def remove(result_pth): 
    if os.path.exists(result_pth):  
        shutil.rmtree(result_pth)   
        os.mkdir(result_pth)    
    else:       
        os.mkdir(result_pth)    
    
if __name__ == '__main__':  
    remove(result_pth)
    pytest.main(['-s', '-q','--alluredir', result_pth])
    os.system('allure serve {path}'.format(path = result_pth ))
    