from django.db import models


class Autores(models.Model):
    nome_do_autor = models.CharField(max_length=40)


    class Meta:
        db_table = 'autores'


class Autoria(models.Model):
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING)
    id_autor = models.ForeignKey(Autores, models.DO_NOTHING)

    class Meta:
        db_table = 'autoria'
        unique_together = (('id_livro', 'id_autor'),)


class Contas(models.Model):
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=15)
    nif = models.IntegerField()

    class Meta:
        db_table = 'contas'


class Emprestimos(models.Model):
    data_req = models.DateField()
    data_ent = models.DateField()
    id_conta = models.ForeignKey(Contas, models.DO_NOTHING)
    n_registo = models.ForeignKey('Exemplar', models.DO_NOTHING)

    class Meta:
        db_table = 'emprestimos'


class Exemplar(models.Model):
    disponivel = models.BooleanField()
    id_exemplar = models.IntegerField(unique=True)
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING)

    class Meta:
        db_table = 'exemplar'


class Livros(models.Model):
    isbn = models.CharField(max_length=20)
    editora = models.CharField(max_length=30)
    ano = models.IntegerField()
    idioma = models.CharField(max_length=20)
    titulo_do_livro = models.CharField(max_length=20)

    class Meta:
        db_table = 'livros'


class Local(models.Model):
    coluna = models.CharField(max_length=4)
    prateleira = models.CharField(max_length=4)
    estante = models.CharField(max_length=4)
    n_registo = models.ForeignKey(Exemplar, models.DO_NOTHING)

    class Meta:
        db_table = 'local'
