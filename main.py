
'''
Game: Isoland 2：Ashes of Time.
Where: Factory's door.
Method: Use DFS to find the longest line.
'''

def MapReader(file):
    f = open(file)
    ls = f.readlines()
    return ls


def GetStart(mp, sb):
    r = 0
    for l in mp:
        c = 0
        for i in l:
            if i == sb:
                return r, c
            c += 1
        r += 1
    return -1, -1


def MapPrinter(mp):
    for i in mp:
        i = i.replace(" ", "\uf04d", -1)
        i = i.replace("#", "\uf041", -1)
        i = i.replace("*", "\uf111", -1)
        print(i, end='')
    print('')


def CanMove(c, n, mp, sb):
    q, w = c
    a, s = n
    if q < 0 or a < 0 or w < 0 or s < 0:
        return False
    l = len(mp)
    if q >= l or a >= l:
        return False
    if w >= len(mp[q]) or s >= len(mp[a]):
        return False
    if mp[a][s] != sb:
        return False
    if abs(q-a)+abs(w-s) <= 1:
        return True
    return False


def copyMp(mp):
    n = []
    for k in mp:
        n.append(k)
    return n


def visit(mp, c, sb):
    mp = copyMp(mp)
    x, y = c
    mp[x] = mp[x][:y]+sb+mp[x][y+1:]
    return mp


def Runner(mp, c, p=[], r=[], mpr=[]):
    d = [-1, 0, 1, 0, -1]
    s = "\uf062\uf061\uf063\uf060"
    s2 = "\uf35b\uf35a\uf358\uf359"
    fg = True
    for i in range(4):
        n = c[0]+d[i], c[1]+d[i+1]
        if CanMove(c, n, mp, '#'):
            fg = False
            pp = p.copy()
            pp.append(s[i])
            sb = s
            if mp[c[0]][c[1]] == '*':
                sb = s2
            Runner(visit(mp, c, sb[i]), n, pp, r, mpr)
    if fg:
        if len(p) > len(r):
            r.clear()
            for i in p:
                r.append(i)
            mpr.clear()
            for i in mp:
                mpr.append(i)


def main():
    mp = MapReader("input")
    sp = GetStart(mp, '*')
    r, mpr = [], []
    Runner(mp, sp, [], r, mpr)
    MapPrinter(mp)
    print("------------")
    MapPrinter(mpr)


if __name__ == "__main__":
    main()
