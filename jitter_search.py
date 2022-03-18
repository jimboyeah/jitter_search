##
## jitter search by Jeango
## 2020/3/18 20:42
##
class JitterSearch:

    def search(self, s, p):

        if len(s)<len(p): return [-1]

        j = []
        i = 0 # string pointer
        for i in range(i, len(s)-len(p)+1):
            if p[0] == s[i]:
                j.append(i)

        jt = len(p) - 1
        while jt>0:
            for i in range(0, len(j)):
                if j[i] < 0: continue
                if s[j[i]+jt] != p[jt]:
                    j[i] = -1
            jt -=1

        ret = []
        for i in j:
            if i<0: continue
            ret.append(i)
            ismain and print(f"""\
                  P: {p}
                  S: {s}
                 at: {"^"*len(p):>{i+len(p)}} pos: {ret}
                """)
        if len(ret)==0: ret = [-1]
        return ret
        
ismain = __name__ == '__main__'

if ismain:
    v = JitterSearch()
    v.search(p="llam",    s="shellllama")
    v.search(p="ma",      s="shellllama")
    v.search(p="bib",     s="bilibili")
    v.search(p="ili",     s="bilibili")
    v.search(p="bibi",    s="ilibili")
    v.search(p="AAAABAAA",s="AAAABAABAAAABAAABAAAA")
    v.search(p="AAAA",    s="AAAABAABAAAABAAABAAAA")
    v.search(p="loog",    s="loon")
    v.search(p="loon",    s="loon")
    v.search(p="loon",    s="loo")
