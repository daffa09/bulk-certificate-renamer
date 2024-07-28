import os
import csv

directory = 'images/'
if os.path.exists(directory):
    print(f"Directory {directory} ada.")
else:
    print(f"Directory {directory} tidak ditemukan.")

csv_file = 'ide_inovasi.csv'
if os.path.exists(csv_file):
    print(f"File {csv_file} ada.")
else:
    print(f"File {csv_file} tidak ditemukan.")

new_names = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        new_names.append(row[0].strip())

png_files = sorted([f for f in os.listdir(directory) if f.endswith('.png')], key=lambda x: int(os.path.splitext(x)[0]))

if len(new_names) != len(png_files):
    print("Jumlah nama dalam CSV tidak sama dengan jumlah file PNG!")
    exit()

for i in range(len(png_files)):
    old_name = os.path.join(directory, png_files[i])
    new_name = os.path.join(directory, new_names[i] + '.png')
    os.rename(old_name, new_name)
    print(f"File {png_files[i]} direname menjadi {new_names[i]}.png")

print("Proses renaming selesai.")
