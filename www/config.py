
'''
configration
'''
class Dic(dict):
    def __init__(self,names=(),values=(),**kw):
        super(Dic,self).__init__(**kw)
        #含有names values形式的时候进行zip操作
        for k ,v in zip(names,values):
            self[k] =v
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s" % item)
    def __setattr__(self, key, value):
        self[key]=value
#override_config 覆盖default_config
def merge(default,override):
    r ={}
    for k , v in default.items():
        if k in override:
            #若还是dict的情况下：
            if isinstance(k,dict):
                r[k]= merge(v,override[k])
            else :
                r[k] =override[k]
        else:
            r[k]=v
    return  r

def toDic(dic):
    D =Dic()
    for k ,v in dic.items():
        D[k]=toDic(v) if isinstance(v,dict) else v
    return  D

from www import  config_override
from  www import  config_default
configs=config_override.configs
#进行对比：
try:
 configs=merge(config_default.configs,configs)
except ImportError:
     pass
configs =toDic(configs)



















