# Greedy algorithm ?
# WTF!

import math
import random
import common as co


def can(mp, c, sb):
    x, y = c
    if x < 0 or x > len(mp):
        return False
    if y < 0 or y > len(mp[x]):
        return False
    if mp[x][y] != sb:
        return False
    return True


def GetMinWayPos(mp, c):
    ct = math.inf
    out = []
    for i in range(4):
        n = co.Next(c, i)
        if can(mp, n, '#'):
            tmp = 0
            for j in range(4):
                nn = co.Next(n, j)
                if can(co.Visit(mp, n, '*'), nn, '#'):
                    tmp += 1
            if ct > tmp:
                ct = tmp
                out.clear()
                out.append(i)
            elif ct == tmp:
                out.append(i)
    return out


def Runner(mp, c, p=[], r=[], mpr=[]):
    s = "\uf062\uf061\uf063\uf060"
    s2 = "\uf35b\uf35a\uf358\uf359"
    m = GetMinWayPos(mp, c)
    for i in m:
        n = co.Next(c, i)
        pp = p.copy()
        pp.append(i)
        sb = s
        if mp[c[0]][c[1]] == '*':
            sb = s2
        Runner(co.Visit(mp, c, sb[i]), n, pp, r, mpr)

    if len(p) > len(r):
        r.clear()
        for i in p:
            r.append(i)
        mpr.clear()
        for i in mp:
            mpr.append(i)


def main():
    mp = co.MapReader("input")
    sp = co.GetStart(mp, '*')
    r, mpr = [], []
    Runner(mp, sp, [], r, mpr)
    co.MapPrinter(mp)
    print("------------")
    co.MapPrinter(mpr)


if __name__ == "__main__":
    main()
