import os
from pathlib import Path

def read(name):
    dic = {}
    s = ""
    with open(name,'r') as name:
        for line in name:
            for word in line.split():
                s+=word
                s+=" "
    name.close()
    return s
    