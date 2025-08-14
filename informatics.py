# Baubles
ro,bo,s,rp,bp=map(int,input().split())
if ro<bo or rp<bp:
    print(0)
else:
    print(min(ro-rp,bo-bp)+1)