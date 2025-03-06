import configparser



config=configparser.RawConfigParser()
config.read(".\\Configuration\\ConfigData.ini")

class ReadConfig:

    @staticmethod
    def getBaseUrl():
        url=config.get('commondata','base_Url')
        return url

    @staticmethod
    def getname():
        username = config.get('commondata', 'username')
        return username

    @staticmethod
    def getpwd():
        password = config.get('commondata', 'Password')
        return password

    @staticmethod
    def getcommonData(rowkey, key_value):
        value=config.get(rowkey, key_value)
        return value





