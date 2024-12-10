def log_start(func):
    def wrapper():
        print("Бот запущено!")
        func()
    return wrapper
