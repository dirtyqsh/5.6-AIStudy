s = input("Enter text: ")
result_s = ''

for i in s:
    if i.isupper():
        result_s += i

print(f'Текст: "{s}", если мы соберем все заглавные буквы, то получим сообщение "{result_s}".')