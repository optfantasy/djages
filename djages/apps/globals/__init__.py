from djangotoolbox.fields import AbstractIterableField

def dummy(self, **kwargs):
	pass

AbstractIterableField.formfield = dummy
