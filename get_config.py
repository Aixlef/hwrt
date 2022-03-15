import configparser

def qos_constraint():
    conf = configparser.ConfigParser()
    conf.read('config.ini', encoding='utf-8')
    qos_constraint = conf.get('config', 'qos_constraint')