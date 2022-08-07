#Чеканов Вячеслав Александрович
#Домашнее задание №4
#Easy
km = int(input('введите колчество километров: '))
def convert(km):
    miles = km / 1.609
    print(miles)
convert(km)

#2
def my_round(number, ndigits):
    celoe, drobnoe = number.split('.')
    my_drobnoe = drobnoe[0:ndigits]
    last_number = drobnoe[ndigits:ndigits+1]
    if last_number and int(last_number) > 4:
        my_drobnoe = my_drobnoe +1
    answer = celoe + '.' + str(my_drobnoe)
    return answer
number = input('number: ')
ndigits = int(input('ndigits: '))
answer = my_round(number, ndigits)
print(answer)