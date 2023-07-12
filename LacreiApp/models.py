from django.db import models

class PessoaProfissional(models.Model):
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Consulta(models.Model):
    data = models.DateField()
    pessoa_profissional = models.ForeignKey(PessoaProfissional, on_delete=models.CASCADE)

    def __str__(self):
        return f"Consulta {self.id} - Profissional: {self.pessoa_profissional.nome}"
