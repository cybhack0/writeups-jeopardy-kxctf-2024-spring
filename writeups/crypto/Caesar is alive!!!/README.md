# Caesar is alive!!!

## Описание

По версии историков, через два месяца после смерти Цезаря Брут нашёл в его покоях записку следующего содержания:

«Я знал, что ты найдёшь моё послание именно сейчас. Но тебе всё равно никогда не разгадать его...»

Тайна сообщения, которое вы видите перед собой, до сих пор осталась нераскрытой. Кажется, великий полководец хорошо умел думать наперёд.

Человек умрёт, но не его идеи...

# Writeup

Заметим, что шифрованное сообщение можно разбить следующие блоки:

`s13 w31 t11 t30 w3 m1 t30 f19 w31 t18 f2 t18 f5 w31 s3 m1 s7 w31 s28 s14`

И больше как будто бы неизвестно ничего... Может, какая-то информация есть в условии?

1. Цезарь умер 15 марта 44 года до н.э.
2. Через 2 месяца было 15 мая 44 года до н.э.

Известны только даты. Что на это скажет поисковик?

![](/img/search.png)

Теперь, зная, что речь о мае 44 года до нашей эры, ищем нужный календарь [невисокосного года, начинающегося в воскресенье](https://ru.wikipedia.org/wiki/44_год_до_н._э.). Нам подойдёт, например, календарь на май 2023 года. Получается вот такой «ключ»:

![](/img/calendar.png)

Теперь по нему можем расшифровать флаг:

`m4k3ca3s4r6re47ag41n`