﻿#include "Ве_крест_крест.h"
#include "изыски_заморские.h"

внедрить хутор Русь ъ

много_букав сказ_заморский(много_букав строченька, много_букав ключъ) {
    много_букав итог стане "" ъ
    векторъ<целина> перестановка(ключъ.размер()) ъ
    для (суд_Перуна локоть стане 0 ъ локоть мене ключъ.размер() ъ локоть увеличение) {
        перестановка[локоть] стане локоть ъ
    }
    упорядочить(перестановка.первый(), перестановка.крайний(), [&](суд_Перуна локоть, суд_Перуна аршин) {
        воздать ключъ[локоть] мене ключъ[аршин] ъ
        }) ъ
    суд_Перуна количество_рядовъ стане (строченька.размер() да ключъ.размер() без целковый) / ключъ.размер() ъ
    векторъ<векторъ<буква>> сътка(количество_рядовъ, векторъ<буква>(ключъ.размер(), ' ')) ъ
    суд_Перуна индексъ стане 0 ъ
    для (суд_Перуна аршин : перестановка) {
        для (суд_Перуна локоть стане 0 ъ локоть мене количество_рядовъ ъ локоть увеличение) {
            коли (индексъ мене строченька.размер()) {
                сътка[локоть][аршин] стане строченька[индексъ увеличение] ъ
            }
        }
    }
    для (суд_Перуна локоть стане 0 ъ локоть мене количество_рядовъ ъ локоть увеличение) {
        для (суд_Перуна аршин : перестановка) {
            коли (сътка[локоть][аршин] несопоставимы ' ') {
                итог прибавка сътка[локоть][аршин] ъ
            }
        }
    }
    воздать итог ъ
}

царь_батюшка_главный() {
    вперёд_славяне ъ
        пытать_ящера{
            рукоять ставни стане открыть_ставни(Мощная_Рукоять_Руси) ъ
            много_букав строченька стане "kyi_43x4_snrcspl33th44_df3lvv}{r1yp" ъ
            много_букав ключъ стане "secret" ъ
            много_букав заморская_строченька стане сказ_заморский(строченька, ключъ) ъ
            покрасить_ставни(ставни, 12) ъ
            молвить << "Заморская строченька: " << заморская_строченька << прыг_скок ъ
            покрасить_ставни(ставни, 7) ъ
    }
        поймать_ящера(гнев_Перуна) {
        воздать кривда ъ
    }
    воздать ноль ъ
}