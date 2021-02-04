
from collections import defaultdict
def longestArithSeqLength(A) :
    ans = 0
    cnt = defaultdict(lambda: 1)
    seen = set()
    for x in A:
        for xx in seen:
            cnt[x, x - xx] = 1 + cnt[xx, x - xx]
            ans = max(ans, cnt[x, x - xx])
        seen.add(x)
    return ans

longestArithSeqLength([3,6,9,10])