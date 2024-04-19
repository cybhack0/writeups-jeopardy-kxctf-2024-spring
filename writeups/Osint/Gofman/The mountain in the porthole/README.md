# Горав в иллюминаторе
## Описание: Найди бортовой номер самолета, с которого сделана фотография

Формат флага: kxctf{Бортовой номер}

![plane](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/dc82b345-c5eb-4faf-acb8-af48ea0691ab)

## Решение:
Для начала, получим всю информацию об изображении. С помощью exiftool узнаем, что фотография была сделана 26.02.2023 в 07:33:56. Сохраняем эту информацию.

## Анализ изображения
***Гора:*** Эльбрус - самая высокая гора России и Европы (5642 м.). Используйте поиск по картинкам, он такой один.

![Screenshot_1](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/482f2650-b375-4c43-8d7a-f55b686f657d)

***Самолет:*** Поискав ливреи авиалайнеров, можно сделать вывод, что судно принадлежит компании Аэрофлот. Очевидно, что борт не "на эшелоне", что означает набор/снижение высоты. 
Ближайшие аэропорты к Эльбрусу:

![Screenshot_2](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/6b26ff90-03f3-4879-92a8-483edf3662ce)

Определим садится или взлетает борт и куда или откуда соответственно. Объектив направлен перпендикулярно траектории полета самолета. 

***Посадка и взлет в Нальчике***
![Screenshot_3](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/579a209b-c880-462e-acfa-9b778448f5d6)
![Screenshot_4](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/c976cc89-390c-47e3-9eb4-5d2ebdf60338)
Аэропорт г. Нальчик отпадает. 

При посадке в аэропорт Минеральных Вод, Эльбрус ***не видно*** с правого борта (траекторию можно посмотреть на любом доступном радаре). Единственный вариант - взлет из Минеральных Вод.
Заглядываем в прошлое и находим аэропорт Минеральных Вод на ADS-B.

![Screenshot_6](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/55b41482-5c09-4292-872f-d97854431a9a)

![Screenshot_7](https://github.com/cybhack0/writeups-jeopardy-kxctf-2024-spring/assets/122211306/b7c3dafb-ac7e-486d-ae3a-1a96da559db8)

lxctf{RA-73758}