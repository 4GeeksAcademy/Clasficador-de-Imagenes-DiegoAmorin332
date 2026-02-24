from utils import db_connect
engine = db_connect()

import os
import shutil
import random

original_dir = "train"

base_dir = "dataset"

train_dir = os.path.join(base_dir, "train")
val_dir = os.path.join(base_dir, "validation")

os.makedirs(os.path.join(train_dir, "cats"), exist_ok=True)
os.makedirs(os.path.join(train_dir, "dogs"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "cats"), exist_ok=True)
os.makedirs(os.path.join(val_dir, "dogs"), exist_ok=True)

files = os.listdir(original_dir)

cats = [f for f in files if f.startswith("cat")]
dogs = [f for f in files if f.startswith("dog")]

random.shuffle(cats)
random.shuffle(dogs)

split_ratio = 0.8

cats_train = cats[:int(len(cats) * split_ratio)]
cats_val = cats[int(len(cats) * split_ratio):]

dogs_train = dogs[:int(len(dogs) * split_ratio)]
dogs_val = dogs[int(len(dogs) * split_ratio):]

for f in cats_train:
    shutil.copy(os.path.join(original_dir, f),
                os.path.join(train_dir, "cats", f))

for f in cats_val:
    shutil.copy(os.path.join(original_dir, f),
                os.path.join(val_dir, "cats", f))

for f in dogs_train:
    shutil.copy(os.path.join(original_dir, f),
                os.path.join(train_dir, "dogs", f))

for f in dogs_val:
    shutil.copy(os.path.join(original_dir, f),
                os.path.join(val_dir, "dogs", f))

print("Dataset organizado correctamente.")
print(f"Gatos train: {len(cats_train)}")
print(f"Gatos validation: {len(cats_val)}")
print(f"Perros train: {len(dogs_train)}")
print(f"Perros validation: {len(dogs_val)}")