import socket

def server() -> None:
    """
    Эхо-сервер промышленной безопасности
    """
    HOST = '172.17.12.38'
    PORT = 3333

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(2)

    print("Сервер промышленной безопасности запущен")
    print(f"Адрес: {HOST}:{PORT}")

    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        print("From connected user: " + str(data))

        # Обрабатываем команду и получаем ответ
        response = process_safety_command(data)
        conn.send(response.encode())

    conn.close()

def process_safety_command(command: str) -> str:
    """Обработка команд по промышленной безопасности"""
    cmd = command.lower().strip()

    if cmd == "охрана":
        return " Охрана труда: система сохранения жизни и здоровья работников"
    elif cmd == "пожар":
        return " Пожарная безопасность: предотвращение пожаров и защита людей"
    elif cmd == "риск":
        return " Оценка рисков: выявление опасностей на рабочих местах"
    elif cmd == "соут":
        return " СОУТ: специальная оценка условий труда"
    elif cmd == "инструктаж":
        return " Инструктажи: вводный, первичный, повторный, внеплановый, целевой"
    elif cmd == "авария":
        return " ПЛА: план ликвидации аварий на производстве"
    elif cmd == "экспертиза":
        return " Экспертиза промышленной безопасности опасных объектов"
    elif cmd == "помощь":
        return """
Доступные команды:
• охрана     — охрана труда
• пожар      — пожарная безопасность  
• риск       — оценка рисков
• соут       — спецоценка условий труда
• инструктаж — виды инструктажей
• авария     — план ликвидации аварий
• экспертиза — экспертиза промбезопасности
• помощь     — эта справка
• bye        - выход
"""
    elif cmd == "bye":
        return "До свидания!"
    else:
        return f"Неизвестная команда: '{command}'. Введите 'помощь' для списка команд"

if __name__ == '__main__':
    server()
