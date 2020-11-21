# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import json
from tabulate import tabulate
from attrdict import AttrDict

class Statik(object):
    def __init__(self, kekik_json):
        super().__init__()
        self.kekik_json = kekik_json

    def veri(self):
        "json verisi döndürür."
        return self.kekik_json or None

    def nesne(self, index:int=0) -> AttrDict:
        "json verisini python nesnesine dönüştürür"
        return AttrDict(self.kekik_json['veri'][0]) if index == 0 else AttrDict(self.kekik_json['veri'][index])

    def gorsel(self, girinti:int=2, alfabetik:bool=False):
        "oluşan json verisini insanın okuyabileceği formatta döndürür."
        return json.dumps(self.kekik_json, indent=girinti, sort_keys=alfabetik, ensure_ascii=False) if self.kekik_json else None

    def tablo(self, tablo_turu:str='psql'):
        "tabulate verisi döndürür."
        return tabulate(self.kekik_json['veri'], headers='keys', tablefmt=tablo_turu) if self.kekik_json else None

    def anahtarlar(self):
        "kullanılan anahtar listesini döndürür."
        return [anahtar for anahtar in self.kekik_json['veri'][0].keys()] if self.kekik_json else None