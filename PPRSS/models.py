from django.db import models
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    remember_me = models.BooleanField(default=False)

    def __str__(self):
        return self.name




class Features(models.Model):
    ImageDirectoryEntrySecurity = models.FloatField(default=0.0)
    CheckSum = models.FloatField(default=0.0)
    SizeOfInitializedData = models.FloatField(default=0.0)
    SizeOfImage = models.FloatField(default=0.0)
    MajorLinkerVersion = models.FloatField(default=0.0)
    AddressOfEntryPoint = models.FloatField(default=0.0)
    SectionMinEntropy = models.FloatField(default=0.0)
    DirectoryEntryImportSize = models.FloatField(default=0.0)
    SectionMaxPhysical = models.FloatField(default=0.0)
    SectionMinVirtualSize = models.FloatField(default=0.0)
    SectionMaxPointerData = models.FloatField(default=0.0)
    e_lfanew = models.FloatField(default=0.0)
    DllCharacteristics = models.FloatField(default=0.0)
    DirectoryEntryImport = models.FloatField(default=0.0)
    ImageDirectoryEntryResource = models.FloatField(default=0.0)
    ImageDirectoryEntryImport = models.FloatField(default=0.0)
    DirectoryEntryExport = models.FloatField(default=0.0)
    SizeOfCode = models.FloatField(default=0.0)
    ImageBase = models.FloatField(default=0.0)
    SizeOfStackReserve = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"PEFileInfo: {self.id}"

# class FileUpload(models.Model):

#     doc_file=models.FileField()
#     def _str_(self):
#         return f"{self.id}"



class FileUpload(models.Model):
    file = models.FileField(upload_to='static/pefiles/',default='PPRSS/wmpnssui.dll.mui')
    uploaded_at = models.DateTimeField(default=timezone.now)


class Log(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)