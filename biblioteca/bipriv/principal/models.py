from django.db import models


class Autores(models.Model):
    nome_do_autor = models.CharField(max_length=40)

    def __str__(self):
        return self.nome_do_autor

    class Meta:
        db_table = 'autores'
        verbose_name_plural = 'Autores'


class Autoria(models.Model):
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING)
    id_autor = models.ForeignKey(Autores, models.DO_NOTHING)

    def __str__(self):
        return f'{self.id_livro} - {self.id_autor}'

    class Meta:
        db_table = 'autoria'
        verbose_name_plural = 'Autorias'
        unique_together = (('id_livro', 'id_autor'),)


class Contas(models.Model):
    nome = models.CharField(max_length=30)
    cargo = models.CharField(max_length=15)
    nif = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'contas'
        verbose_name_plural = 'Contas'


class Emprestimos(models.Model):
    data_req = models.DateField()
    data_ent = models.DateField()
    id_conta = models.ForeignKey(Contas, models.DO_NOTHING)
    n_registo = models.ForeignKey('Exemplar', models.DO_NOTHING)

    def __str__(self):
        return f'O {self.id_conta} Requesitou {self.n_registo} a ({self.data_req}) com a entrega a ({self.data_ent})'

    class Meta:
        db_table = 'emprestimos'
        verbose_name_plural = 'Emprestimos'


class Exemplar(models.Model):
    disponivel = models.BooleanField()
    id_exemplar = models.IntegerField(unique=True)
    id_livro = models.ForeignKey('Livros', models.DO_NOTHING)

    def __str__(self):
        return f'{self.id_livro} - Exemplar {self.id_exemplar}'

    class Meta:
        db_table = 'exemplar'
        verbose_name_plural = 'Exemplares'


class Livros(models.Model):
    isbn = models.CharField(max_length=20)
    editora = models.CharField(max_length=30)
    ano = models.IntegerField()
    idioma = models.CharField(max_length=20)
    titulo_do_livro = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo_do_livro

    class Meta:
        db_table = 'livros'
        verbose_name_plural = 'Livros'




class Local(models.Model):
    coluna = models.CharField(max_length=4)
    prateleira = models.CharField(max_length=4)
    estante = models.CharField(max_length=4)
    n_registo = models.ForeignKey(Exemplar, models.DO_NOTHING)

    def __str__(self):
        return self.n_registo

    class Meta:
        db_table = 'local'
        verbose_name_plural = 'Locais'
