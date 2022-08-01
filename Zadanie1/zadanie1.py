print("Kalkulator liczb zespolonych")
while True:
  choice = int(input("Wybierz akcję:\n0. Wyjście z programu\n1. Dodawanie\n2. Mnożenie\n3. Dzielenie\n"))
  if choice == 0:
    break
  elif choice == 1:
    x = int(input("Ile liczb zespolonych chcesz dodać? "))
    suma = 0
    for i in range(0, x):
      a = int(input("Podaj część rzeczywistą: "))
      b = int(input("Podaj część urojoną: "))
      c = complex(a, b)
      suma = suma + c
    print("Suma to:", suma, "\n")
  elif choice == 2:
    x = int(input("Ile liczb zespolonych chcesz pomnożyć? "))
    iloczyn = 1
    for i in range(0, x):
      a = int(input("Podaj część rzeczywistą: "))
      b = int(input("Podaj część urojoną: "))
      c = complex(a, b)
      iloczyn = iloczyn * c
    print("Iloczyn to:", iloczyn, "\n")
  elif choice == 3:
    a = int(input("Podaj część rzeczywistą dzielnej: "))
    b = int(input("Podaj część urojoną dzielnej: "))
    c = complex(a, b)
    d = int(input("Podaj część rzeczywistą dzielnika: "))
    e = int(input("Podaj część urojoną dzielnika: "))
    if d == 0 and e == 0:
      print("\nDzielnik nie może być równy 0!\n")
    else:
      f = complex(d, e)
      iloraz = c / f
      print("Iloraz to:", iloraz, "\n")
  else:
    print("Niepoprawna akcja, spróbuj jeszcze raz.")
