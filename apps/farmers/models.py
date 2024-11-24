from django.db import models

FARMER_TYPES = [
    ("LL", "Landless Farmer"),
    ("MF", "Marginal Farmer"),
    ("SF", "Small Farmer"),
    ("BF", "Big Farmer"),
]


# Create your models here.
class Farmer(models.Model):
    lf = models.CharField(max_length=32)
    si = models.CharField(max_length=32)
    #
    name = models.CharField(max_length=255, blank=True, null=True)
    relative = models.CharField(max_length=255, blank=True, null=True)
    date_of_birth = models.DateField(blank=True)
    # ward
    village = models.CharField(max_length=255, blank=True, null=True)
    panchayat = models.CharField(max_length=255, blank=True, null=True)
    block = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    pin_code = models.CharField(max_length=6, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    #
    aadhar = models.CharField(max_length=12, blank=True, null=True)
    mobile = models.CharField(max_length=10, blank=True, null=True)
    #
    site = models.CharField(max_length=255, blank=True, null=True)
    thana = models.CharField(max_length=255, blank=True, null=True)
    khata = models.CharField(max_length=255, blank=True, null=True)
    khesra = models.CharField(max_length=255, blank=True, null=True)
    area = models.FloatField(default=0)
    farmer_type = models.CharField(choices=FARMER_TYPES, max_length=2)
    #
    certificate = models.ImageField(upload_to="certificates/", blank=True, null=True)
    signature = models.ImageField(upload_to="signatures/", blank=True, null=True)
    #
    lno = models.CharField(max_length=32, blank=True, null=True)
    grno = models.CharField(max_length=32, blank=True, null=True)
    #
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_address(self):
        return f"{self.ward}, {self.village}, {self.panchayat}, {self.block}, {self.district}, {self.pin_code}, {self.state}"

    def get_type(self):
        return FARMER_TYPES[self.farmer_type][1]
