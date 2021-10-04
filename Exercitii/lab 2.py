  def is_palindrome( n ):
  '''
  Determina daca un numar este palindrom
  Input:
  -n : intreg,numarul care trebuie verificat
  Output:
  -True daca este palindrom
  -False daca nu este palindrom
  '''
    n = nr1
    inv = []
    while n:
     inv = inv * 10 + n % 10
     n = n/10

    if inv == n:
      return True
    if inv != n :
        return False

  def main():
  while True:
  print('1. Numar palindrom.')
  optiune = input('Alegeti o optiune: ')
  if option == '1':
    nr1 = int(input('Dati un numar: '))
    palindrom = is_palindrome(n)
    print(f'Numarul {nr1} este {palindrom}')
    main()