import sqlite3


conn = sqlite3.connect('devices.db')


conn.execute('''
CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    imei TEXT,
    assigned_to TEXT
)
''')


def add_device(name, imei, assigned_to):
    conn.execute("INSERT INTO devices (name, imei, assigned_to) VALUES (?, ?, ?)", (name, imei, assigned_to))
    conn.commit()
    print(f"Dispositivo '{name}' adicionado com sucesso!")


def list_devices():
    cursor = conn.execute("SELECT id, name, imei, assigned_to FROM devices")
    for row in cursor:
        print(f"ID: {row[0]}, Nome: {row[1]}, IMEI: {row[2]}, Assinado para: {row[3]}")


def main():
    while True:
        print("\n--- Gerenciador de Dispositivos ---")
        print("1. Adicionar Dispositivo")
        print("2. Listar Dispositivos")
        print("3. Sair")
        choice = input("Escolha uma opção: ")

        if choice == '1':
            name = input("Nome do dispositivo: ")
            imei = input("IMEI do dispositivo: ")
            assigned_to = input("Assinado para: ")
            add_device(name, imei, assigned_to)
        elif choice == '2':
            list_devices()
        elif choice == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")

    
    conn.close()
    print("Programa encerrado.")


if __name__ == "__main__":
    main()