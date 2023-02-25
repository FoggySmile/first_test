from first_test.capitalize import capitalize

# Если результат функции не равен ожидаемому значению
if capitalize('hello') != 'Hello':
    # Выбрасываем исключение и завершаем выполнение теста
    raise Exception('Функция работает неверно!')

if capitalize('') != '':
    raise Exception('Функция работает неверно!')

print('Все тесты пройдены!')