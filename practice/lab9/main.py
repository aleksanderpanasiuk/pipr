from file import FileInfo
import json
import csv


def write_json(file_handle, files_info):
    data = []

    for file in files_info:
        file_info = {
            "path": file.path,
            "name": file.name,
            "number_of_lines": file.number_of_lines
        }

        data.append(file_info)

    json.dump(data, file_handle, indent=4)


def read_json(file_handle):
    return json.load(file_handle)


def test_json():
    files_info = FileInfo("sad.txt"), FileInfo("das.txt")

    file_handle = open("test.json", 'w')
    write_json(file_handle, files_info)
    file_handle.close()

    file_handle = open("test.json", 'r')
    print(read_json(file_handle))
    file_handle.close()


def write_csv(file_handle, files_info):
    writer = csv.DictWriter(file_handle, ["path", "name", "number_of_lines"])
    writer.writeheader()

    for file in files_info:
        file_info = {
            "path": file.path,
            "name": file.name,
            "number_of_lines": file.number_of_lines
        }

        writer.writerow(file_info)


def read_csv(file_handle):
    data = []
    reader = csv.DictReader(file_handle)

    for row in reader:
        data.append(row)

    return data


def test_csv():
    files_info = FileInfo("sad.txt"), FileInfo("das.txt")

    file_handle = open("test.csv", 'w')
    write_csv(file_handle, files_info)
    file_handle.close()

    file_handle = open("test.csv", 'r')
    print(read_csv(file_handle))
    file_handle.close()


def main():
    test_json()
    test_csv()


if __name__ == "__main__":
    main()
