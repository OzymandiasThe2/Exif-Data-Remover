from PIL import Image
from PIL.ExifTags import TAGS

# See current exif data
filename = "test-image.jpg"
image = Image.open(filename)
# for tag, value in image._getexif().items():
#     print(TAGS.get(tag), value)

# Strip
image_info = list(image.getdata())
stripped_image = Image.new(image.mode, image.size)
stripped_image.putdata(image_info)

clean_filename = f"clean_{filename}"
stripped_image.save(clean_filename)

# Check if stripped
tag_list = []
try:  # if this works ,that mean there is still exif data meaning stripping FAILED
    image_cleaned = Image.open(clean_filename)
    for tag in image_cleaned._getexif():
        tag_list.append(TAGS.get(tag))
    print(f"\nFailed to strip {filename}, the image contains the following tags: \n"
          f"{tag_list}")
except TypeError:  # if this raises then that means it couldn't find exif data which means stripping WORKED
    print(
        f"\nIn {clean_filename} could not find a tag within the file (this is a good thing), this means file has "
        f"been successfully stripped")
