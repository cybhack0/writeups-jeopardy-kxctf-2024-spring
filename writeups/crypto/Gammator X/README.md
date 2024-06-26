# Gammator X


## Описание

Чтобы исправить уязвимость в схеме шифрования Gammator 3000, разработавший её НИИ создал новую схему под названием Gammator X, которая вместо устаревших регистров линейного сдвига использует инновационные эллиптические кривые. Чтобы доказать, что ошибка, приводящая к раскрытию всей гаммы при знании 32 первых байт гаммы, была исправлена, разработчики выложили в сеть текст секретной презентации Gammator X, зашифрованный им же, а также первый параграф этого текста в открытом виде.  
Проанализировав новую криптосхему, вы осознали, что на первый взгляд, она действительно не имеет уязвимостей. Расстроившись, вы отправились в ближайшее пивное заведение (Дисклеймер: алкоголь вредит вашему здоровью). Там вас ждала неожиданная встреча. Вы увидели работника НИИ, который, по добытой вами информации, был участником разработки Gammator X. Учёный был уже в изменённом состоянии сознания. Вы начали разговаривать с ним на разные темы, связанные с криптографией. В порыве разговора, учёный случайно проболтался. Оказывается, что тайное рептилоидное правительство заставило его вшить в Gammator X небольшой бэкдор. Он заключается в следующем: 11Q=P.  
Надеюсь, что полученная информация поможет вам расшифровать текст презентации и получить содержащейся в ней секретный флаг.  


flag: kxctf{7r1cky_l177l3_b4ckd00r}


## Writeup


Пусть *s<sub>0</sub>*, *s<sub>1</sub>*, ... - внутренние состояния генератора гаммы (s<sub>0</sub> — это, 
соответственно, ключ).  
Схема работы генератора следующая:  
    *s<sub>i</sub> = x(s<sub>i-1</sub> \* P) mod 2\*\*256*  
    *r<sub>i</sub> = x(s<sub>i</sub> \* Q) mod 2\*\*256*  
    *output += младшие 30 байт r<sub>i</sub>*  
Здесь функция *x()* - взятие первой координаты точки кривой.  
Ксорим известную часть открытого текста с шифрованным текстом и получаем, первые несколько байт гаммы. Из них нам нужно первые *30* байт, так как они являются байтами внешнего состояния генератора *r<sub>1</sub>*.  
Перебором восстанавливаем недостающие *2* байта *r<sub>1</sub>*. Зная *r<sub>1</sub>*, мы можем получить точку на эллиптической кривой *A*, в которой *r<sub>1</sub>* будет первой координатой.  
Мы знаем, что *A = s<sub>1</sub> \* Q*. Также из полученной методом социальной инженерии информации мы знаем, что *11Q=P*. Следовательно *11A = 11 \* s<sub>1</sub> \* Q = s<sub>1</sub> \* P*.  
Теперь мы можем восстановить *s<sub>2</sub>*: *s<sub>2</sub> = x(s<sub>1</sub> \* P) mod 2\*\*256*.  
Зная *s<sub>2</sub>*, мы можем подставить его в качестве ключа в генератор, и получить всю остальную гамму.  