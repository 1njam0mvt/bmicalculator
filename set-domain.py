#!/usr/bin/env python3
"""Replace the placeholder domain in every file.
Usage:  python3 set-domain.py https://yourdomain.com
        python3 set-domain.py yourdomain.com
"""
import sys,os
if len(sys.argv)!=2:
    sys.exit(__doc__)
new=sys.argv[1].strip().rstrip("/")
if not new.startswith("http"): new="https://"+new
old="https://example.com"
n=0
for root,_,files in os.walk(os.path.dirname(os.path.abspath(__file__))):
    for f in files:
        if f.endswith((".html",".xml",".txt",".webmanifest",".md")):
            p=os.path.join(root,f);s=open(p,encoding="utf-8").read()
            if old in s:
                open(p,"w",encoding="utf-8").write(s.replace(old,new));n+=1
print(f"Done: {new} written into {n} files.")
