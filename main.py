
'''
Game: Isoland 2：Ashes of Time.
Where: Factory's door.
Method: Use DFS to find the longest line.

This code is too slow, gona find more fast algorithms.
'''

import common as co


def Runner(mp, c, p=[], r=[], mpr=[]):
    d = [-1, 0, 1, 0, -1]
    s = "\uf062\uf061\uf063\uf060"
    s2 = "\uf35b\uf35a\uf358\uf359"
    fg = True
    for i in range(4):
        n = c[0]+d[i], c[1]+d[i+1]
        if co.CanMove(c, n, mp, '#'):
            fg = False
            pp = p.copy()
            pp.append(s[i])
            sb = s
            if mp[c[0]][c[1]] == '*':
                sb = s2
            Runner(co.Visit(mp, c, sb[i]), n, pp, r, mpr)
    if fg:
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
