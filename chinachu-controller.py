#!/usr/local/bin/python3

import urllib.request
import argparse
import json

from datetime import datetime

server = "node02.data-hotel.intranet"
port = 10772

target = "http://" + server + ":" + str(port) + "/api/"


def main():
    with urllib.request.urlopen(target + "reserves.json") as res:
        data = res.read().decode("utf-8")
    
    decoded_data = json.loads(data)

    for item in decoded_data:
        start_time = datetime.fromtimestamp(item["start"] / 1000)

        print("Title:      " + item["title"])
        print("Category:   " + item["category"])
        print("Date:       " + str(start_time.year) + "/" + str(start_time.month) + "/" + str(start_time.day))
        print("Start Time: " + str(start_time.hour) + ":" + str(start_time.minute))

if __name__ == '__main__':
    main()
