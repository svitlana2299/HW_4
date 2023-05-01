USERS = {}

# Функція-декоратор для обробки виключень від користувача


def input_error(func):
    def wrapper(*args):
        try:
            result = func(*args)
            return result
        except KeyError:
            return "Contact not found"
        except ValueError:
            return "Please provide a name and phone number"
        except IndexError:
            return "Please provide a name"
    return wrapper

# Функція для відображення привітання


def greeting():
    return "How can I help you?"


def unknown_command():
    return "Invalid command. Please try again."


def exit_program():
    return None

# Функція для додавання нового контакту


@input_error
def add_contact(name, phone):
    USERS[name] = phone
    return f"{name} has been added to your contacts"

# Функція для зміни номера телефону існуючого контакту


@input_error
def change_contact(name, phone):
    old_phone = USERS[name]
    USERS[name] = phone
    return f"{name}'s phone number has been updated"

# Функція для відображення номера телефону для зазначеного контакту


@input_error
def show_phone(name):
    if name not in USERS:
        return "Contact not found"
    return f"{name}'s phone number is {USERS[name]}"

# Функція для відображення всіх збережених контактів


def show_all():
    if not USERS:
        return "You have no contacts yet"
    result = "Your contacts:\n"
    for name, phone in USERS.items():
        result += f"{name}: {phone}\n"
    return result


HANDLERS = {
    'hello': greeting,
    'add': add_contact,
    'change': change_contact,
    'show all': show_all,
    'exit': exit_program,
    'good bye': exit_program,
    'close': exit_program,
    'phone': show_phone
}


def parse_input(user_input):
    command, *args = user_input.split()
    command = command.lstrip()

    try:
        handler = HANDLERS[command.lower()]
    except KeyError:
        if args:
            command = command + ' ' + args[0]
            args = args[1:]
        handler = HANDLERS.get(command.lower(), unknown_command)

    if command.lower() == "change" and len(args) == 2:
        args = [args[0], args[1]]
    return handler, args

# Головна функція, що виконується у безкінечному циклі та чекає команди користувача


def main():
    print("Welcome to the contacts bot!")
    while True:
        user_input = input('Please enter command and args: ')
        handler, args = parse_input(user_input)
        result = handler(*args)
        if result is None:
            break
        print(result)
    message = "Good bye!"
    print(message)


# Запуск головної функції
if __name__ == "__main__":
    main()
