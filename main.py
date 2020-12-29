import hashlib
import argparse
import os
import time
from classes.progress import Progress
import colorama
colorama.init()


def dohash(text):
    return hashlib.md5(text.encode()).hexdigest()


class Hashcrack:
    def __init__(self):
        self.start = None
        self.args = {}
        self.verbose = False
        self.passes = []
        self.passlen = 0
        self.getargs()
        self.checkargs()
        self.readpass()
        self.bruteforce()

    def getargs(self):
        ap = argparse.ArgumentParser()
        ap.add_argument('-p', "--hashed", type=str, help="Hashed password to break.")
        ap.add_argument('-d', "--dict", type=str, help="Dictionary of passes for brute force.")
        ap.add_argument("--hash", type=str, help="Get hash of given text.")
        ap.add_argument("-v", "--verbose", action="store_true", help="Verbose mode for this script.")
        self.args = vars(ap.parse_args())
        self.verbose = self.args['verbose']

    def checkargs(self):
        self.msg("Checking Arguments")
        if self.args['hash'] not in [None, ""]:
            print(f"{self.args['hash']} => {dohash(self.args['hash'])}")
            exit()
        toexit = False
        if self.args['hashed'] in [None, '']:
            print("Please specify hashed password!")
            toexit = True
        if self.args['dict'] in [None, ''] or not os.path.exists(self.args['dict']):
            print("Dictionary doesn't exist!")
            toexit = True
        if toexit:
            exit()

    def readpass(self):
        self.msg("Reading Password Dict")
        with open(self.args['dict'], 'r') as f:
            for line in f.readlines():
                self.passes.append(line.rstrip('\n'))
        self.passlen = len(self.passes)

    def bruteforce(self):
        self.msg("Starting Brute Forcing")
        prg = Progress(tabs=int(os.get_terminal_size()[0]/2), spc="-")
        self.start = time.time()
        for index, pasw in enumerate(self.passes):
            pasw = pasw.replace('\n', '')
            cur_hash = hashlib.md5(pasw.encode()).hexdigest()
            if self.args['hashed'] == cur_hash:
                print(" " * int(os.get_terminal_size()[0] * 0.75), end="\r")
                self.msg("Match Found")
                print("Brute force completed!\nPassword:", u"\033[1m" + pasw + u"\033[0m")
                break
            if index % 1000000 == 0:
                prg.next(cur_perc=round(index / self.passlen, 2))

    def msg(self, text):
        BLUE = "\033[96m"
        END = "\033[0m"
        if self.verbose:
            print(f"{BLUE}>>{END} {text} {BLUE}<<{END}")


# e5d9dee0892c9f474a174d3bfffb7810 => root1
if __name__ == '__main__':
    print()
    cracker = Hashcrack()
    if cracker.verbose:
        print(f"Program was brute forcing for {time.time() - cracker.start} seconds")
