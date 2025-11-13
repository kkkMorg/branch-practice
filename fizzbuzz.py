# fizzbuzz
# 1 ~ n 까지의 자연수에 대해, 3의 배수라면 fizz, 5 buzz, 15 fizzbuzz, 나머지는 숫자 

for i in range(1, 15 + 1):

    if i % 3 == 0 :
        print('fizz')
    else:
        print(i)
