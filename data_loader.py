caca

dataset_path = "../data"

base = 0
labels = []


def load_labels():
    return os.listdir(dataset_path)


max_train_data = 30000
max_test_data = 10000
max_val_data = 10000

sample_size_train = 1800
sample_size_val = 1200


def load_batch_data(start_point, whichData="train"):
    labels = load_labels()
    labels.sort()
    # print(labels)

    data_step = 0

    if "train" == whichData:
        dataset = np.ndarray(shape=(sample_size_train, 300, 300, 3),
                             dtype=np.float32)
        dataset_labels = np.zeros(sample_size_train, dtype=np.int32)
        data_step = 150
    elif "validation" == whichData:
        dataset = np.ndarray(shape=(sample_size_val, 300, 300, 3),
                             dtype=np.float32)
        dataset_labels = np.zeros(sample_size_val, dtype=np.int32)
        data_step = 100

    count = 0
    label_int = 0
    for label in labels:
        temp = os.listdir(dataset_path + "/" + label + "/" + whichData + "/patches/")
        # print(temp)

        for x in range(start_point, start_point + data_step):
            img = cv2.imread(dataset_path + "/" + label + "/" + whichData + "/patches/" + temp[x])
            # print(img)
            dataset[count] = img
            dataset_labels[count] = label_int
            count += 1
        label_int += 1

    return dataset, dataset_labels


"""train_data, label_data = load_batch_data(0, "validation")

print(train_data.shape)

print(label_data.shape)"""


# load_train_batch_data(0)
def rename_paths():
    full_path = os.listdir(dataset_path)

    for full in full_path:

        temp = os.listdir(dataset_path + "/" + full)
        print(temp)
        for pathy in temp:
            oldpath = dataset_path + "/" + full + "/" + pathy
            print(oldpath)

            if "_train" in pathy:
                newpath = dataset_path + "/" + full + "/train"
                os.rename(oldpath, newpath)
            elif "_test" in pathy:
                newpath = dataset_path + "/" + full + "/test"
                os.rename(oldpath, newpath)
            elif "_validation" in pathy:
                newpath = dataset_path + "/" + full + "/validation"
                os.rename(oldpath, newpath)

# rename_paths()
