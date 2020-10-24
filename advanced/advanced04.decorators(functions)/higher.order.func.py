def leibniz_term(n):
    return (-1)**n * 1/(2*(n+1)-1)


def sum_func_terms(leibniz_term, n):
    sum=0
    for i in range(n):
        sum+=leibniz_term(i)

    return 4*sum


for i in range(10,200,10):
    print(sum_func_terms(leibniz_term, i))

print(sum_func_terms(leibniz_term,100000))