class Solution:
    def isValid(self, s: str) -> bool:
        while '()' in s or '[]' in s or '{}'in s:
            print('loop inside :', s)
            s = s.replace('()','')
            s = s.replace('[]','')
            s = s.replace('{}','')
            
        return s==''
        