import ollama
import time

# --- Вспомогательная функция, которая является генератором ---
def generate_numbers(start, end):
    """Простой генератор, который выдает числа в заданном диапазоне."""
    print(f"  [Внутри generate_numbers: Начинаем с {start}]")
    for i in range(start, end + 1):
        yield i
        print(f"  [Внутри generate_numbers: Выдано {i}, продолжаем]")
    print(f"  [Внутри generate_numbers: Заканчиваем]")

# --- Функция с yield from ---
def delegating_generator(prompt_type):
    """
    Функция, которая использует 'yield from' для делегирования
    генерации другой функции.
    """
    print(f"\n--- Вызвана delegating_generator ({prompt_type}) ---")
    if prompt_type == "четные":
        result = generate_numbers(2, 6) # Генератор четных чисел
    else: # "нечетные" или любое другое
        result = generate_numbers(1, 5) # Генератор нечетных чисел

    print(f"  [Внутри delegating_generator: Передаем управление 'result' (генератору)]")
    yield from result # <-- Здесь делегирование
    print(f"  [Внутри delegating_generator: Управление возвращено после завершения 'result']")

# --- Функция с return ---
def returning_generator_object(prompt_type):
    """
    Функция, которая использует 'return' для возврата объекта генератора,
    а не является генератором сама по себе.
    """
    print(f"\n--- Вызвана returning_generator_object ({prompt_type}) ---")
    if prompt_type == "четные":
        result = generate_numbers(2, 6) # Генератор четных чисел


    print(f"  [Внутри returning_generator_object: Возвращаем объект генератора 'result']")
    return result # <-- Здесь возврат объекта


# --- Демонстрация ---

if __name__ == "__main__":
    print("=== Демонстрация 'yield from result' ===")
    # Вызываем delegating_generator. Она сама является генератором.
    # Поэтому мы можем сразу итерировать по ней.
    for value in delegating_generator("четные"):
        print(f"    [Из цикла: Получено значение: {value}]")

    print("\n\n=== Демонстрация 'return result' ===")
    # Вызываем returning_generator_object. Она НЕ является генератором.
    # Она возвращает ОБЪЕКТ генератора, по которому нужно итерировать отдельно.
    generator_obj = returning_generator_object("четные")
    print(f"    [Из цикла: Получен объект: {generator_obj}]") # Здесь будет напечатан объект генератора, а не значения

    # Теперь мы должны явно итерировать по возвращенному объекту генератора
    print("\n    [Из цикла: Начинаем итерацию по возвращенному объекту генератора:]")
    for value in generator_obj:
        print(f"    [Из цикла: Получено значение: {value}]")