import uuid
import time
import re
import os
from django.conf import settings
from django.core.files import File

def get_file_path():
    path = settings.DOWNLOAD_DIRECTORY + str(uuid.uuid4())
    return path


def get_file_name(name, ext):
    replace_str = 'abcdef'
    for char in replace_str:
        name = name.replace(char, '')
    file_name = '%s_%s.%s' %(name, int(time.time()), ext)
    return file_name


def base64_to_photo_obj(creator, base64_str):
    from photos.models import Photo
    
    base64_str = re.sub('\s', '', base64_str)
    base64_pattern = re.compile('data:image/(%s);base64,(.*)$' % '|'.join(settings.PHOTOS_FORMATS))
    match_groups = base64_pattern.match(base64_str)
    format = match_groups.group(1)
    photo_64 = match_groups.group(2)

    tmp_file_name = "/tmp/%s.%s" % (uuid.uuid4(), 'png')
    fh = open(tmp_file_name, "wb")
    fh.write(photo_64.decode('base64'))
    fh.close()

    fh = open(tmp_file_name, "rb")
    photo = Photo(user=creator, title='', description='')
    photo.image.save("%s.%s" % (uuid.uuid4(), 'png'), File(fh))
    fh.close()
    photo.save()
    os.remove(tmp_file_name)

    return photo, format
