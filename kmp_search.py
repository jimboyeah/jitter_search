class KnuthMorrisPratt:

    def gen_next(self, p):

        k = 0 # prefix pointer
        l = 1 # postfix pointer
        _next = [0] * len(p)
        for l in range(l, len(p)):
            while k>0 and p[k] != p[l]:
                k = _next[k-1]
            if p[l] == p[k]: k += 1
            _next[l] = k
        return _next

    def search(self, s, p):

        _next = self.gen_next(p)

        j = 0 # pattern pointer
        i = 0 # string pointer
        for i in range(i, len(s)):
            while j>0 and p[j] != s[i]:
                j = _next[j-1]
            if p[j] == s[i]:
                j += 1
            if j == len(p):
                ismain and print(f"""\
                    PMT: {_next}
                      P: {p}
                      S: {s}
                     at: {"^"*len(p):>{i+1}}|<== end pos: {i}
                    """)
                return i - j + 1
        return -1
        
ismain = __name__ == '__main__'
if ismain:
    v = KnuthMorrisPratt()
    v.search(p="llam",    s="shellllama")
    v.search(p="bib",     s="bilibili")
    v.search(p="bibi",    s="ilibili")
    v.search(p="AAAABAAA",s="AAAABAABAAAABAAABAAAA")
    v.search(p="loog",    s="loon")
    v.search(p="loon",    s="loon")
    v.search(p="loon",    s="loo")
