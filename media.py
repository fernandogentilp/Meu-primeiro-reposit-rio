n1 = int(input())
n2 = int(input())
n3 = int(input())
m = (n1 + n2 + n3) / 3
print(m)
if m <= 4:
    print('Prova final')
elif m >= 7:
    print('Passou')
else:
    print('Reprovou')
