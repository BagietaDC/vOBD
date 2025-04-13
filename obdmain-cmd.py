import obd

def connect_to_obd():
    try:
        connection = obd.OBD()  # auto-detekcja portu
        if connection.is_connected():
            print("Połączono z adapterem ELM327!")
            print(f"Port: {connection.port_name()}")
            return connection
        else:
            print("Brak połączenia z adapterem. Sprawdź podłączenie.")
            return None
    except Exception as e:
        print(f"Błąd połączenia: {e}")
        return None

def read_dtc_codes(connection):
    if connection:
        print("\n=== Odczytywanie kodów błędów (DTC) ===")
        dtc_response = connection.query(obd.commands.GET_DTC)
        if not dtc_response.is_null():
            dtc_codes = dtc_response.value
            if dtc_codes:
                print("Znalezione kody błędów:")
                for code in dtc_codes:
                    print(f"- {code}")
            else:
                print("Brak zapisanych kodów błędów.")
        else:
            print("Nie udało się odczytać DTC.")

def read_freeze_frames(connection):
    if connection:
        print("\n=== Odczytywanie Freeze Frames ===")
        freeze_response = connection.query(obd.commands.GET_FREEZE_FRAME)
        if not freeze_response.is_null():
            freeze_data = freeze_response.value
            if freeze_data:
                print("Freeze Frame Data:")
                for key, value in freeze_data.items():
                    print(f"{key}: {value}")
            else:
                print("Brak danych Freeze Frame.")
        else:
            print("Nie udało się odczytać Freeze Frames.")

def clear_dtc_codes(connection):
    if connection:
        print("\n=== Kasowanie kodów błędów ===")
        clear_response = connection.query(obd.commands.CLEAR_DTC)
        if not clear_response.is_null():
            print("Kody błędów zostały skasowane!")
        else:
            print("Nie udało się skasować kodów błędów.")

def main():
    print("=== OBD-II Reader (ELM327) ===")
    connection = connect_to_obd()
    if connection:
        try:
            while True:
                print("\nWybierz opcję:")
                print("1. Odczytaj kody błędów (DTC)")
                print("2. Odczytaj Freeze Frames")
                print("3. Kasuj kody błędów")
                print("4. Wyjście")

                choice = input("Twój wybór (1-4): ").strip()

                if choice == "1":
                    read_dtc_codes(connection)
                elif choice == "2":
                    read_freeze_frames(connection)
                elif choice == "3":
                    clear_dtc_codes(connection)
                elif choice == "4":
                    print("Zamykanie programu...")
                    break
                else:
                    print("Nieprawidłowy wybór. Spróbuj ponownie.")
        except KeyboardInterrupt:
            print("\nProgram przerwany przez użytkownika.")
        finally:
            connection.close()
            print("Połączenie z adapterem zostało zamknięte.")

if __name__ == "__main__":
    main()
