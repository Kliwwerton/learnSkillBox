number = '7586'
number2 = '6987'

# for i in str(number):
#     count = str(number).count(i)
#     print(count)

for i in number:
    print(number.index(i))
    if i in number2:
        print('Да')
        if number.index(i) == number2.index(i):
            print('ДА ДА')

