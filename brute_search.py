class Violent:

    def search(self, s, p):
        for i in range(0, len(s)-len(p)+1):
            for j in range(0, len(p)):
                if s[i+j] != p[j]:
                    break
                elif j+1 == len(p):
                    ismain and print(f"""\
                    Pattern: {p}
                     Search: {s}
                         at: {"^"*len(p):>{i+len(p)}} col:{i}
                    """)
                    return i
        return -1

ismain = __name__ == '__main__'

if ismain:

    v = Violent()
    v.search(p="Type",    s="git clone git@github.com:Microsoft/TypeScript-Sublime-Plugin")
    v.search(p="Complexy",s="Denial of Service via Algorithmic Complexity Attack")
    v.search(p="Hash",    s="New Second-Preimage Attacks on Hash Functions")
    v.search(p="4th",     s="Robert Sedgewick - Algorithms, 4th Edition")
    v.search(p="Closed",  s="Open Hash Tables (Closed Addressing)")
    v.search(p="Open",    s="Closed Hash Tables (Open Addressing)")
    v.search(p="using",   s="Closed Hash Tables, using buckets")
    v.search(p="3rd",     s="Introduction to Algorithms 3rd Edition")
    v.search(p="loog",    s="loon")
    v.search(p="loon",    s="loon")
    v.search(p="loon",    s="loo")
