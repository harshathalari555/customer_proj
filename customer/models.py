from django.db import models

# Create your models here.

Customer_Type= (
    ('Bussiness', 'Bussiness'),
    ('Individual', 'Individual'),
)
salutation_choices = (
        ('Mr', "Mr"),
        ('Mrs', "Mrs"),
    )

supply_places = (
        ('Banglore', "Banglore"),
        ('Hyderbad', "Hyderbad"),
    )

tax_preference= [
    ('Taxable', 'Taxable'),
    ('Tax Exempt', 'Tax Exempt'),
    ]

payment_terms = (
        ('Due on Receipt', "Due on Receipt"),
        ('No Due on Receipt', "No Due on Receipt"),
    )

countrys = (
        ('India', "India"),
        ('USA', "USA"),
    )


class Customer(models.Model):
    customer_type = models.CharField(max_length=50, choices=Customer_Type)
    salutation = models.CharField(max_length=50, choices=salutation_choices)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    company_name = models.CharField(max_length=50, blank=True, null=True)
    company_display_name = models.CharField(max_length=50, blank=True, null=True)
    customer_email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    work_phone = models.CharField(max_length=12)
    mobile = models.CharField(max_length=12)
    website = models.CharField(max_length=50, blank=True, null=True)
    gst_treatment = models.CharField(max_length=50, blank=True, null=True)
    place_of_supply = models.CharField(max_length=50, choices=supply_places)
    currency = models.CharField(max_length=50, blank=True, null=True)
    payment_terms = models.CharField(max_length=50, choices=payment_terms)
    facebook = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    receivables = models.IntegerField(blank=True, null=True)
    attention = models.CharField(max_length=50, blank=True, null=True)
    country = models.CharField(max_length=50, choices=countrys)
    adress = models.TextField()
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

