'''initialize'''
from .base import BaseProxiedSession
from ..utils import BaseModuleBuilder
from .ihuan import IhuanProxiedSession
from .geonode import GeonodeProxiedSession
from .qiyunip import QiyunipProxiedSession
from .kxdaili import KxdailiProxiedSession
from .proxydb import ProxydbProxiedSession
# from .spysone import SpysoneProxiedSession
from .jiliuip import JiliuipProxiedSession
# from .iplocate import IPLocateProxiedSession
from .proxifly import ProxiflyProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .proxylist import ProxylistProxiedSession
from .kuaidaili import KuaidailiProxiedSession
# from .thespeedx import TheSpeedXProxiedSession
# from .tomcat1235 import Tomcat1235ProxiedSession
# from .freeproxydb import FreeProxyDBProxiedSession
from .proxyscrape import ProxyScrapeProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'IhuanProxiedSession': IhuanProxiedSession,
        'GeonodeProxiedSession': GeonodeProxiedSession,
        'QiyunipProxiedSession': QiyunipProxiedSession,
        'KxdailiProxiedSession': KxdailiProxiedSession,
        'ProxydbProxiedSession': ProxydbProxiedSession,
        # 'SpysoneProxiedSession': SpysoneProxiedSession,
        'JiliuipProxiedSession': JiliuipProxiedSession,
        # 'IPLocateProxiedSession': IPLocateProxiedSession,
        'ProxiflyProxiedSession': ProxiflyProxiedSession,
        'ProxyhubProxiedSession': ProxyhubProxiedSession,
        'ProxylistProxiedSession': ProxylistProxiedSession,
        'KuaidailiProxiedSession': KuaidailiProxiedSession,
        # 'TheSpeedXProxiedSession': TheSpeedXProxiedSession,
        # 'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession,
        # 'FreeProxyDBProxiedSession': FreeProxyDBProxiedSession,
        'ProxyScrapeProxiedSession': ProxyScrapeProxiedSession,
        'FreeproxylistProxiedSession': FreeproxylistProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build