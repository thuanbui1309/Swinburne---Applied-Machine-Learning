# The intial data is not in correct structure for model training:

#       image’s name{space}class label

# We need to transform it to the correct format for model training:

#       Data/train/{class}/{image_name}
#       Data/test/{class}/{image_name}

# Please note that the processed data is already included in the submission
# Only run it again if you have installed all data folder and annotation files
# in folder "inital_data". 

import os
import shutil

# Paths
INIT_DATA_TRAIN_PATH = "initial_data/Train"
INIT_ANNOTATION_TRAIN_TRAIN = "initial_data/train.txt"
INIT_DATA_TEST_PATH = "initial_data/Test"
INIT_ANNOTATION_TEST_TRAIN = "initial_data/test.txt"

DATA_PATH = "data"
DATA_TRAIN_PATH = f"{DATA_PATH}/train"
DATA_TEST_PATH = f"{DATA_PATH}/test"

def main():
    # Process the train data:
    with open(INIT_ANNOTATION_TRAIN_TRAIN, "r") as file:
        for line in file:
            line = line.split()
            image_name = line[0]
            class_label = line[1]

            image_link = f"{INIT_DATA_TRAIN_PATH}/{image_name}"
            train_class_folder = f"{DATA_TRAIN_PATH}/{class_label}"

            os.makedirs(train_class_folder, exist_ok=True)
            shutil.copyfile(image_link, f"{train_class_folder}/{image_name}")

    # Process the test data:
    with open(INIT_ANNOTATION_TEST_TRAIN, "r") as file:
        for line in file:
            line = line.split()
            image_name = line[0]
            class_label = line[1]

            image_link = f"{INIT_DATA_TEST_PATH}/{image_name}"
            test_class_folder = f"{DATA_TEST_PATH}/{class_label}"

            os.makedirs(test_class_folder, exist_ok=True)
            shutil.copyfile(image_link, f"{test_class_folder}/{image_name}")

    # Move annotation files
    shutil.copyfile(INIT_ANNOTATION_TRAIN_TRAIN, f"{DATA_PATH}/train.txt")
    shutil.copyfile(INIT_ANNOTATION_TEST_TRAIN, f"{DATA_PATH}/test.txt")

if __name__ == "__main__":
    main()