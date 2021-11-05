def my_exmpl1(N=int(input("enter a number"))):
    total_odd = 0
    total_even = 0
    even_counter = 0
    even_average = 0
    for i in range(1, N + 1):
        if i % 2 == 0:  #even
            total_even += i
            even_counter += 1
        else:
            total_odd += i  #odd
    even_average = total_even / even_counter
    print("even average: ", even_average)
    print("sum of odds: ", total_odd)

my_exmpl1()