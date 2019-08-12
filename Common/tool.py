# -- coding: utf-8 --
'''
Created on 2019年7月15日

@author: lyc
'''
import random   
import string
def getString(num):  
    '''根据参数返回多少位字符串'''  
    return ''.join(random.sample(string.ascii_letters + string.digits, num))


# print(string.ascii_letters)
if __name__ == '__main__':  
    print(getString(13))
         
