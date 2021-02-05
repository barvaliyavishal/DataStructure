import playsound

playsound.playsound()
nums = [1, 3, 5, 9]

sq = lambda x: x*x
cu = lambda x: x*x*x
func = [sq,cu]
val = []
for i in nums:
    val.append( list(map(lambda x : x(i), func)))
print(val)