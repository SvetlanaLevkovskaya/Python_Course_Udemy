def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    print(is_prime)
    # if is_prime:
    #     print("it is a prime number")
    # else:
    #     print("it is not a prime number")
    # print(is_prime)


n = int(input("Check this number: "))
prime_checker(number=n)


# a = int(input('enter a number: '))
#
# k = 0
# divider = []
# for i in range(1, a+1):
#     if a % i == 0:
#         k += 1
#         divider.append(i)
# print(divider)
#
# if k == 2:
#     print("prime number")
# else:
#     print("it is not a prime number")
