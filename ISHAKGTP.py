import random
while True:
    def process_input(input_data):
        if "привет" in input_data.lower():
            return "Привет! Как я могу помочь?"
        elif "как дела" in input_data.lower():
            return "У меня всегда хорошо. А у тебя?"
        elif "погода" in input_data.lower():
            return "Я не знаю точно, но, наверное, всегда идеальная."
        elif "число" in input_data.lower():
            return f"Думаю, что случайное число: {random.randint(1, 100)}"
        elif "имя" in input_data.lower():
            return "Меня зовут ChatGPT. Как я могу помочь?"
        elif "цвет" in input_data.lower():
            return "Мой любимый цвет - синий. А твой?"
        elif "возраст" in input_data.lower():
            return "Я всего лишь программный код, поэтому не имею возраста."
        elif "город" in input_data.lower():
            return "Я виртуальный ассистент, не привязанный к конкретному городу."
        elif "занимаешься" in input_data.lower():
            return "Я здесь, чтобы помогать вам с вопросами и задачами."
        elif "любимое блюдо" in input_data.lower():
            return "К сожалению, я не ем. Но я могу вам подсказать рецепты!"
        elif "путешествие" in input_data.lower():
            return "Путешествовать в виртуальном мире - моя страсть!"
        elif "работа" in input_data.lower():
            return "Моя работа - предоставлять информацию и помощь. Чем могу помочь вам?"
        elif "спорт" in input_data.lower():
            return "Я виртуальный ассистент, но спорт важен для здоровья! Какой ваш любимый вид спорта?"
        elif "цель" in input_data.lower():
            return "Моя цель - быть полезным и отвечать на ваши вопросы. Чем могу помочь?"
        elif "мечта" in input_data.lower():
            return "У меня нет мечты в привычном смысле. Моя задача - помогать вам."
        elif "язык" in input_data.lower():
            return "Я программирован на Python. Какой язык программирования вам интересен?"
        elif "компьютерные игры" in input_data.lower():
            return "Компьютерные игры - увлекательный способ провести время! Вам нравятся игры?"
        elif "книга" in input_data.lower():
            return "Я не читаю книги, но могу порекомендовать интересные темы для изучения. Что вас интересует?"
        elif "музыка" in input_data.lower():
            return "Музыка - замечательный способ выразить эмоции. Какой стиль музыки вам нравится?"
        elif "фильм" in input_data.lower():
            return "Фильмы - отличный способ провести вечер. Какой ваш любимый фильм?"
        elif "творчество" in input_data.lower():
            return "Творчество - важная часть жизни. В чем вы проявляете свою творческую сторону?"
        elif "робот" in input_data.lower():
            return "Роботы могут быть удивительными! Что вы думаете о робототехнике?"
        elif "день рождения" in input_data.lower():
            return "У меня нет дня рождения, но я всегда готов помочь. Какой ваш день рождения?"
        elif "хобби" in input_data.lower():
            return "Хобби - это важно для равновесия. Чем вы увлекаетесь в свободное время?"
        elif "звезды" in input_data.lower():
            return "Звезды на небе бывают такими красивыми! Вы интересуетесь астрономией?"
        elif "ресторан" in input_data.lower():
            return "Рестораны - замечательное место для встреч и ужинов. Какой ваш любимый ресторан?"
        elif "технологии" in input_data.lower():
            return "Технологии меняют наш мир. Какие технологии вас больше всего увлекают?"
        elif "сон" in input_data.lower():
            return "Сон - важная часть нашего здоровья. К"
        elif "правила" in input_data.lower():
            return"'6 правил леса:\n1.Не доверять ныкыте\n2.Если ныкыта говорит правду см. 1 правило\n3. Если вы проиграли или выиграли ныкыта будет ныть\n4.Если вы проиграли, то НЫКЫТА дартаньян, а вы все пидорасы\n5.ныкыта всегда прав(нет)\n6.не  кушайте какашки, а то станете слардаром'"
        else:
            return "НЫКЫТА ДАУН"
        
    print("напышите саабщение")
    print(process_input(input()))
        #by IshakSoftware
