""" Site photos photospecs """

#from imagekit.specs import ImageSpec
#from imagekit import processors
import ImageEnhance
from PIL import ImageOps
from imagekit.models import ImageSpecField
from imagekit import processors

class Sepia(object):
    """
        Turn image sepia
    """
    def process(self, img):

        def make_linear_ramp(white):
            # putpalette expects [r,g,b,r,g,b,...]
            ramp = []
            r, g, b = white
            for i in range(255):
                ramp.extend((r * i / 255, g * i / 255, b * i / 255))
            return ramp

        img = img.convert('RGB')
        #sepia = make_linear_ramp((224, 187, 153))
        sepia = make_linear_ramp((239, 191, 147))
        if img.mode != "L":
            img = img.convert("L")
        img = ImageOps.autocontrast(img)
        img.putpalette(sepia)
        img = img.convert('RGB')
        return img

class ImageJpeg(ImageSpecField):
    def __init__(self):
        super(ImageJpeg, self).__init__(
            image_field='image',
            options={'quality': 90, 'optimize':True},
            format='JPEG'
        )

class ImageFit128x128(ImageSpecField):
    def __init__(self):
        super(ImageFit128x128, self).__init__(
            processors=[processors.ResizeToFit(width=128,height=128)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image343x260(ImageSpecField):
    def __init__(self):
        super(Image343x260, self).__init__(
            processors=[processors.SmartResize(width=343, height=260)],
            image_field='image',
            options={'quality': 90, 'optimize':True},
            format='JPEG'
        )
        
class Image24x24(ImageSpecField):
    def __init__(self):
        super(Image24x24, self).__init__(
            processors=[processors.ResizeToFill(width=24,height=24,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image25x25(ImageSpecField):
    def __init__(self):
        super(Image25x25, self).__init__(
            processors=[processors.ResizeToFill(width=25,height=25,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image26x26(ImageSpecField):
    def __init__(self):
        super(Image26x26, self).__init__(
            processors=[processors.ResizeToFill(width=26,height=26,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )
    
class Image32x32(ImageSpecField):
    def __init__(self):
        super(Image32x32, self).__init__(
            processors=[processors.ResizeToFill(width=32,height=32,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Sepia32x32(ImageSpecField):
    def __init__(self):
        super(Sepia32x32, self).__init__(
            processors=[processors.ResizeToFill(width=32,height=32,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1), Sepia()],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )
    
class Image40x40(ImageSpecField):
    def __init__(self):
        super(Image40x40, self).__init__(
            processors=[processors.ResizeToFill(width=40,height=40,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image50x50(ImageSpecField):
    def __init__(self):
        super(Image50x50, self).__init__(
            processors=[processors.ResizeToFill(width=50,height=50,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Sepia50x50(ImageSpecField):
    def __init__(self):
        super(Sepia50x50, self).__init__(
            processors=[processors.ResizeToFill(width=50,height=50,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1), Sepia()],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image55x55(ImageSpecField):
    def __init__(self):
        super(Image55x55, self).__init__(
            processors=[processors.SmartResize(width=55,height=55)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image60x37(ImageSpecField):
    def __init__(self):
        super(Image60x37, self).__init__(
            processors=[processors.ResizeToFill(width=60,height=37,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image60x105(ImageSpecField):
    def __init__(self):
        super(Image60x105, self).__init__(
            processors=[processors.ResizeToFill(width=60,height=105,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image64x64(ImageSpecField):
    def __init__(self):
        super(Image64x64, self).__init__(
            processors=[processors.ResizeToFill(width=64,height=64,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image77x77(ImageSpecField):
    def __init__(self):
        super(Image77x77, self).__init__(
            processors=[processors.ResizeToFill(width=77,height=77,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image98x98(ImageSpecField):
    def __init__(self):
        super(Image98x98, self).__init__(
            processors=[processors.SmartResize(width=98,height=98)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image105x105(ImageSpecField):
    def __init__(self):
        super(Image105x105, self).__init__(
            processors=[processors.ResizeToFill(width=105,height=105,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image120x177(ImageSpecField):
    def __init__(self):
        super(Image120x177, self).__init__(
            processors=[processors.ResizeToFill(width=120,height=177,anchor=processors.Anchor.CENTER), processors.Adjust(contrast=1.2, sharpness=1.1)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image128x128(ImageSpecField):
    def __init__(self):
        super(Image128x128, self).__init__(
            processors=[processors.ResizeToFill(width=128,height=128,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image134x134(ImageSpecField):
    def __init__(self):
        super(Image134x134, self).__init__(
            processors=[processors.ResizeToFill(width=134,height=134,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image146x146(ImageSpecField):
    def __init__(self):
        super(Image146x146, self).__init__(
            processors=[processors.ResizeToFill(width=146,height=146,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image147x113(ImageSpecField):
    def __init__(self):
        super(Image147x113, self).__init__(
            processors=[processors.ResizeToFill(width=147,height=113,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )
        
class Image150x150(ImageSpecField):
    def __init__(self):
        super(Image150x150, self).__init__(
            processors=[processors.ResizeToFill(width=150,height=150,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image153x153(ImageSpecField):
    def __init__(self):
        super(Image153x153, self).__init__(
            processors=[processors.ResizeToFill(width=153,height=153,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )
        
class Image160x160(ImageSpecField):
    def __init__(self):
        super(Image160x160, self).__init__(
            processors=[processors.SmartResize(width=160,height=160)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image186x119(ImageSpecField):
    def __init__(self):
        super(Image186x119, self).__init__(
            processors=[processors.ResizeToFill(width=186,height=119,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image235x250(ImageSpecField):
    def __init__(self):
        super(Image235x250, self).__init__(
            processors=[processors.ResizeToFill(width=235,height=250,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image256x256(ImageSpecField):
    def __init__(self):
        super(Image256x256, self).__init__(
            processors=[processors.ResizeToFill(width=256,height=256,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image307x307(ImageSpecField):
    def __init__(self):
        super(Image307x307, self).__init__(
            processors=[processors.ResizeToFill(width=307,height=307,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )
        
class Image405x405(ImageSpecField):
    def __init__(self):
        super(Image405x405, self).__init__(
            processors=[processors.ResizeToFill(width=405,height=405,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )

class Image450x450(ImageSpecField):
    def __init__(self):
        super(Image450x450, self).__init__(
            processors=[processors.ResizeToFill(width=450,height=450,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 90, 'optimize':True},
            format='JPEG'
        )

class Image512x512(ImageSpecField):
    def __init__(self):
        super(Image512x512, self).__init__(
            processors=[processors.ResizeToFill(width=512,height=512,anchor=processors.Anchor.CENTER)],
            image_field='image',
            options={'quality': 90, 'optimize':True},
            format='JPEG'
        )

class Image480xAny(ImageSpecField):
    def __init__(self):
        super(Image480xAny, self).__init__(
            processors=[processors.ResizeToFit(width=480)],
            image_field='image',
            options={'quality': 95, 'optimize':True},
            format='JPEG'
        )  