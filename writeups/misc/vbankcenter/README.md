# vbankcenter: Write-Up

На первый взгляд нам дан вордовский файл, в котором лежит картинка и больше ничего. Но если обратить внимание на его расширение, то увидим `.docm`, этот формат файлов позволяет исполнять VBA скрипты внутри файла.

### Как найти скрипт?

Для этого нужно включить возможности разработчика в Word и перейти во вкладку `Visual Basic`. Тут и лежит наш скрипт, но при попытке его исполнить вызовется ошибка, нужно проанализировать код.

### Анализ

Сразу бросается в глаза метод Execute(), в которую все обернуто. Просмотрев содержимое можно понять, что `chr("MTE4Ng=="-1110)& ...` это представление символов, объединенных в текст.

Разберем из чего состоит символ. Первая часть `"MTE4Ng=="` - преобразована в base64, вернем ее в привычный формат используя данный [сайт](https://www.base64decode.org/) и получим `1186`. Далее видим, что из полученного числа отнимается `1110`, результатом является число `76`, что соответсвует символу `L` ascii-таблицы. Преобразованием из числа в символ, как раз занимается функция `chr()`. Вспоминаем про наш метод `Execute()`, который не совсем подходит сюда, найдем его аналоги для строки - `MsgBox()` отличный вариант для вывода текста.

Таким образом преобразовав весь код и по частям вызывая метод `MsgBox()` получаем наш текст, среди которого и спрятан флаг: **kxctf{vb4_1s_n0t_s0_b4d?}**

### Альтернатива

Данное решение можно автоматизировать, ведь никому не хочется заниматься этим вручную. Для этого напишем скрипт на python, который распарсит и преобразует код.

```python
import base64 as b

final = ''
with open("file.txt",'r') as file:
    payload = file.readlines()[0].split('&')
    for char in payload:
        char1 = int(b.b64decode(char.split('"')[1]))
        char2 = int(char.split('"')[2][1:-1])
        sign = char.split('"')[2][0]
        if sign == '+':
            final += chr(char1+char2)
        else:
            final += chr(char1-char2)
print(final)
```
