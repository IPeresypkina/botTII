# -*- coding: utf-8 -*-

welcome_message = "Добро пожаловать в проект Робот-ЭС."

solve_message = "Если вы не уверены в результате, то вы можете нажать на кнопку ниже для объяснения решения."

first_response = "\nДля начала выберите кто перед вами: \n\n" \
                 "1. Собака\n" \
                 "2. Кошка \n"\

section_one_questions = [
    "Какая собака? Длиношерстная или короткошерстная?", #1
    "У собаки короткий или длинный хвост?", #2
    "Какой рост собаки? Менее 50см или более?", #3
    "Собака весит более 50кг или менее?", #4
    "У собаки доброжелательный характер?", #5
    "У собаки рост менее 70см или более?", #6
    "У собаки длинные уши или короткие?", #7
    "Тело длинное или короткое?", #8
    "Окрас рыжий с белыми отметинами?", #9
    "Белоснежный окрас?" #10
]

section_one_answers = [
    "Английский бульдог", #1
    "Мопс", #2
    "Чихуахуа", #3
    "Гончая", #4
    "Английский фоксхаунд", #5
    "Немецкий дог", #6
    "Ирландский красный сеттер", #7
    "Английский кокер-спаниель", #8
    "Колли", #9
    "Большой вандейский гриффон", #10
    "Ньюфаундленд", #11
    "Ирландский волкодав", #12
    "Сенбернар" #13
]

section_two_questions = [
    "Какая кошка? Длиношерстная или короткошерстная?", #1
    "Какой вес кошки? Менее 6кг или более?", #2
    "У кошки короткий или длинный хвост?", #3
    "У кошки доброжелательный характер?", #4
    "У кошки 7 пальцев на передних лапах?", #5
    "У кошки вислоухие уши?", #6
    "Окрас рыжий?", #7
    "Окрас пятнистый?", #8
]

section_two_answers = [
    "American Bobtail", #1
    "Пиксибоб", #2
    "Тайская кошка", #3
    "Абиссинская кошка", #4
    "Британская короткошёрстная кошка", #5
    "Шотландская вислоухая кошка", #6
    "Саванна (порода_кошек)", #7
    "Картезианская кошка", #8
    "Хауси", #9
    "Персидская кошка", #10
    "Британская длинношерстная кошка", #11
    "Шотландская вислоухая кошка", #12
    "Курильский бобтейл", #13
    "Японский бобтейл", #14
    "Норвежская лесная кошка", #15
    "Мейн-кун" #16
]

section_one_history_answers = [
    "Вы выбрали варианты ответа: собака \"короткошерстная\", ", #1
    "Вы выбрали варианты ответа: собака \"длинношерстная\", ", #2
    "рост \"менее 50см\", ", #3
    "рост \"более 50см\", ", #4
    "вес \"менее 50кг\", ", #5
    "вес \"более 50кг\", ", #6
    "уши \"короткие\", ", #7
    "уши \"длинные\", ", #8
    "тело \"короткое\", ", #9
    "тело \"длинное\", ", #10
    "характер \"доброжелательный\", ", #11
    "характер \"не доброжелательный\", ", #12
    "окрас \"рыжий с белыми отметинами\", ", #13
    "окрас \"не рыжий с белыми отметинами\", ", #14
    "окрас \"белоснежный\", ", #15
    "окрас \"не белоснежный\", ", #16
    "рост \"менее 70см\", ", #17
    "рост \"более 70см\", ", #18
    "хвост \"короткий\", ", #19
    "хвост \"длинный\", ", #20
]

section_two_history_answers = [
    "Вы выбрали варианты ответа: кошка \"короткошерстная\", ", #1
    "Вы выбрали варианты ответа: кошка \"длинношерстная\", ", #2
    "вес \"менее 6кг\", ", #3
    "вес \"более 6кг\", ", #4
    "хвост \"короткий\", ", #5
    "хвост \"длинный\", ", #6
    "уши \"вислоухие\", ", #7
    "уши \"не вислоухие\", ", #8
    "характер \"доброжелательный\", ", #9
    "характер \"не доброжелательный\", ", #10
    "окрас \"рыжий\", ", #11
    "окрас \"не рыжий\", ", #12
    "окрас \"пятнистый\", ", #13
    "окрас \"не пятнистый\", ", #14
    "имеет 7 пальцев на передних лапах, ", #15
    "не имеет 7 пальцев на передних лапах, ", #16
]

section_one_explanation_question = [
    "<b>Короткошёрстные собаки</b> характеризуются очень короткой, гладкой, прямой шерстью на всех частях тела. "
    "Подшёрсток отсутствует или слаборазвит.\n"
    "<b>Длинношёрстные собаки</b> имеют длинный шелковистый покровный волос на шее и туловище, "
    "часто он образует свисающую бахрому. Развитие подшёрстка у длинношёрстных собак определяется условиями содержания. "
    "Шерсть длинношёрстных собак может быть прямой, волнистой или вьющейся. "
    "У пуделеобразных собак длинная волнистая шерсть расположена по всему телу, шерсть может ниспадать волнами, "
    "скручиваться шнурами или сваливаться в войлокообразные ленты", #1

    "Длину <b>хвоста</b> принято измерять по отношению к скакательному суставу: длина <b>хвоста</b>, "
    "достигающего его своим концом, считается нормальной. <b>Длинным</b> считается хвост, "
    "конец которого ниже скакательного сустава, а <b>короткий</b> - если он его не достигает.", #2

    "Найти где у собаки холка просто – начало этой части тела расположено сразу после шеи. "
    "Холка – это первые пять позвонков спинного отдела позвоночника, находящиеся в начале спины между лопатками."
    "Соответственно, рост собаки измеряет от пола до верхней части холки.", #3

    "Существует несколько простых способов определить вес собаки в домашних условиях. "
    "Собак маленьких пород, а также щенков можно взвесить в сумке при помощи безмена. "
    "Для более точного вычисления массы тела можно взвесить сумку отдельно и вычесть это значение из общего результата.\n"
    "Чтобы иметь хотя бы приблизительное представление о весе животных, издавна используют определение живого веса животных по промерам с использованием специальных таблиц."
    "Чтобы определить вес животного, можно использовать обычную мерную рулетку длиной не менее 3 м."
    "Лентой нужно измерить обхват груди за лопатками (обвести лентой вокруг туловища так, чтобы она легла под грудь на расстоянии ширины ладони от локтя) "
    "и косую длину туловища (расстояние от переднего выступа плечевого сустава до седалищного бугра). "
    "Понадобится еще промер длины туловища - от середины холки до корня хвоста. Используя полученные результаты, "
    "по таблице определяют живую массу животного в килограммах.", #4

    "Доброжелательное выражение морды, сопровождаемое легким помахиванием хвостом, "
    "отражает спокойствие или дружелюбную заинтересованность. Интенсивное махание хвостом в сочетании с радостным лаем, "
    "прыжками говорит о ликовании, выражает буйную радость. Быстрое движение опущенным хвостом при склоненной голове — "
    "поза умиротворения. Легкое подрагивание вытянутым хвостом свидетельствует о настороженном ожидании и, возможно, "
    "агрессивном развитии событий.", #5

    "Найти где у собаки холка просто – начало этой части тела расположено сразу после шеи. "
    "Холка – это первые пять позвонков спинного отдела позвоночника, находящиеся в начале спины между лопатками."
    "Соответственно, рост собаки измеряет от пола до верхней части холки.", #6

    "В сравнении с размером головы собаки стоячие уши могут быть большими, средними, небольшими или маленькими, "
    "а висячие уши различаются по длине и ширине.", #7

    "Некоторых псов природа наградила особенными параметрами: длинным телом и короткими лапами.", #8

    "Двухцветные окрасы могут образовываться сочетанием сплошного окраса с белыми пятнами. "
    "Белые пятна могут быть покрыты тёмным крапом, пятна могут состоять из смеси белых и окрашенных волос. "
    "Сочетание белых пятен со сплошным окрасом образует бело-чёрный, бело-рыжий окрасы и их осветлённые модификации. "
    "Другой вариант двухцветной раскраски — смешанный окрас, когда по телу собаки в определённом порядке расположены "
    "эумеланиновые и феомеланиновые зоны (подпалый, чепрачный).", #9

    "Одноцветные, или сплошные, окрасы образуются при равномерном распределении пигмента (эумеланина или феомеланина) "
    "по корпусу собаки. Эффект сплошного окраса может достигаться в результате возрастного осветления, "
    "а также при крайней степени белой пятнистости." #10
]

section_two_explanation_question = [
    "Длительное время кошек по длине шерсти относили к двум типам: \n"
    "<b>короткошерстные</b>, с длиной шерсти до 5 см \n"
    "<b>длинношерстные</b>, с длиной шерсти свыше 5 см \n"
    "Сегодня заводчики расширили этот диапазон благодаря разведению новых уникальных пород кошек. "
    "Так, появились бесшерстные представители кошачьих, которые могут быть голыми, либо иметь шерсть, "
    "не превышающую в длину 1 см.", #1

    "К наиболее простым и распространенным относятся следующие способы взвешивания:\n"
    "• При помощи бытовых напольных весов. Сначала хозяину следует взвеситься самому, а потом с котом на руках. "
    "Вычтя из результата совместного взвешивания собственный вес, Вы узнаете вес кота с точностью до 0,1 кг. "
    "Если кошка царапается и проявляет признаки недовольства, рекомендуется отложить процедуру или попробовать "
    "применить другой способ.\n"
    "• Аналогичным способом можно взвесить котенка или взрослого кота используя кошачий домик или любую другую емкость, "
    "привычную для кота. Ведь зачастую любимыми местами отдыха питомца являются коробки из-под обуви или плетеные корзинки.\n"
    "• При помощи более точных электронных кухонных весов выполняется взвешивание котят и котов мелких пород.\n"
    "• При помощи ручного безмена. Для применения этого способа кота требуется поместить в сумку-переноску, "
    "что нравится далеко не всем домашним любимцам.\n"
    "• При помощи специальных весов во время посещения ветеринарной клиники. Обычно такую услугу предоставляют бесплатно.\n", #2

    "Примечателен тот факт, что нахождение хвоста в «зачаточном» состоянии или его полное отсутствие у кошек "
    "является признаком «благородного» происхождения (в отличие от тех же домашних собак, у которых хвосты купируются "
    "намеренно – для подгонки животных под стандарты той или иной породы).", #3

    "Выразительные большие глаза, подвижные ушки, умеющие поворачиваться на 180° и усы способны передать полную гамму "
    "эмоций животного. В зависимости от настроения, кошачья мордочка может выглядеть следующим образом:\n"
    "• Состояние покоя – ушки подняты вертикально, ушная раковина развернута вперед, взгляд внимательный и спокойный.\n"
    "• Игривое настроение – настороженные ушки, широко открытые глаза.\n"
    "• Злость, гнев, недовольство – уши находятся в напряженном состоянии и развернуты назад, зрачки сужены, усы направлены вперед.\n"
    "• Удовлетворение, симпатия – мимические мышцы расслаблены, а глаза наполовину прикрыты.\n"
    "• Готовность к атаке, агрессия или страх – широко открытые глаза, расширенные зрачки, зачастую «остекленевший» взгляд, уши и усы прижаты к голове.\n"
    "Иногда создается впечатление, что хвост живет отдельной от кота жизнью."
    "Животное может находиться в полностью неподвижном или напряженном состоянии, в то время как хвост будет выписывать "
    "замысловатые кренделя, мотаться из стороны в сторону или напряженно постукивать по полу. "
    "Как понять настроение кота по движениям хвоста можно узнать, опираясь на следующие наблюдения:", #4

    "Признак полидактилийности (многопалость) не является обязательным, так же он не является характерным. "
    "Хотя, весьма очаровательно выглядят кошки и коты с многопалыми лапками.", #5

    "У некоторых домашних кошек явной отличительной чертой, относящей их к определенной породе, "
    "являются уши – а точнее их необычная форма или размеры. Органы слуха у питомцев могут быть вогнутыми "
    "(таких кошек называют вислоухими), вывернутыми или особо большими.", #6

    "Тёмно-рыжий окрас, с хорошо прокрашенным волосом до корней, без рисунка и светлых пятен. Мочка носа и подушечки лап — кирпично-красные.", #7

    "Пятнистый, как и полосатый окрас, характеризуется наличием гена T (Табби). Такая расцветка бывает только у кошек и, "
    "преимущественно, у диких ее видов. Основная шерсть у пятнистых животных светлее, чем пятна. "
    "Их рисунок может быть в виде круглых отметин, «розеток» или мраморный.", #8
]

def select_message(section, message_id, m_type):
    if section == 1:
        if m_type == 'question':
            return section_one_questions[message_id - 1]
        if m_type == 'answer':
            return section_one_answers[message_id - 1]
        if m_type == 'explanation':
            return section_one_explanation_question[message_id - 1]
        if m_type == 'history':
            return section_one_history_answers[message_id - 1]
    if section == 2:
        if m_type == 'question':
            return section_two_questions[message_id - 1]
        if m_type == 'answer':
            return section_two_answers[message_id - 1]
        if m_type == 'explanation':
            return section_two_explanation_question[message_id - 1]
        if m_type == 'history':
            return section_two_history_answers[message_id - 1]
