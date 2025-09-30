def calculator():
    """
    Простой консольный калькулятор
    Поддерживает базовые арифметические операции
    """
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /")
    print("Для выхода введите 'q'")
    print("-" * 30)
    
    while True:
            # Ввод первого числа
            num1_input = input("Введите первое число (или 'q' для выхода): ")
            if num1_input.lower() == 'q':
                print("Выход из калькулятора. До свидания")
                break
            
            num1 = float(num1_input)
            
            # Ввод операции
            operation = input("Введите операцию (+, -, *, /): ")
            if operation.lower() == 'q':
                print("Выход из калькулятора. До свидания")
                break
                
            if operation not in ['+', '-', '*', '/']:
                print("Ошибка: Неподдерживаемая операция")
                continue
            
            # Ввод второго числа
            num2_input = input("Введите второе число (или 'q' для выхода): ")
            if num2_input.lower() == 'q':
                print("Выход из калькулятора. До свидания")
                break
            
            num2 = float(num2_input)
            
            # Выполнение операции
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    print("Ошибка: Деление на ноль невозможно")
                    continue
                result = num1 / num2
            
            # Вывод результата
            print(f"Результат: {num1} {operation} {num2} = {result}")
            print("-" * 30)

if __name__ == "__main__":
    calculator()
