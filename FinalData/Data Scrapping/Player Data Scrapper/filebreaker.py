

import csv
import os
import re

MAX_CHUNKS = 30


def writeRow(idr, row):
    with open("player_%d.txt" % idr, 'a') as file:
        writer = csv.writer(file, delimiter=',', quotechar='\"', quoting=csv.QUOTE_ALL)
        writer.writerow(row)

def cleanup():
    for f in os.listdir("."):
        if re.search("player_.*", f):
            os.remove(os.path.join(".", f))

def main():
    cleanup()
    with open("player.txt", 'r') as results:
        r = csv.reader(results, delimiter=',', quotechar='\"')
        idr = 1
        for i, x in enumerate(r):
            temp = i + 1
            if not (temp % (MAX_CHUNKS + 1)):
                idr += 1
            writeRow(idr, x)

#if __name__ == "__main__": main()

