# ============================================================================
class ImageLoader:
    """A mixin to add image loading features to any class.
    It seachs for images in a set of predefined paths,
    looking for files matching image names and types.
    It stores images internally: this allows for reuse. Also,
    it is needed to avoid the image object to be garbage
    collected before it is needed.
    """

    # exceptions
    ImageNotFound = 'File not found for image' # args: (imagename, imagetype)

    def __init__(self, *dirs):
        self.images={}
        self.dirs=[]
##        for d in dirs:
            

    def searchpath(self, dir):
        self.dirs.append( dir )

    def load(name, type ):
        for dir in self.dirs :
            fname = self._filename( dir, name, type )
            try :
                f = open(fname, 'r')
                f.close()
                img = Image( master=self, type = 'photo', file=fname ) #this requires self be a widget
                self.images['type']['name'] = img
            
                break # found the image
            except IOError:
                pass

        if not img:
            raise self.__class__.ImageNotFound, (name, type)
        else:
            return img
        











