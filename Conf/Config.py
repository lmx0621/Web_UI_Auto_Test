# -*- coding: utf-8 -*-
# @Time    : 2018/7/25 上午10:46
# @File    : Config.py

from configparser import ConfigParser
from Common import Log
import os

class Config:
    # titles:
    TITLE_DEBUG = "private_debug"
    TITLE_RELEASE = "online_release"
    TITLE_EMAIL = "mail"
    TITLE_DB = "db"

    # values:
    # [debug\release]
    VALUE_TESTER = "tester"
    VALUE_ENVIRONMENT = "environment"
    VALUE_VERSION_CODE = "versionCode"
    VALUE_HOST = "host"
    VALUE_LOGIN_HOST = "loginHost"
    VALUE_LOGIN_INFO = "loginInfo"
    VALUE_LOGIN_URL = "loginUrl"
    # [mail]
    VALUE_SMTP_SERVER = "smtpserver"
    VALUE_SENDER = "sender"
    VALUE_RECEIVER = "receiver"
    VALUE_USERNAME = "username"
    VALUE_PASSWORD = "password"
    
    #[db]  
    VALUE_DB_HOST = "db_host"
    VALUE_DB_PORT = "db_port"
    VALUE_DB_USER = "db_user"
    VALUE_DB_PASSWD = "db_passwd"
    VALUE_DB_NAME = "db_name"
    VALUE_DB_CHARSET = "db_charset"
    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'
        self.pic_path = Config.path_dir +'/Picture/' #截图存放位置
        
        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！")

        self.config.read(self.conf_path, encoding='utf-8')

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        #测试环境host
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)
        self.login_url_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_URL)
        
        #上线环境端口
        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)  
        
        
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)
        self.login_url_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_URL)
        
        
        self.smtpserver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_EMAIL, Config.VALUE_PASSWORD)


        self.db_host = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_HOST) 
        self.db_port = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_PORT) 
        self.db_user = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_USER)
        self.db_passwd = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_PASSWD)
        self.db_name = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_NAME)   
        self.db_charset = self.get_conf(Config.TITLE_DB, Config.VALUE_DB_CHARSET) 
        
        
    def get_conf(self, title, value):
        """
        配置文件读取
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        配置文件修改
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
    配置文件添加
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f) 
if __name__ == '__main__':  
    obj = Config()  
    print(type(obj.login_url_debug))
    
