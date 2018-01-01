#!/usr/local/bin/python3

import urllib.request
import argparse
import json
import sys
from datetime import datetime

server = ""
port = 10772
target = "http://" + server + ":" + str(port) + "/api/"

def main():
    parser = argparse.ArgumentParser(
            description = 'chinachu remote controller'
    )

    parser.add_argument('mode', action='store')

    args = parser.parse_args()

    if args.mode == 'reserves':
        reserves()
    elif args.mode == 'recorded':
        recorded()
    else:
        __exit(1, "mode does not exist")

def reserves():
    data = __getData("reserves")
    __showData(data)

def recorded():
    data = __getData("recorded") 
    __showData(data)

def __getData(method):
    with urllib.request.urlopen(target + method + ".json") as res:
        data = res.read().decode("utf-8")

    if data is not None:
        return json.loads(data)
    else:
        __exit(1, "the data is empty.")

def __showData(data):
    for item in data:
        start_time = datetime.fromtimestamp(item["start"] / 1000)
        print("ID:         " + item["id"])
        print("Title:      " + item["title"])
        print("Category:   " + item["category"])
        print("Date:       " + str(start_time.year) + "/" + str(start_time.month) + "/" + str(start_time.day))
        print("Start Time: " + str(start_time.hour) + ":" + str(start_time.minute))

def __exit(return_code, message):
    print(message)
    sys.exit(return_code)

if __name__ == '__main__':
    main()
