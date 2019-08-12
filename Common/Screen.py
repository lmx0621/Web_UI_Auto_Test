# -- coding: utf-8 --
'''
Created on 2019年7月25日

@author: lyc
'''


class screen(object):   
    '''截图函数'''  
    
    def __init__(self,obj):  
        self.obj =  obj   
        
    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                self.obj.allure_pic_report()        
                raise
        return inner
        