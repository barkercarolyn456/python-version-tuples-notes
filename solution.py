import re

def solve(value):
    return (lambda a,b: (a>b)-(a<b))(*[tuple(int(x) for x in s.split(".")) + (0,)*(max(len(v.split(".")) for v in value)-len(s.split("."))) for s in value]) if len(value)==2 and all(re.fullmatch(r"\d+(\.\d+)*", s) for s in value) else (_ for _ in ()).throw(ValueError("two numeric versions required"))
