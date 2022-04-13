# with statement in file handling

with open("s.txt") as f:
  d = f.read()
  print(d)
  print(f.closed)#checks weather file is clised or not
print(f.closed)#outside of with method