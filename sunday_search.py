
class Sunday:

    def lastOf(self, p, c):
        l = len(p)
        while l>-1:
            l -= 1
            if p[l] == c:
                break
        return l

    def search(self, s, p):

        i = 0 # string pointer
        j = 0 # pattern pointer
        while i < len(s):
            if s[i] != p[j]:
                # print(f"i,j = {i},{j} p:{len(p)} s:{len(s)}")
                if i+j+1 >= len(s): break
                if (n := i+len(p)-j) >= len(s): break
                k = self.lastOf(p, s[n])
                # print(f"k = {k} n = {n} {s[n]}:p{p}")
                if k==-1:
                    i += len(p) - j + 1
                else:
                    i += len(p) - j - k
                j = 0
            elif j+1 == len(p):
                ismain and print(f"""\
                      P: {p}
                      S: {s}
                     at: {"^"*len(p):>{i+1}} end pos: {i}
                    """)
                return i-len(p) + 1
            else:
                i += 1
                j += 1
        ismain and print(f"S: {s} doesn't has P: {p}")
        return -1

ismain = __name__ == '__main__'

if __name__ == '__main__':
    v = Sunday()
    v.search(p="llam",    s="shellllama")
    v.search(p="loon",    s="aloong")
    v.search(p="loog",    s="loon")
    v.search(p="loon",    s="loon")
    v.search(p="loon",    s="loo")
    v.search(p="ma",      s="shellllama")
    v.search(p="bib",     s="bilibili")
    v.search(p="ili",     s="bilibili")
    v.search(p="bibi",    s="ilibili")
    v.search(p="AAAABAAA",s="AAAABAABAAAABAAABAAAA")
    v.search(p="AAAA",    s="AAAABAABAAAABAAABAAAA")
