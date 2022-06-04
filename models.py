# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class Cadastropedido(models.Model):
    idcadastropedido = models.AutoField(db_column='idcadastroPedido', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cadastroPedido'


class Classe(models.Model):
    idclasse = models.AutoField(db_column='idClasse', primary_key=True)  # Field name made lowercase.
    classe = models.CharField(db_column='Classe', max_length=45)  # Field name made lowercase.
    idfilo = models.ForeignKey('Filo', models.DO_NOTHING, db_column='idFilo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'classe'


class Distrito(models.Model):
    iddistrito = models.AutoField(db_column='idDistrito', primary_key=True)  # Field name made lowercase.
    distrito = models.CharField(db_column='Distrito', max_length=45)  # Field name made lowercase.
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idProvincia')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'distrito'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Especie(models.Model):
    idespecie = models.AutoField(db_column='idEspecie', primary_key=True)  # Field name made lowercase.
    especie = models.CharField(db_column='Especie', max_length=45, blank=True, null=True)  # Field name made lowercase.
    idgenero = models.ForeignKey('Genero', models.DO_NOTHING, db_column='idGenero', blank=True, null=True)  # Field name made lowercase.
    habitat = models.CharField(db_column='Habitat', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    coordenadas = models.CharField(db_column='Coordenadas', max_length=600, blank=True, null=True)  # Field name made lowercase.
    notas = models.CharField(db_column='Notas', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    detalhes = models.CharField(max_length=1000, blank=True, null=True)
    nomecomum = models.CharField(db_column='NomeComum', max_length=45, blank=True, null=True)  # Field name made lowercase.
    codigo = models.CharField(db_column='Codigo', max_length=10000, blank=True, null=True)  # Field name made lowercase.
    validacao = models.CharField(db_column='Validacao', max_length=45)  # Field name made lowercase.
    datacriacao = models.DateField(db_column='DataCriacao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especie'


class Especieimagem(models.Model):
    idimagem = models.AutoField(db_column='idImagem', primary_key=True)  # Field name made lowercase.
    imagem = models.CharField(max_length=1000, blank=True, null=True)
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especieImagem'


class Especiesom(models.Model):
    idsom = models.AutoField(db_column='idSom', primary_key=True)  # Field name made lowercase.
    som = models.CharField(max_length=1000, blank=True, null=True)
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especieSom'


class Especievideo(models.Model):
    idvideo = models.AutoField(db_column='idVideo', primary_key=True)  # Field name made lowercase.
    video = models.CharField(max_length=1000, blank=True, null=True)
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especieVideo'


class Especieincompleta(models.Model):
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie', primary_key=True)  # Field name made lowercase.
    idfamilia = models.ForeignKey('Familia', models.DO_NOTHING, db_column='idFamilia', blank=True, null=True)  # Field name made lowercase.
    idordem = models.ForeignKey('Ordem', models.DO_NOTHING, db_column='idOrdem', blank=True, null=True)  # Field name made lowercase.
    idclasse = models.ForeignKey(Classe, models.DO_NOTHING, db_column='idClasse', blank=True, null=True)  # Field name made lowercase.
    idfilo = models.ForeignKey('Filo', models.DO_NOTHING, db_column='idFilo', blank=True, null=True)  # Field name made lowercase.
    idreino = models.ForeignKey('Reino', models.DO_NOTHING, db_column='idReino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'especieincompleta'


class Familia(models.Model):
    idfamilia = models.AutoField(db_column='idFamilia', primary_key=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=45)  # Field name made lowercase.
    idordem = models.ForeignKey('Ordem', models.DO_NOTHING, db_column='idOrdem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'familia'


class Filo(models.Model):
    idfilo = models.AutoField(db_column='idFilo', primary_key=True)  # Field name made lowercase.
    filo = models.CharField(db_column='Filo', max_length=45)  # Field name made lowercase.
    idreino = models.ForeignKey('Reino', models.DO_NOTHING, db_column='idReino', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filo'


class Genero(models.Model):
    idgenero = models.AutoField(db_column='idGenero', primary_key=True)  # Field name made lowercase.
    genero = models.CharField(db_column='Genero', max_length=45)  # Field name made lowercase.
    idfamilia = models.ForeignKey(Familia, models.DO_NOTHING, db_column='idFamilia', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'genero'


class Localizacaoespecie(models.Model):
    idlocalizacao = models.AutoField(db_column='idLocalizacao', primary_key=True)  # Field name made lowercase.
    iddistrito = models.ForeignKey(Distrito, models.DO_NOTHING, db_column='idDistrito')  # Field name made lowercase.
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localizacaoespecie'
        unique_together = (('idlocalizacao', 'iddistrito', 'idespecie'),)


class Localizacaoincompleta(models.Model):
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie', blank=True, null=True)  # Field name made lowercase.
    idprovincia = models.ForeignKey('Provincia', models.DO_NOTHING, db_column='idProvincia', blank=True, null=True)  # Field name made lowercase.
    idregiao = models.ForeignKey('Regiao', models.DO_NOTHING, db_column='idRegiao', blank=True, null=True)  # Field name made lowercase.
    idlocalizacao = models.PositiveIntegerField(db_column='idLocalizacao', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'localizacaoincompleta'


class Metododepreservacao(models.Model):
    idmetododepreservacao = models.AutoField(db_column='idMetodoDePreservacao', primary_key=True)  # Field name made lowercase.
    metodo = models.CharField(db_column='Metodo', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'metododepreservacao'


class Ordem(models.Model):
    idordem = models.AutoField(db_column='idOrdem', primary_key=True)  # Field name made lowercase.
    ordem = models.CharField(db_column='Ordem', max_length=45)  # Field name made lowercase.
    idclasse = models.ForeignKey(Classe, models.DO_NOTHING, db_column='idClasse', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ordem'


class Pessoa(models.Model):
    idpessoa = models.AutoField(db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pessoa'


class Preservacaoespecie(models.Model):
    idpreservacaoespecie = models.AutoField(db_column='idPreservacaoEspecie', primary_key=True)  # Field name made lowercase.
    idmetododepreservacao = models.ForeignKey(Metododepreservacao, models.DO_NOTHING, db_column='idMetodoDePreservacao')  # Field name made lowercase.
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'preservacaoespecie'


class Provincia(models.Model):
    idprovincia = models.AutoField(db_column='idProvincia', primary_key=True)  # Field name made lowercase.
    provincia = models.CharField(db_column='Provincia', max_length=45)  # Field name made lowercase.
    idregiao = models.ForeignKey('Regiao', models.DO_NOTHING, db_column='idRegiao')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'provincia'


class Quemencontrou(models.Model):
    idpessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quemencontrou'
        unique_together = (('idpessoa', 'idespecie'),)


class Quemidentificou(models.Model):
    idpessoa = models.ForeignKey(Pessoa, models.DO_NOTHING, db_column='idPessoa', primary_key=True)  # Field name made lowercase.
    idespecie = models.ForeignKey(Especie, models.DO_NOTHING, db_column='idEspecie')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quemidentificou'
        unique_together = (('idpessoa', 'idespecie'),)


class Regiao(models.Model):
    idregiao = models.AutoField(db_column='idRegiao', primary_key=True)  # Field name made lowercase.
    regiao = models.CharField(db_column='Regiao', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'regiao'


class Reino(models.Model):
    idreino = models.AutoField(db_column='idReino', primary_key=True)  # Field name made lowercase.
    descricao = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'reino'


class Tipoutilizador(models.Model):
    idtipoutilizador = models.IntegerField(primary_key=True)
    tipoutilizador = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoutilizador'


class Utilizador(models.Model):
    idutilizador = models.AutoField(db_column='idUtilizador', primary_key=True)  # Field name made lowercase.
    email = models.CharField(max_length=255)
    senha = models.CharField(db_column='Senha', max_length=255)  # Field name made lowercase.
    idtipoutilizador = models.ForeignKey(Tipoutilizador, models.DO_NOTHING, db_column='idtipoutilizador', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilizador'
