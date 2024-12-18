import os
import csv

directory = 'images/'
if os.path.exists(directory):
    print(f"Directory {directory} ada.")
else:
    print(f"Directory {directory} tidak ditemukan.")

csv_file = 'data_csv/example.csv'
if os.path.exists(csv_file):
    print(f"File {csv_file} ada.")
else:
    print(f"File {csv_file} tidak ditemukan.")

new_names = []
with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        new_names.append(row[0].strip())

# Get a sorted list of .png, .jpg, and .jpeg files
file_list = os.listdir(directory)
image_files = sorted(
    [f for f in file_list if f.endswith('.png') or f.endswith('.jpg') or f.endswith('.jpeg')],
    key=lambda x:
        int(os.path.splitext(x)[0]) if x.split('.')[0].isdigit() else float('inf')
)

print(len(new_names))
print(len(image_files))

if len(new_names) != len(image_files):
    print("Jumlah nama dalam CSV tidak sama dengan jumlah file PNG!")
    exit()

for i in range(len(image_files)):
    old_name = os.path.join(directory, image_files[i])
    new_name = os.path.join(directory, new_names[i] + '.png')
    os.rename(old_name, new_name)
    print(f"File {image_files[i]} direname menjadi {new_names[i]}.png")

print("Proses renaming selesai.")
