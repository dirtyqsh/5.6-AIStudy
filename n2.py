x = int(input("Enter x: "))

result = ("Плохо" if x % 2 != 0 else
          "Неплохо" if 2 <= x <= 5 else
          "Так себе" if 6 <= x <= 20 else
          "Отлично" if x > 20 else
          "Ужасно :)")

print(f"x = {x}, результат: {result}")