import os
from pathlib import Path
import json

def writes(name,inn):
    ans = inn
    # print("ans",ans)
    with open(name,'w') as file:
        file.write(ans)
