s = input("Enter text: ").split()

result_s = ",".join(s).replace("right", "left")

print(f"{s}, результат: '{result_s}'")