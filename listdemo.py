Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[100,23,12,41,52,1,3,970]
a.append(0)
a.insert(23,56)
a.extend([235,745,98])
a[5]=180
a
[100, 23, 12, 41, 52, 180, 3, 970, 0, 56, 235, 745, 98]
a.pop()
98
a.remove(3)
a.sort()
a
[0, 12, 23, 41, 52, 56, 100, 180, 235, 745, 970]
a.reverse()
a
[970, 745, 235, 180, 100, 56, 52, 41, 23, 12, 0]
u=[('parag',23),('sue',34),('miha',56)]
u
[('parag', 23), ('sue', 34), ('miha', 56)]
for i in u:
    print(i[0],' age is ', i[1])

    
parag  age is  23
sue  age is  34
miha  age is  56
