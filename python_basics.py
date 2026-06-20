age = 1
name = 'Bob'

print(name + ' is ' +str(age) + ' years old')

a = 10
b = 5
add = a + b
sub = a - b
div = a / b
mult = a * b
pow = a ** b
print(add, sub, div, mult, pow)

age = 28

isHappy = True

if age > 21:
    print('You are old!')
elif age == 18:
    print('You are getting old!')
else:
    print('You are young!')


if isHappy:
    print('You are happy!')
else:
    print('You are not happy!')


for i in range(3):
    print('Hello ', i)

colors = {1, 2, 3, 4, 5}

# for n in colors:
#     print(n)

n1 = 1
n2 = 1
# max = int(input("Enter max: "))
max = 1
while n1 < max:
    print(n1)
    n1 += n2
    n2 = n1-n2


str = 'hello'
def reverse(str, i):
    if(i <= 1):
        return str[0]
    return str[i-1]+reverse(str, i-1)

print(reverse(str, len(str)))

def something():
    pass


number = '1'

try:
    print(number+2)
except:
    print('not a valid number')


