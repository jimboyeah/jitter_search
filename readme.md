
# ⚡🏡🗝

我曾经以不正确的姿势学习研究了 KMP，但是被众说纷纭文章搞头脑迷糊了。看着别人撤了一堆的名词术语，又是动态规划，又是状态图，又是状态转换什么的，别人就是懂得多。感觉真是后悔学了中文，因为每个字我都懂，但就是不清楚别人在说什么😂

我觉得 KMP 搜索算法应该有更好的学习姿势，不需要扯概念扯术语，只需要直觉，Algorithm Visualizer 也许是一个可以在直觉上增加理解的好工具。

代码仓库可以通过以下链接或克隆获取：

    git clone git@github.com:jimboyeah/jitter_search.git
    git clone https://github.com/jimboyeah/jitter_search.git

以上是学习库 Algorithms.md 分类文档中关于字符串搜索算法的部分，因为有离线整理资料的习惯，只会挑选部分公开发布。使用的工具是 Sublime Text + Git，感谢作者的共享软件，真的非常高效。


# 🚩 Violent Search 暴力搜索算法

暴力搜索算法，Brute Force Searching，是两层简单的循环结构。先从 S 第 1 个字符位置开始逐字与 P 字符比较，发现不匹配时，再从 S 第 2 个字符位置开始逐字比较，依次处理直到整个 S 字符串处理完成，算法复杂度是 O(mn)。

```py
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
```

输出测试结果：

    Pattern: Type
     Search: git clone git@github.com:Microsoft/TypeScript-Sublime-Plugin
         at:                                    ^^^^ col:35
    
    Pattern: Hash
     Search: New Second-Preimage Attacks on Hash Functions
         at:                                ^^^^ col:31
    
    Pattern: 4th
     Search: Robert Sedgewick - Algorithms, 4th Edition
         at:                                ^^^ col:31
    
    Pattern: Closed
     Search: Open Hash Tables (Closed Addressing)
         at:                   ^^^^^^ col:18
    
    Pattern: Open
     Search: Closed Hash Tables (Open Addressing)
         at:                     ^^^^ col:20
    
    Pattern: using
     Search: Closed Hash Tables, using buckets
         at:                     ^^^^^ col:20
    
    Pattern: 3rd
     Search: Introduction to Algorithms 3rd Edition
         at:                            ^^^ col:27


# 🚩 KMP Search
- Algorithms 4th - 5.3 Substring Search
- 有限状态机之 KMP 字符匹配算法 https://labuladong.gitee.io/algo/3/27/99/
- KMP - Algorithm Visualizer https://algorithm-visualizer.org/dynamic-programming/knuth-morris-pratts-string-search
- 1143. 最长公共子序列 https://leetcode-cn.com/problems/longest-common-subsequence/
- 14. 最长公共前缀 https://leetcode-cn.com/problems/longest-common-prefix/

KMP 字符串查找算法，用于在一个文本串 S 内查找一个模式串 P 的出现位置，这个算法由 Donald Knuth、James H. Morris、Vaughan Pratt 三人于 1977 年联合发表，故取这 3 人的姓氏命名此算法。

Knuth D.E., Morris J.H., and Pratt V.R., Fast pattern matching in strings, SIAM Journal on Computing, 6(2), 323-350, 1977.


暴力搜索算法中，是两层简单的循环结构。先从 S 第 1 个字符位置开始逐字与 P 字符比较，发现不匹配时，再从 S 第 2 个字符位置开始逐字比较，依次处理直到整个 S 字符串处理完成，算法复杂度是 O(mn)。

如果字符串中重复的字符比较多，或者 P 中有更合适的匹配位置却没有相应处理，该算法就显得很蠢，比如如下数据：

    s = "shellllama" p = "llam"

KMP 算法的不同之处在于，它会花费空间来记录一些信息，这是一处反馈机制，是动态规划算法的特性，在上述情况中就会显得很聪明。

相比暴力的逐字搜索，KMP 算法不用对 S 字符的每一个位置的字符串进行一轮比较，永不回退处理 S 输入字符串。另一个角度来说，KMP 算法回退的是 PMT 查询表的数据。

如果文本串的长度为 n，模式串的长度为 m，那么匹配过程的时间复杂度为 O(n)，整体时间复杂度为 O(m + n)。

而 KMP 算法通过引入一个前缀和后缀的公共字串长度表，也称为部分匹配表 PMT - Partial Match Table，这个表的构建就是 KMP 算法的核心思想：监测到不匹配时，P 提供足够的信息来确定下一次应该从什么位置开始搜索。跳过一些不必要比较的字符串，从而提高了搜索效率，所以把构建出来的这个表称作 next_table 或者 dp_table 都是合适的。

首先了解一些概念：

前缀：以第一个字符开始，但是不包含最后的字符，列如 "abc" 的前缀有 "a" 和 "ab"。
后缀：以最后的字符开始，但是不包含第一个字符，列如 "abc" 的后缀有 "c" 和 "bc"。
最长公共子串：Longest Common Substring 是指两个字符串中最长连续相同的子串长度。 例如 “1AB2345CD” 和 “12345EF” 的最长公共子串为 “2345”，这也是一道算法题目。
子序列：由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。

以 Algorithm Visualizer 演示的数据为例：

    S = "AAAABAABAAAABAAABAAAA";
    P = "AAAABAAA";

    S = "Monkey like banana.";
    P = "anana";

首先，KMP 需要根据 P 生成一个 PMT 数据表，以供匹配失败时确定下一个位置，PMT 生成规则，以前缀公共字串长度为例，PMT 每个值是 P 对应位置的匹配前缀字符数量，前缀长度，所以开始位置总是 0：

    PMT: 0 1 2 3 0 1 2 3      | Group
      P: A A A A B A A A      |   A

    PMT: 0 1 0 0              | Group
      P: l l a m              |   B

    PMT: 0 0 1 2              | Group
      P: n a n a              |   C

以上 A、B、C 三组数据产生的 PMT 如何使用呢？还是拿 P 去匹配 S 字符串，从头开始，以 B 组数据为例：

    S: s h e l l l l a m a
       1 2 3 4 5 6 7 8 9 0

从 S 开头检索，直到位置 4 出现第一个匹配字符，继续位置 5 出现第二个匹配字符。注意，每出现匹配表示 PMT 数据获取的位置状态也在变化。

检索第 6 个字符时，出现不匹配，这时 PMT 的数据就起作用了。如果是 Violent Search 算法，肯定是推倒重来，从 S 的第 2 个字符开始检索。但是 KMP 算法因为提前准备好了 PMT 数据，第一次出现不匹配时，知道可以从 PMT 表查询到前面可以匹配的前缀长度，即上一个位置有一个目标前缀长度为 1 的匹配子串。

从而可以直接修改 PMT 状态，或者叫做回退 PMT 数据指针位置，从而避免了在 S 字符串中进行回退操作。通常，输入数据中 S 会比 P 大得多，之也就是 KMP 的算法优点所在：高频前缀字符串的优化搜索算法。

```py
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
```

# 🚩 Jitter Search

KMP 主要思想是当出现字符串不匹配时，可以通过 PMT 获释已经匹配的前后缀长度，并利用这些长度信息避免从头再去做匹配，考虑 PMT 查询表的构建，KMP 本质上还是线性搜索算法。

实际上，KMP 算法并不比 C 库函数 strstr() 快多少，因为在缺少重复前缀后缀的情况下，KMP 算法并不占优势。

糟糕的情况是 P 长度 S 相近时，这种算法反而表现更差，花大力气生成的 PMT 数据几乎没什么作用。

考虑到 KMP 算法的不足，这里设计了一种带有二分法思维的搜索算法 Jitter Search：

- 第一步，在 S 串中找出所有 P 第一个字符出现的位置，设为 J 集合；
- 第二步，选择一个整数 jitter，比如 P 串长度的一半；
- 第三步，将 J 集合中所有位置偏移 jitter 处且与 P 串相应位置的值相同的过滤出来；
- 重复，这种操作，直到完整匹配结果。

这种算法的优点是结合了二分法及低频过滤器思维，可以高效处理非频繁重复的字符串搜索。空间上需要占用一个 max(S, p) 的数组空间来存储索引值。

以下为 Python 实现代码，在应用中，可以对首字符高频重复的情况做优化：

```py
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
```

输出结构：

      P: llam
      S: shellllama
     at:      ^^^^ pos: [5]
    
      P: ma
      S: shellllama
     at:         ^^ pos: [8]
    
      P: ili
      S: bilibili
     at:  ^^^ pos: [1]
    
      P: ili
      S: bilibili
     at:      ^^^ pos: [1, 5]
     ...


# 🚩 Sunday Search
- 28. [Easy] implement strStr() https://leetcode-cn.com/problems/implement-strstr/
- 187. [Medium] Repeated DNA Sequences https://leetcode.com/problems/repeated-dna-sequences/

1977 年，同时期德克萨斯大学 Robert S. Boyer 教授和 J Strother Moore 教授发明了一种新的字符串匹配算法，简称 BM 算法。该算法从模式串的尾部开始匹配，且最坏情况下的时间复杂度为 O(N)。在实践中，比 KMP 从模式串的开头开始匹配的算法效能高，但是这两种算法都需要对 P 进行预处理，算法实现复杂，大大降低的实用性。

A fast string searching algorithm R. Boyer, J. S. Moore Published 1977 Computer Science Commun.

Daniel M. Sunday, A very fast substring search algorithm, Communications of the ACM, v.33 n.8, p.132-142, Aug. 1990

Horspool R.N., 1980, Practical fast searching in strings, Software - Practice & Experience, 10(6):501-506


但 BM 算法也还不是现有字符串查找算法中最快的算法，更快的查找算法是 Sunday 算法，由 Daniel M.Sunday 在 1990 年提出，它的思想跟 BM 算法很相似，只不过 Sunday 算法是从前往后匹配，逻辑如下：

- 从头开始匹配，失败时关注的是 S 文本串中按 P 匹配长度的下一位置的字符，记为 M；
- 如果该字符不在模式串 P 中，这表示 M 位置之前不可能匹配，则下一轮匹配开始位置在偏移 len(P) 距离后；
- 如果该字符出现在模式 P **最右侧位置** Q 中，则将 Q 位置与 M 位置对齐后，再开始新一轮匹配搜索。

从右侧检索 P 中的字符位置这一点很关键，这可以保证对齐 S 序列中的 M 位置时不会错失可能匹配的子串。

例如，以下一组数据：

    S = "aloong"
    P = "loon"

第一轮搜索 l:a 就不匹配，所以直接找到 len(P) 位置的 “n”，确认它在 P 串最右侧的位置，字符索引位置按 0 为起始值：

    S = a l o o n g        >>>   S = a l o o n g
        ^       ^M = 4     >>>         ^     ^M = 4
    P = l o o n            >>>   P =   l o o n 
        ^     ^Q = 3       >>>         ^     ^Q = 3

然后，再按对齐后的序列进入第二轮搜索，如果 M 位置的字符没有出现在 P 序列中，这种情况就是最好处理的，也是最有效率的，直接就只可以跳过一长段不可能匹配的子序列，大大提高的检索效率。同时，与 KMP 等算法相比，还可以不事先建立索引表。

```py
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
```

输出结果：

      P: llam
      S: shellllama
     at:      ^^^^ end pos: 8

      P: loon
      S: aloong
     at:  ^^^^ end pos: 4

      P: loon
      S: loon
     at: ^^^^ end pos: 3

      P: ma
      S: shellllama
     at:         ^^ end pos: 9

      P: ili
      S: bilibili
     at:  ^^^ end pos: 3

      P: AAAABAAA
      S: AAAABAABAAAABAAABAAAA
     at:         ^^^^^^^^ end pos: 15

      P: AAAA
      S: AAAABAABAAAABAAABAAAA
     at: ^^^^ end pos: 3

Sunday 算法就像在移动一个匹配窗口，连续匹配时窗口就放大，匹配失败就根据 M 指示的字符来调整新窗口位置。实际上是对 BM 算法的优化，并且它更简单易实现。

Sunday 算法可以先对 P 建立查询表，再对 S 进行搜索。那表时的扫描顺序没有限制，为了提高最坏情况下的算法效率，可以对 P 字符按照其出现的概率从小到大的顺序扫描，这样能尽早地确定失配与否。

Horspool 算法的思想有个创新之处就是模式串是从右向左进行比较的，在不匹配情况处理手法和 Sunday 有类似特征。


# 🚩 Tests for String Search

最后，是以上几种字符串搜索算法的测试用例：

```py
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
```
