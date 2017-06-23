# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Alumno(models.Model):
	ApellidoPaterno = models.CharField (max_length=35)
	ApellidoMaterno = models.CharField (max_length=35)
	Nombres = models.CharField (max_length=35)
	DNI= models.CharField (max_length=8)
	FechaNacimiento = models.DateField()
	SEXOS= (('F','Femenino'), ('M','Masculino'))
	Sexo=models.CharField(max_length=1,choices=SEXOS, default='M')

	def NombreCompleto (self):
		cadena = "{0} {1}. {2}"
		return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno, Self.Nombres)

		def _Str_ (self):
			return self.NombresCompleto()

class loggin(models.Model):
	Usuario = models.CharField (max_length=35)
	pass1 = models.CharField (max_length=35)
	

	def logginCompleto (self):
		cadena = "{0} {1}. {2}"
		return cadena.format(self.Usuario,self.pass1)

		def _Str_ (self):
			return self.logginCompleto()


