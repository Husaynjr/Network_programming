def is_prime(num):
    for i in range (2,num):
        if num%i ==0 :
            return False
    return True

primary_list = [x for x in range (1,1001) if is_prime(x)]
print (primary_list)