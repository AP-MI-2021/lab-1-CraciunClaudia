def is_palindrome(n):
    '''
    Determina daca un numar este palindrom.
    -Input: n
     -Output : "Numarul este palindrom" sau "Numarul nu este palindrom"
    '''
    inv = 0
    x = n
    ogl=0
    while n!= 0:
        ogl=ogl * 10 + n % 10
        n = n / 10
    if x == ogl :
        print(f'Numarul este palindrom')
    elif x !=ogl :
        print(f'Numarul nu este palindrom')


