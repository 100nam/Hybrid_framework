import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationurl():
        url = config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
    @staticmethod
    def getUseremail():
        username = config.get('common info', 'user-email')
        return username
