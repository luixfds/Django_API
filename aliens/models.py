from django.db import models


def up_img_alien(instance, filename):
    return f"{instance.id}-{instance.nome}" #-{filename}" # filename salva o nome da foto apos o id e nome no banco


class Alien(models.Model):
    nome = models.CharField(max_length=20)
    especie = models.CharField(max_length=20)
    planetaN = models.CharField(max_length=30)
    altura = models.DecimalField(max_digits=10, decimal_places=2)
    peso = models.DecimalField(max_digits=10, decimal_places=2)

    baixo = '0%'
    baime = '25%'
    medio = '50%'
    medal = '75%'
    alto = '100%'

    setNivel = (
        (baixo, '0%'),
        (baime, '25%'),
        (medio, '50%'),
        (medal, '75%'),
        (alto, '100%'),
    )

    forca = models.CharField(max_length=20, choices=setNivel)
    inteligencia = models.CharField(max_length=20, choices=setNivel)
    agilidade = models.CharField(max_length=20, choices=setNivel)

    imagem = models.ImageField(upload_to=up_img_alien, blank=True)
