import os
import sys
from PIL import Image
from shutil import copyfile
from tqdm import tqdm


FILE_NAME = "file.jpg"
THUMB_NAME = "-thumb.jpg"
COLLECTION_DIR = "collection"
TARGET_DIR = "thumb"
THUMB_SIZE = [256, 144]
MAX_LENGTH_NAME = 5

if len(sys.argv) >= 3:
    param = dict(zip(*[iter(sys.argv[1:])]*2))
else:
    param = {}

collection_path = param.get("-c") or COLLECTION_DIR
target_path = param.get("-t") or TARGET_DIR
size = param.get("-s") or THUMB_SIZE

if not isinstance(size, tuple):
    size = [int(x) for x in size.split("x")]


def make_dir_name(name, length=MAX_LENGTH_NAME):
    count = len(str(name))
    temp_list = [x for x in range(1, length + 1)]
    temp_list.reverse()
    if length > count:
        return "{}{}".format("0" * temp_list[count], name)
    else:
        return "{}".format(name)


def create_thumb(item_name, thumb=THUMB_NAME, size=size):
    filename = os.path.splitext(item_name)[0]
    im = Image.open(item_name)
    im.thumbnail(size)
    im.save(filename + thumb, "JPEG")


if __name__ == "__main__":

    if not os.path.exists(collection_path):
        os.mkdir(collection_path, mode=0o777)

    # probably need remove
    if not os.path.exists(target_path):
        os.mkdir(target_path, mode=0o777)

    count = 0
    items_list = (
                    os.path.join(target_path, item)
                    for item in os.listdir(target_path)
                    if ".jpg" in item
                )

    for n, item in tqdm(enumerate(items_list, start=1)):
        while os.path.exists(
            os.path.join(collection_path, make_dir_name(count))
        ):
            count += 1

        temp_dir = os.path.join(collection_path, make_dir_name(count))
        temp_item = os.path.join(temp_dir, FILE_NAME)
        os.mkdir(temp_dir, mode=0o777)
        copyfile(item, temp_item)
        create_thumb(temp_item, thumb=THUMB_NAME, size=size)

    print("Done! {} dirs were created in '{}'!".format(n, collection_path))
