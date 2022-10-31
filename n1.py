num = int(input("Enter num: "))

fizz_buzz = ("Fizz Buzz" if (num % 3 == 0 and num % 5 == 0) else
             "Fizz" if num % 3 == 0 else
             "Buzz" if num % 5 == 0 else
             str(num))

print(f'x = {num}, результат: "{fizz_buzz}"')