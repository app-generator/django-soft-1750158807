# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    entreprise = models.CharField(max_length=255, null=True, blank=True)
    contact = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Category(models.Model):

    #__Category_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Category_FIELDS__END

    class Meta:
        verbose_name        = _("Category")
        verbose_name_plural = _("Category")


class Produit(models.Model):

    #__Produit_FIELDS__
    code = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Produit_FIELDS__END

    class Meta:
        verbose_name        = _("Produit")
        verbose_name_plural = _("Produit")


class Entree(models.Model):

    #__Entree_FIELDS__
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    nombre = models.IntegerField(null=True, blank=True)
    observation = models.TextField(max_length=255, null=True, blank=True)

    #__Entree_FIELDS__END

    class Meta:
        verbose_name        = _("Entree")
        verbose_name_plural = _("Entree")


class Commande(models.Model):

    #__Commande_FIELDS__
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    nombre = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    statut = models.BooleanField()
    observation = models.TextField(max_length=255, null=True, blank=True)

    #__Commande_FIELDS__END

    class Meta:
        verbose_name        = _("Commande")
        verbose_name_plural = _("Commande")


class Vente(models.Model):

    #__Vente_FIELDS__
    reference = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    client = models.CharField(max_length=255, null=True, blank=True)

    #__Vente_FIELDS__END

    class Meta:
        verbose_name        = _("Vente")
        verbose_name_plural = _("Vente")


class Detailsvente(models.Model):

    #__Detailsvente_FIELDS__
    vente = models.ForeignKey(Vente, on_delete=models.CASCADE)
    article = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField(null=True, blank=True)
    pu = models.IntegerField(null=True, blank=True)
    pt = models.IntegerField(null=True, blank=True)
    observation = models.TextField(max_length=255, null=True, blank=True)

    #__Detailsvente_FIELDS__END

    class Meta:
        verbose_name        = _("Detailsvente")
        verbose_name_plural = _("Detailsvente")



#__MODELS__END
