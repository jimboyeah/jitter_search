from sunday_search import Sunday
from brute_search import Violent
from kmp_search import KnuthMorrisPratt as KPM
from jitter_search import JitterSearch

tests = [
    dict(c=5,  p="llam",    s="shellllama"),
    dict(c=1,  p="loon",    s="aloong"),
    dict(c=-1, p="loog",    s="loon"),
    dict(c=0,  p="loon",    s="loon"),
    dict(c=-1, p="loon",    s="loo"),
    dict(c=8,  p="ma",      s="shellllama"),
    dict(c=-1, p="bib",     s="bilibili"),
    dict(c=1,  p="ili",     s="bilibili"),
    dict(c=-1, p="bibi",    s="ilibili"),
    dict(c=8,  p="AAAABAAA",s="AAAABAABAAAABAAABAAAA"),
    dict(c=0,  p="AAAA",    s="AAAABAABAAAABAAABAAAA"),
    dict(c=35, p="Type",    s="git clone git@github.com:Microsoft/TypeScript-Sublime-Plugin"),
    dict(c=-1, p="Complexy",s="Denial of Service via Algorithmic Complexity Attack"),
    dict(c=31, p="Hash",    s="New Second-Preimage Attacks on Hash Functions"),
    dict(c=31, p="4th",     s="Robert Sedgewick - Algorithms, 4th Edition"),
    dict(c=18, p="Closed",  s="Open Hash Tables (Closed Addressing)"),
    dict(c=20, p="Open",    s="Closed Hash Tables (Open Addressing)"),
    dict(c=20, p="using",   s="Closed Hash Tables, using buckets"),
    dict(c=27, p="3rd",     s="Introduction to Algorithms 3rd Edition"),
    dict(c=5,  p="Fuzz",    s=u"模糊测试（Fuzz Testing）是一种自动化的软件测试技术"),
    dict(c=11, p="？",      s=u"软件测试中如何测试算法？"),
]

def search_assert(s, p, c, d):
    ret = d(s, p)
    if isinstance(ret, list) and len(ret)>0: ret = ret[0]
    if c == ret:
        if c == -1:
            print(f"✅pass: [{ret:>3}] ==> [{p}] is not in [{s}]")
        else:
            print(f"✅pass: [{ret:>3}] ==> [{p}] is in [{s}]")
    else:
        print(f"⛔fail: [{ret:>3}] expect [{c}] ==> [{p}] is in [{s}]")

def test():
    print("Sunday search test:")
    alg = Sunday()
    for case in tests:
        search_assert(**case, d=alg.search)

    print("Violent search test:")
    alg = Violent()
    for case in tests:
        search_assert(**case, d=alg.search)

    print("KPM search test:")
    alg = KPM()
    for case in tests:
        search_assert(**case, d=alg.search)

    print("Jitter search test:")
    alg = JitterSearch()
    for case in tests:
        search_assert(**case, d=alg.search)

if __name__ == '__main__':
    test()
