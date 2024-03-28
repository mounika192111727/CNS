class Solution:
   def solve(self, text, key):
      cip = []
      start = ord('a')
      for l, k in zip(text, key):
         shift = ord(k) - start
         pos = start + (ord(l) - start + shift) % 26
         cip.append(chr(pos))
      return ''.join([l for l in cip])
ob = Solution()
text = "code"
key = "team"
print(ob.solve(text, key))
