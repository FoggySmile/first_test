from first_test.capitalize import capitalize

# Если результат функции не равен ожидаемому значению
# Выбрасываем исключение и завершаем выполнение теста
assert capitalize('') == ''
assert capitalize('hello') == 'Hello'

print('Все тесты пройдены!')