from base64 import b64decode
from urllib.parse import unquote

strings = ['W7ddM8ktWONdRW', 'EuSWxe7dMmowiW', 'fNi9emonqmkg','WQpcV8k5WOLeW4lcHZC','WPVdI08bj29Cd1a','iqDYW7Xi','fZhdHW','W4hdKSkzuSoE','W67cL8k/xG','W4/dKCkfqSoqcff+v28','DSkxW7tcL8oAW5K8','WPRdLJtcRWKnW5tcGCox','xCkBWRNdS8onWRPWWRzvdW','strephJcTrRdOq','WO7dOt/dPZqQWQ0','gcFdMSk4z8kB','i3VdNSoTWO3dNg0','z0zKC8oaBq','WPpdNSkfxNZdPmkiW4GYW4G','ob3dPcxdIZldTstdJZZcUWzCACoZWPq','b8o/wcae','uYVcN0O','WRFdMhpcJY4UhuhcQ0BdLfddQa','g3SKcSofqW','WPpcHSodbSosj3HDz1O','W4PdwtZdOmkzWQyiW7vWy8o1','WQxcN8kUx3KH','qZ05','tCkOjCoCWQJdV8kHWRVcSLZdRSo8qq','W65WWO4','WQJcHcZdJg8ZtL3cI1FdPWRdQ0iKkG','W7SzWPiqtduzsCk1fwmt','cCkpDgVcTIVcI3CVWQKpqtFdO8oYW4G','WPC0Emokxmkkes/dNsWEW7W','a8khC2u','CfHiW610bCozWRe','b3hdG2O','W6hdRCkQW74spKVdTJu3WP0','BKmUWPC','p1TXCfldJCompXi','W4RcVsFdQq','W5GgW4KtW5JdT3SN','a3tcMW','jvT+','WQ5YW4W','WOXzdJH+W5RdUGH4WQXJWPa','lfTLza','W5FdItxcTaulW4W','u8oNqZSceH3cUc0','hw3dIxddISkYehr1sh/cNJ3dOMe','p1TWCfldJCompXi','o8kiW7xcJmowW58KWQrL','gmkgEhC','W65XW43dLSkrAuP5W60','wmozWRadgcKM','ccvUxa','rsNcMI3dKSoUtwLoavtcHIe','W5hdLSkFrG','jIJcNHhdP8kosWJcTMTJoIK','WO7dSMW','WOJcIX/cGG','a3xdM8oUWQpdMmkenCkT','WQbyW5vue3C','e8kWA8kcW5j2WQFcSJHeW4RcQCka','C3j0W5FdV8o1ebal','WOOBagdcVCoLWPe5W4i','E8kuW67cGmoE','rCozWQWEcsaXoCo1W7G','aYJcLae','DuiLWOu','WOdcOCodW4RcPN/dUJPC','WPFdHtpcSX4hW4RdN8kgssyBdG','W6/dKCkhWP7dSYddTSkRt3S','W5Ohg2VcU8oeWO09WP4','WQZdJ8odW4ddUtxdRmk2rwC','scRcLfG','eNdcO08JWQVcImkx','W75QW74','W6nWWOVdLSkcEfbLWRa','rcPiphNdTaNdOapdPd9DqCkFumoR','tmkHiCoDWQ7cPCobWOBcKuBdJW','uhW+j8oitSkBwG','WRhcS8kYWR0','W4hcISoFcNa','WOPFdJj1W5VdGWPrWQjoWOK','WQTeW4nc','c8oqWRaddsa','WPpcIHtcKa','u23dHSo2','uNiuEd3dQtRdLXRdIaC3','WPhdP8o7W6RcK23dHbK','r3VcH8oTiCkAk8kfq8koW4G','WQbEW5q','BdRdHq','pYtcMCkQW5dcGdFdJWukWQbcW4S']

def _0x596fa7(_0x1e9a71, _0x4da13d):
    _0x4e38e4 = []
    _0x10f9e0 = 0
    _0x237a4b = ''
    _0x170325 = ''
    _0x50f95f = ''
    _0x1e9a71 = str(b64decode(_0x1e9a71 + (4 - (len(_0x1e9a71) % 4)) * '='));
    for i in range(len(_0x1e9a71)):
        _0x50f95f += '%' + hex(ord(_0x1e9a71[i]))[2:]
    
    _0x1e9a71 = unquote(_0x50f95f);

    for i in range(256):
        _0x4e38e4.append(i);
    for i in range(256):
        _0x10f9e0 = (_0x10f9e0 + _0x4e38e4[i] + ord(_0x4da13d[i % len(_0x4da13d)])) % 256
        _0x237a4b = _0x4e38e4[i]
        _0x4e38e4[i] = _0x4e38e4[_0x10f9e0]
        _0x4e38e4[_0x10f9e0] = _0x237a4b

    
    _0x1f7610 = 0x0
    _0x10f9e0 = 0x0
    for _0x1f1904 in range(len(_0x1e9a71)):
        _0x1f7610 = (_0x1f7610 + 0x1) % 0x100;
        _0x10f9e0 = (_0x10f9e0 + _0x4e38e4[_0x1f7610]) % 0x100;
        _0x237a4b = _0x4e38e4[_0x1f7610];
        _0x4e38e4[_0x1f7610] = _0x4e38e4[_0x10f9e0];
        _0x4e38e4[_0x10f9e0] = _0x237a4b;
        _0x170325 += chr(ord(_0x1e9a71[_0x1f1904]) ^ _0x4e38e4[(_0x4e38e4[_0x1f7610] + _0x4e38e4[_0x10f9e0]) % 0x100]);
    return _0x170325;

def decode(a, b):
    return _0x596fa7(strings[a - 0x1da], b)

print(decode(0x20c, 'G0Z('))