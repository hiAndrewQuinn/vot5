# vot5.py

from functools import reduce

vot5_table = { 'a':'e', 'e':'i', 'i':'o', 'u':'a' , 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}  

def vot5(s):
  """Shift every vowel and leave everything else unchanged. Case-preserving."""
  return reduce(lambda x, y: x + y, map(lambda l: vot5_table[l] if l in vot5_table else l, s))

if __name__ == "__main__":
  print(vot5("An example of vot5 in action."))
