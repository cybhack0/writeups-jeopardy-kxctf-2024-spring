# velikorusiy obstrel writeup

Нам дан код написанный на Старославянском ЯП. Нужно заставить его работать.

### Начало битвы

Открываем файл и видим в первой строке `#include "изыски_заморские.h"`, в нем находятся часть define нужные для работы, требуется восстановить все define.

```cpp
#define рукоять HANDLE
#define малая_рукоять handle
#define диковинки attributes
#define инструмент device
#define открыть_ставни(инструмент) GetStdHandle(инструмент)
#define покрасить_ставни(малая_рукоять, диковинки) SetConsoleTextAttribute(малая_рукоять, диковинки)
#define Мощная_Рукоять_Руси STD_OUTPUT_HANDLE
...
```

Сделать это можно двумя способами:
1) Анализ кода
2) Найти источники в интернете [[1]](https://github.com/KanatnikovMax/znanie-drevnix), [[2]](https://www.av13.ru/notes/ancient-slavic-c/)

После восстановления кода, просто запускаем его и получаем флаг: **kxctf{y4sh3ri_p4l1_sl4vy4n3_vp3r3d}**