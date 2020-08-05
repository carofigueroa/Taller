from django.db import models

# Create your models here.

class prevision(models.Model):
    prevision=models.CharField(max_length=50)

    def __str__(self):
        return self.prevision
    
    class Meta:
        verbose_name_plural="Previsiones"

class paciente(models.Model):
    rut=models.IntegerField()
    fecha_hospitalizacion=models.DateField(auto_now=True)
    edad=models.IntegerField()
    prevision=models.ForeignKey(prevision,on_delete=models.CASCADE,null=True,blank=True)
    nombre=models.CharField(max_length=20)
    apellido=models.CharField(max_length=30)
    embarazada=models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" %(self.nombre,self.apellido)


class profesional(models.Model):
    rut=models.IntegerField()
    nombre_completo=models.CharField(max_length=60)
    profesion=models.CharField(max_length=50)

    def __str__(self):
        if self.profesion=="Ginecólogo" or self.profesion=="Ginecóloga": 
            return self.nombre_completo

        else:
            return ""
    class Meta:
        verbose_name_plural = "Profesionales"
    

class medicamentos(models.Model):
    nombre=models.CharField(max_length=60)
    dosis=models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    
    class Meta:
        verbose_name_plural = "Medicamentos"
    
    

class tipo_reposo(models.Model):
    nombre=models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Reposos"
    

class cirugias(models.Model):
    nombre_cirugia=models.CharField(max_length=40)
    def __str__(self):
        return self.nombre_cirugia

    
    class Meta:
        verbose_name_plural = "Cirugias"
    

class regimen(models.Model):
    tipo_regimen=models.CharField(max_length=20)

    def __str__(self):
        return self.tipo_regimen

    
    class Meta:
        verbose_name_plural = "Regimenes"

class cadacuanto(models.Model):
    regular=models.CharField(max_length=10)
    def __str__(self):
        return self.regular

    class Meta:
        verbose_name_plural = "Regularidad"


class controles(models.Model):
    tipo_control=models.CharField(max_length=50)
    regularidad=models.ForeignKey(cadacuanto, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s cada %s horas" % (self.tipo_control, self.regularidad)
    
    class Meta:
        verbose_name_plural = "Controles"

class examene(models.Model):
    nombre_examen=models.CharField(max_length=50)
    tipo_examen=models.CharField(max_length=20)
    especificaciones=models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre_examen} del tipo {self.tipo_examen} especificaciones {self.especificaciones}"

class recien_nacido(models.Model):
    nombre_recien_nacido=models.CharField(max_length=50)
    madre=models.ForeignKey(paciente,blank=True,null=True, on_delete=models.deletion.CASCADE)
    num_ficha=models.IntegerField()
    rut=models.IntegerField()
    prevision=models.ForeignKey(prevision,blank=True,null=True, on_delete=models.deletion.CASCADE)
    fecha_nacimiento=models.DateField()
    class Meta:
        verbose_name_plural = "Recien Nacidos"

class hoja_indicaciones(models.Model):
    fecha=models.DateField(auto_now=True)
    nombre_profesional=models.ForeignKey(profesional, blank=True, null=True, on_delete=models.deletion.CASCADE)
    nombre_paciente=models.ForeignKey(paciente, blank=True, null=True, on_delete=models.deletion.CASCADE)
    reposo=models.ForeignKey(tipo_reposo, blank=True, null=True, on_delete=models.deletion.CASCADE)
    tipo_regimen=models.ForeignKey(regimen, blank=True, null=True, on_delete=models.deletion.CASCADE)
    nombre_medicamento=models.ManyToManyField(medicamentos, blank=True)
    #preparacion_operacion=models.BooleanField(default=False)
    Nombre_cirugias=models.ForeignKey(cirugias, blank=True, null=True, on_delete=models.deletion.CASCADE)
    control=models.ForeignKey(controles,default=None, blank=True, null=True, on_delete=models.deletion.CASCADE)
    examen=models.BooleanField(default=False)
    #hora_examen=models.TimeField(blank=True,null=True)
    alta=models.BooleanField(default=False)


