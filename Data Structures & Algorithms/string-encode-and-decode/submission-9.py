class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        if not strs:
            return s
        sizes = []
        for word in strs:
            sizes.append(len(word))
        for sz in sizes:
            s += str(sz)
            s += ','
        s +='#'
        for word in strs:
            s += word
        print(s)
        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        if not s:
            return strs
        i = 0
        sizes= []
        while s[i] !='#':
            current = ''
            while s[i] != ',':
                current += s[i]
                i += 1
            sizes.append(int(current))
            i+=1
        i += 1

        for sz in sizes:
            strs.append(s[i: i+sz])
            i += sz
        return strs

