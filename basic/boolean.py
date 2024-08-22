print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 1

myobj = myclass()
print(bool(myobj))

x = 200
print(isinstance(x, int))

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")