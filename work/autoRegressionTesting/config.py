#coding=utf-8
import yaml

class Config():
    def __init__(self,configPath):
        self._config = yaml.safe_load(open(configPath if configPath else "config.yml","r",encoding="utf-8"))

    def getCfgValue(self,*args):
        ret = self._config
        for arg in args:
            ret = ret.get(arg)
        return ret
