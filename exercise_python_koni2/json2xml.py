"""
○使用外部パッケージ
    poetry add BeautifulSoup4
    poetry add lxml
    poetry add dicttoxml
○参考
    jsonからxmlについて
        https://qiita.com/kkdmgs110/items/9317057facb60764ed74
    BeautifulSoupやパーサについて
        https://qiita.com/PND/items/06e1053eeed69ec4f418
        https://lets-hack.tech/programming/languages/python/beautifulsoup-xml/
○内容
    指定したjsonファイルを読み込み、xmlに変換する。その後パース(見やすく)し、ファイル出力する。
    ここでは「jsonfile.json」を読み込み、「xmlfile.xml」を出力している。
"""

import json
from bs4 import BeautifulSoup
import dicttoxml


def json2xml():
    """json形式をxml形式に変換する"""
    translatedjsonfile = jsontodictfile(readjsonfile())
    translatedxmlfile = dicttoxmlfile(translatedjsonfile)
    writexmlfile(shapingxmlfile(translatedxmlfile))
    print("jsonからxmlを作成完了")


def readjsonfile():
    """指定したjsonを読み込んで返す"""
    targetfile = open(r"readfiles\jsonfile.json", "r")
    return targetfile


def writexmlfile(writefile):
    """指定したxmlに書き込んで返す"""
    with open(r"xmlfile.xml", "wt") as xmlfile:
        xmlfile.write(writefile)
        return xmlfile


def shapingxmlfile(xmlfile):
    """外部モジュール'BeautifulSoup4'を使用する。
    xmlを整形し返す"""
    shapingfile = BeautifulSoup(xmlfile, "lxml")
    return shapingfile.prettify()


def jsontodictfile(targetfile):
    """jsonをdictに変換して返す"""
    translateddictfile = json.load(targetfile)
    return translateddictfile


def dicttoxmlfile(targetfile):
    """dictをxmlに変換して返す"""
    translatedxmlfile = dicttoxml.dicttoxml(targetfile)
    return translatedxmlfile


if __name__ == "__main__":
    json2xml()
