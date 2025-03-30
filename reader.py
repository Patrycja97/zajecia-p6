import csv
import sys


def load_data(file_path):
    """
    Funkcja do wczytywania danych z pliku CSV
    """
    with open(file_path, "r") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


def pretty_print(data):
    """
    Funkcja do drukowania ładnej tabelki w konsoli
    """
    print("\n")
    max_lengths = []

    for col in range(len(data[0])):
        max_col_length = max(len(row[col]) for row in data)
        max_lengths.append(max_col_length)

    for row in data:
        text = ""
        for i, cell in enumerate(row):
            text += "\t" + str(cell).ljust(max_lengths[i])
        print(text)


def modify_data(data, row, col, new_value):
    """
    Zmiana wartości w tabeli
    """
    if validate_coordinates(data, row, col):
        data[row][col] = new_value
    return data


def validate_coordinates(data, row, col):
    """
    Sprawdzenie poprawności współrzędnych
    """
    if row < 0 or row >= len(data):
        print(f"Błąd: Niepoprawny wiersz {row}")
        return False
    if col < 0 or col >= len(data[0]):
        print(f"Błąd: Niepoprawna kolumna {col}")
        return False
    return True


def save_data(data, file_path):
    """
    Zapisanie danych do pliku CSV
    """
    with open(file_path, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def main():
    if len(sys.argv) < 3:
        print("Użycie: python reader.py <plik_wejsciowy> <plik_wyjsciowy> <zmiana_1> <zmiana_2> ...")
        print("Przykład: python reader.py in.csv out.csv 0,0,gitara 3,1,kubek")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    changes = sys.argv[3:]

    print("Wczytywanie danych z pliku:", input_file)
    data = load_data(input_file)

    print("Dane przed zmianą:")
    pretty_print(data)

    for change in changes:
        try:
            col, row, value = change.split(",", 2)
            col = int(col)
            row = int(row)
            data = modify_data(data, row=row, col=col, new_value=value)
        except ValueError:
            print(f" Błąd parsowania zmiany: {change}")

    print("\nDane po zmianie:")
    pretty_print(data)

    print("\nZapis do pliku:", output_file)
    save_data(data, output_file)


if __name__ == "__main__":
    main()