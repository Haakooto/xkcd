import webbrowser, sys, random as rand, json, requests

baseurl = "https://xkcd.com/"  # sets baseurl for combination with number
new = requests.get("https://xkcd.com/info.0.json").json()[
    "num"
]  # finds the number of the newest xkcd


def open_xkcd(num):
    url = baseurl + str(num)
    webbrowser.open(url)


def check_valid(num):
    try:
        num = int(num)
    except:
        open_xkcd(new)
        print("yup")
    if num <= new and 0 < num:
        open_xkcd(num)
    else:
        open_xkcd(new)


def random():
    num = rand.randint(1, new)
    open_xkcd(num)


def newest():
    open_xkcd(new)


if __name__ == "__main__":
    if len(sys.argv) != 1:
        check_valid(sys.argv[-1])
    else:
        random()
