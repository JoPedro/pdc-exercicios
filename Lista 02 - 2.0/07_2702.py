f, b, m = map(int, input().split())
fR, bR, mR = map(int, input().split())

nRf = (fR - f)
nRb = (bR - b)
nRm = (mR - m)

nRt = 0

if (nRf > 0):
    nRt = nRf
if (nRb > 0):
    nRt += nRb
if (nRm > 0):
    nRt += nRm

print(nRt)
