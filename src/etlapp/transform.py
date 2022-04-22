
import typer 
import os 

def transform1(out):
    ans = out.upper()
    return ans

def transform2(out):
    dic = {}
    out = out.split()
    for i in out:
        if i in dic:
            dic[i]+=1
        else:
            dic.update({i:1})
    return dic