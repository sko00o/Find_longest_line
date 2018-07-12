# Simulated Annealing
# WTF!

import common as co
import math
import random as rd


def initPath(mp, c):
    p = []
    getPath(mp, c, p)
    return p


def getPath(mp, c, p):
    end = True
    nb = []
    for i in range(4):
        n = co.Next(c, i)
        if co.CanMove(c, n, mp, '#'):
            end = False
            nb.append(n)
    if end:
        return
    else:
        rn = int(rd.random()*len(nb))
        n = nb[rn]
        p.append(n)
        getPath(co.Visit(mp, c, '*'), n, p)


def calRes(p):
    return -len(p)


def getNewPath(mp, p, ra):
    sz = int(len(p)*ra)
    if sz == 0:
        sz = 1
    if sz > len(p):
        sz = len(p)
    np = []
    for i in range(sz):
        np.append(p[i])
        mp = co.Visit(mp, p[i], '*')
    getPath(mp, np[-1], np)
    return np


def getResult(mp, c):
    tmp = 100.0
    endTmp = 1e-8
    des = 0.98
    ct = 0
    total = math.log(endTmp/tmp)/math.log(des)
    it = len(mp)*len(mp[0])
    lp = []
    tp = []

    for i in range(it):
        nmp = co.copyMp(mp)
        p = initPath(nmp, c)
        tp.append(p)

    while tmp > endTmp:
        for i in range(it):
            p = tp[i]
            r = calRes(p)
            nmp = co.copyMp(mp)
            np = getNewPath(nmp, p, ct/total)
            nr = calRes(np)

            if nr < r:
                p = np
            else:
                cp = 1/(1+math.exp(-(nr-r)/tmp))
                if rd.random() < cp:
                    p = np
        ct += 1
        tmp *= des

    for i in range(len(tp)):
        if len(tp[i]) > len(lp):
            lp = tp[i]
    return lp


def getDir(c, n):
    for i in range(4):
        tn = co.Next(c, i)
        if tn == n:
            return i
    return -1


def getSB(i, sSB, SB):
    s = "\uf062\uf061\uf063\uf060"
    s2 = "\uf35b\uf35a\uf358\uf359"
    wrong = "\uf00d"
    ss = s
    if sSB == SB:
        ss = s2
    if i < 0 or i > 3:
        return wrong
    return ss[i]


def TransMp(mp, r):
    fg = True
    ti = None
    for i in r:
        if fg:
            fg = False
            ti = i
            continue
        d = getDir(ti, i)
        s = mp[ti[0]][ti[1]]
        # print ("%s->%s: %d : %s"%(ti,i,d,s))
        sr = mp[ti[0]]
        mp[ti[0]] = sr[:ti[1]]+getSB(d, s, '*')+sr[ti[1]+1:]
        ti = i
    return mp


def main():
    mp = co.MapReader("input")
    sp = co.GetStart(mp, '*')
    r = getResult(mp, sp)
    # print(r)
    co.MapPrinter(mp)
    print("------------")
    mpr = TransMp(mp, r)
    co.MapPrinter(mpr)


if __name__ == "__main__":
    main()
