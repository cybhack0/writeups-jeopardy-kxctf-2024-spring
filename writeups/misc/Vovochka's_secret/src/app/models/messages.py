class MSG:
    HELLO = '''
        Добро пожаловать в мою хранилку секретов!
        Чтобы добавить новый секрет, напиши /add
        Чтобы прочитать секрет, напиши /get
        /list
    '''

    HELP = '''
        Чтобы добавить новый секрет, напиши /add
    Чтобы прочитать секрет, напиши /get
    Чтобы увидеть все секреты, напиши /list
    '''

    ADD = '''
        Чтобы добавить новый секрет, напиши его вот в таком формате:
        <название скерета>:<секрет>
    '''

    ERROR_ADD = '''
        Кажется, ты делаешь что-то странное!!!
        Напиши секрет вот в таком формате:
        <название скерета>:<секрет>
    ''' 

    GET = '''
        Запроси скекрет вот в таком формате:
        <название секрета>:<пароль>
    '''

    ERROR_GET = '''
        Кажется, ты делаешь что-то странное!!!
        Запроси скекрет вот в таком формате:
        <название секрета>:<пароль>
    ''' 