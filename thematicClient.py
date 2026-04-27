import socket

def client() -> None:
    """
    Клиент системы промышленной безопасности
    """
    HOST = '217.71.129.139' # IP сервера (гипервизора)
    PORT = 4393

    print("=" * 50)
    print(" Клиент промышленной безопасности")
    print(f" Подключение к {HOST}:{PORT}")
    print(' Для списка команд введите "помощь"')
    print(' Для выхода введите "bye"')
    print("=" * 50)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    print(" Подключено к серверу\n")

    message = input(" >> ")

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())

        data = client_socket.recv(1024).decode()
        print(f"\n{data}\n")

        message = input(" >> ")

    client_socket.close()
    print("\n Соединение закрыто. Безопасного производства!")

if __name__ == '__main__':
    client()
