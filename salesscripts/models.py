from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Salesscript(models.Model):
    scripttitle = models.TextField(null=True)
    salutationone = models.TextField(null=True)
    greetingsone = models.TextField(null=True)
    usernameone = models.TextField(null=True)
    companynameone = models.TextField(null=True)
    problemstatementone = models.TextField(null=True)
    backstorytwo = models.TextField(null=True)
    productnamethree = models.TextField(null=True)
    qualifierquestionsthree = models.TextField(null=True)
    productpresentationfour = models.TextField(null=True)
    rapportquestionfive = models.TextField(null=True)
    customerdoubtssix = models.TextField(null = True)
    answertocustomersix = models.TextField(null = True)
    productnameseven = models.TextField(null = True)
    painpointseven = models.TextField(null = True)
    productidealstateeight = models.TextField(null = True)
    problemstatementnine = models.TextField(null = True)
    productdescriptionelevan = models.TextField(null = True)
    productnametwelve = models.TextField(null = True)
    whatdoesitdotwelve = models.TextField(null = True)
    pricetwelve = models.TextField(null = True)
    member = models.ForeignKey(User, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.scripttitle
