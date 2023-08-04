# Декоратор для обробки помилок вводу користувача
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        # Обробка помилки, якщо не знайдено контакт за ключем у словнику
        except KeyError:
            return "Contact not found!"
        # Обробка помилки, якщо користувач ввів некоректний формат команди
        except ValueError:
            return "Invalid input. Please enter a valid name and phone number separated by a space."
        # Обробка помилки, якщо користувач ввів неправильну команду
        except IndexError:
            return "Invalid input. Please enter a valid command."
    return inner

# Словник для збереження контактів (ім'я користувача як ключ, номер телефону як значення)
contacts = {}

# Декоратор @input_error додається до кожної з функцій-обработчиків команд

# Функція для додавання нового контакту
@input_error
def add_contact(name, phone):
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' has been added."

# Функція для зміни номера телефону існуючого контакту
@input_error
def change_phone(name, phone):
    contacts[name] = phone
    return f"Phone number for contact '{name}' has been changed to '{phone}'."

# Функція для отримання номера телефону за іменем контакту
@input_error
def get_phone(name):
    return f"The phone number for contact '{name}' is '{contacts[name]}'."

# Функція для виведення всіх збережених контактів
def show_all():
    if not contacts:
        return "No contacts found."
    else:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result

# Основна функція, яка виконує взаємодію з користувачем
def main():
    while True:
        command = input("Enter a command: ").lower()  # Запит користувача на введення команди
        if command in ['good bye', 'close', 'exit']:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            _, name, phone = command.split()
            print(add_contact(name, phone))  # Виклик функції для додавання контакту
        elif command.startswith("change"):
            _, name, phone = command.split()
            print(change_phone(name, phone))  # Виклик функції для зміни номера телефону
        elif command.startswith("phone"):
            _, name = command.split()
            print(get_phone(name))  # Виклик функції для отримання номера телефону за іменем контакту
        elif command == "show all":
            print(show_all())  # Виклик функції для виведення всіх контактів
        else:
            print("Invalid command. Please try again.")  # Виведення повідомлення про неправильну команду

if __name__ == "__main__":
    main()  # Запуск основної функції взаємодії з користувачем
    