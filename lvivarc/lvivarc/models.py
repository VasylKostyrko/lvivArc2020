from django.db import models

class ArcType(models.Model):
    """ Види архітектурних об'єктів """
    typeName = models.CharField(max_length=60)
    def __str__(self):
        return self.typeName

class ArcObj(models.Model):
    """ Архітектурні об'єкти """
    objName = models.CharField(max_length=100)
    objType = models.ForeignKey(ArcType, on_delete=models.CASCADE)
    descr = models.TextField()
    curAddress = models.CharField(max_length=100, blank=True)
    # imageName = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="", blank = True)
    def __str__(self):
        return self.objName
