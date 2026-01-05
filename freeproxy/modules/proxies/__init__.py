'''initialize'''
from .base import BaseProxiedSession
from ..utils import BaseModuleBuilder
from .ihuan import IhuanProxiedSession
from .geonode import GeonodeProxiedSession
from .qiyunip import QiyunipProxiedSession
from .kxdaili import KxdailiProxiedSession
from .proxydb import ProxydbProxiedSession
from .spysone import SpysoneProxiedSession
from .jiliuip import JiliuipProxiedSession
from .iplocate import IPLocateProxiedSession
from .proxifly import ProxiflyProxiedSession
from .proxyhub import ProxyhubProxiedSession
from .proxylist import ProxylistProxiedSession
from .kuaidaili import KuaidailiProxiedSession
from .thespeedx import TheSpeedXProxiedSession
from .tomcat1235 import Tomcat1235ProxiedSession
from .freeproxydb import FreeProxyDBProxiedSession
from .proxyscrape import ProxyScrapeProxiedSession
from .freeproxylist import FreeproxylistProxiedSession


'''ProxiedSessionBuilder'''
class ProxiedSessionBuilder(BaseModuleBuilder):
    REGISTERED_MODULES = {
        'ProxiflyProxiedSession': ProxiflyProxiedSession,
        'FreeproxylistProxiedSession': FreeproxylistProxiedSession,
        'IhuanProxiedSession': IhuanProxiedSession,
        'KuaidailiProxiedSession': KuaidailiProxiedSession,
        'KxdailiProxiedSession': KxdailiProxiedSession,
        'ProxydbProxiedSession': ProxydbProxiedSession,
        'ProxyhubProxiedSession': ProxyhubProxiedSession,
        'ProxylistProxiedSession': ProxylistProxiedSession,
        'QiyunipProxiedSession': QiyunipProxiedSession,
        'SpysoneProxiedSession': SpysoneProxiedSession,
        'Tomcat1235ProxiedSession': Tomcat1235ProxiedSession,
        'IPLocateProxiedSession': IPLocateProxiedSession,
        'JiliuipProxiedSession': JiliuipProxiedSession,
        'TheSpeedXProxiedSession': TheSpeedXProxiedSession,
        'FreeProxyDBProxiedSession': FreeProxyDBProxiedSession,
        'ProxyScrapeProxiedSession': ProxyScrapeProxiedSession,
        'GeonodeProxiedSession': GeonodeProxiedSession,
    }


'''BuildProxiedSession'''
BuildProxiedSession = ProxiedSessionBuilder().build