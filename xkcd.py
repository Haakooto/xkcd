import numpy as xkcd
import json as Xkcd
import requests as XKcd
from PIL import Image as xkcdxkcd
from io import BytesIO as XKCD
from bs4 import BeautifulSoup as xKcd

xkCd = "https://xkcd.com/"
xkcD = XKcd.get("https://xkcd.com/info.0.json").json()["num"]

xkCD = xkcd.random.randint(1, xkcD)
XkCd = xkCd + str(xkCD)

XkcD = XKcd.get(XkCd)

XKCd = xKcd(XkcD.content, "html.parser")
xkcd = str(XKCd.find("div", {"id": "comic"}))
XKcD = xkcd.find("src")
XkCD = xkcd.find(".png")
xkcd = xkcd[XKcD + 5: XkCD + 4]

XkcD = XKcd.get("http:" + xkcd)
xKCD = xkcdxkcd.open(XKCD(XkcD.content))
xKCD.save("xkcd.png")

XKCDXKCD = xkcdxkcd.open("xkcd.png")
XKCDXKCDXKCD, XKCDXKCDXKCDXKCD = XKCDXKCD.size
XKCDXKCDXKCDXKCDXKCD = XKCDXKCDXKCDXKCD / XKCDXKCDXKCD
XKCDXKCDXKCDXKCDXKCDXKCD = 120
XKCDXKCDXKCDXKCDXKCDXKCDXKCD = XKCDXKCDXKCDXKCDXKCD * XKCDXKCDXKCDXKCDXKCDXKCD * 0.55
XKCDXKCD = XKCDXKCD.resize((XKCDXKCDXKCDXKCDXKCDXKCD, int(XKCDXKCDXKCDXKCDXKCDXKCDXKCD)))
XKCDXKCD = XKCDXKCD.convert("L")
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = XKCDXKCD.getdata()
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = ["X", "K", "C", "Ð", "D", "x", "k", "c", "d", "×", " "]
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = [
    XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD[XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD // 25] for XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD in XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD
]
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = "".join(XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD)
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = len(XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD)
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = [
    XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD[XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD : XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD + XKCDXKCDXKCDXKCDXKCDXKCD]
    for XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD in range(0, XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD, XKCDXKCDXKCDXKCDXKCDXKCD)
]
XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD = "\n".join(XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD)
print(XKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCDXKCD)
