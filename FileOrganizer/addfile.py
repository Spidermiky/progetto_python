import os, shutil, sys, argparse, csv

# importo le funzioni principali del modulo argparse

parser = argparse.ArgumentParser(description="smista il file indicato (indicare il nome completo del file e l'estensione) nella cartella di riferimento, audio, docs o images")

parser.add_argument("filename", type = str, help="nome del file da spostare")

args = parser.parse_args()

#####

def addfile(filename):

    main_path = "../FileOrganizer/files"

    docs_dir = os.path.join(main_path, "docs")
    images_dir = os.path.join(main_path, "images")
    audio_dir = os.path.join(main_path, "audio")

    recap_csv = os.path.join(main_path, "recap.csv")

    type_mapping = {
        "txt": "doc",
        "odt": "doc",
        "mp3": "audio",
        "jpg": "image",
        "jpeg": "image",
        "png": "image"
    }

    file_path = os.path.join(main_path, filename)
    if not os.path.exists(file_path):
        print(f"file {filename} not found.")
        return

    file_name, file_extension = os.path.splitext(filename)
    file_extension = file_extension[1:].lower()

    if file_extension in type_mapping:
        if type_mapping[file_extension] == "doc":
            target_dir = docs_dir
        elif type_mapping[file_extension] == "image":
            target_dir = images_dir
        elif type_mapping[file_extension] == "audio":
            target_dir = audio_dir
    else:
        print(f"File type'.{file_extension}' is not supported")
        return

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    shutil.move(file_path, target_dir)

    target_path = os.path.join(target_dir, filename)
    file_size = os.path.getsize(target_path)

    file_csv_exists = os.path.exists(recap_csv)
    with open(recap_csv, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_csv_exists:
            header = "name, type, size(B)".split(", ")
            writer.writerow(header)
        writer.writerow([file_name, type_mapping[file_extension], file_size])

    print(f"{filename}, type:{type_mapping[file_extension]}, size:{file_size}")

addfile(args.filename)











