import argparse
import random
import os
from PIL import Image
from tqdm import tqdm


SIZE = 64

parser = argparse.ArgumentParser()
parser.add_argument('--data_dir',  help="Directory with the SIGNS dataset")
parser.add_argument('--output_dir', help="Where to write the new data")


def save(filename, output_dir, size=SIZE):
    """ select the image contained in `filename` and save it to the `output_dir`"""
    image = Image.open(filename)
    image.save(os.path.join(output_dir, filename.split('/')[-1]))


if __name__ == '__main__':
    args = parser.parse_args()

    assert os.path.isdir(args.data_dir), "Couldn't find the dataset at {}".format(args.data_dir)

    # Define the data directories
    train_data_dir = os.path.join(args.data_dir, 'train_data')

    # Get the filenames in each directory (train and test)
    filenames = os.listdir(train_data_dir)
    filenames = [os.path.join(train_data_dir, f) for f in filenames if f.endswith('.jpg')]


    # Split the images in 'train_data' into 80% train and 10% val and 10% test
    random.seed(230)
    filenames.sort()
    random.shuffle(filenames)

    split_1 = int(0.8 * len(filenames))
    split_2 = int(0.9 * len(filenames)) 
    train_filenames = filenames[:split_1] 
    dev_filenames = filenames[split_1:split_2] 
    test_filenames = filenames[split_2:]

    print(len(train_filenames))
    print(len(dev_filenames))
    print(len(test_filenames))


    filenames = {'train': train_filenames,
                 'dev': dev_filenames,
                 'test': test_filenames}

    if not os.path.exists(args.output_dir):
        os.mkdir(args.output_dir)
    else:
        print("Warning: output dir {} already exists".format(args.output_dir))

    # Preprocess train, dev and test
    for split in ['train', 'dev', 'test']:
        output_dir_split = os.path.join(args.output_dir, '{}_dataset'.format(split))
        if not os.path.exists(output_dir_split):
            os.mkdir(output_dir_split)
        else:
            print("Warning: dir {} already exists".format(output_dir_split))

        print("Processing {} data, saving preprocessed data to {}".format(split, output_dir_split))
        for filename in tqdm(filenames[split]):
            save(filename, output_dir_split, size=SIZE)

    print("Done building dataset")