import os

# dictionary with translations
translate = {
    "cane": "dog", "cavallo": "horse", "elefante": "elephant", "farfalla": "butterfly",
    "gallina": "chicken", "gatto": "cat", "mucca": "cow", "pecora": "sheep", "scoiattolo": "squirrel",
    "dog": "cane", "horse": "cavallo", "elephant": "elefante", "butterfly": "farfalla",
    "chicken": "gallina", "cat": "gatto", "cow": "mucca", "spider": "ragno", "squirrel": "scoiattolo",
    "sheep": "pecora", "ragno": "spider"}


# set path to "raw-img" folder
base_path = "data/raw-img/"

# check if such path exists
if not os.path.exists(base_path):
    print(f'directory "{base_path}" doesnt exist')
    exit()

# loop through dirs in "raw-img"
for folder in os.listdir(base_path):
    old_path = os.path.join(base_path, folder)
    
    if not os.path.isdir(old_path):
        print(f'Skipped (not a folder): {folder}')
        continue

    if folder not in translate:
        print(f'Skipped (no translation): {folder}')
        continue

    new_name = translate[folder]
    new_path = os.path.join(base_path, new_name)

    if os.path.exists(new_path):
        print(f'Skipped (destination exists): {new_name}')
        continue

    os.rename(old_path, new_path)
    print(f'Renamed: {folder} -> {new_name}')

