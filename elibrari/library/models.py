# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AdministratorE1(models.Model):
    administratorid = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    adminid = models.ForeignKey('self', models.DO_NOTHING, db_column='adminid', blank=True, null=True)

    class Meta:
        db_table = 'administrator_e1'


class AuthorE6(models.Model):
    authorname = models.CharField(primary_key=True, max_length=50)
    writingarea = models.TextField()
    description = models.TextField()

    class Meta:
        db_table = 'author_e6'


class CompletedorderE6(models.Model):
    completedorder = models.IntegerField(primary_key=True)
    publicationslist = models.TextField()
    completeddate = models.DateField()
    readerid = models.ForeignKey('ReaderE3', models.DO_NOTHING, db_column='readerid', blank=True, null=True)
    librarianid = models.ForeignKey('LibrarianE2', models.DO_NOTHING, db_column='librarianid', blank=True, null=True)
    editionid = models.ForeignKey('EditionE7', models.DO_NOTHING, db_column='editionid', blank=True, null=True)

    class Meta:
        db_table = 'completedorder_e6'


class EditionE7(models.Model):
    editionid = models.CharField(primary_key=True, max_length=20)
    booktitle = models.CharField(max_length=50)
    registrationnumber = models.IntegerField()
    authors = models.CharField(max_length=150)
    annotation = models.TextField()
    typeedition = models.CharField(max_length=20)
    availablequantity = models.IntegerField()
    refusalid = models.ForeignKey('RefusalE5', models.DO_NOTHING, db_column='refusalid', blank=True, null=True)

    class Meta:
        db_table = 'edition_e7'


class EditionauthorE6E7(models.Model):
    editionid = models.ForeignKey(EditionE7, models.DO_NOTHING, db_column='editionid', blank=True, null=True)
    authorname = models.ForeignKey(AuthorE6, models.DO_NOTHING, db_column='authorname', blank=True, null=True)

    class Meta:
        db_table = 'editionauthor_e6e7'


class EditionsectionE7E12(models.Model):
    editionid = models.ForeignKey(EditionE7, models.DO_NOTHING, db_column='editionid', blank=True, null=True)
    sectionid = models.ForeignKey('SectionsE12', models.DO_NOTHING, db_column='sectionid', blank=True, null=True)

    class Meta:
        db_table = 'editionsection_e7e12'


class LibrarianE2(models.Model):
    librarianid = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    adminid = models.ForeignKey(AdministratorE1, models.DO_NOTHING, db_column='adminid', blank=True, null=True)

    class Meta:
        db_table = 'librarian_e2'


class OrderE4(models.Model):
    orderid = models.IntegerField(primary_key=True)
    publicationslist = models.TextField()
    orderdate = models.DateField()
    readerid = models.ForeignKey('ReaderE3', models.DO_NOTHING, db_column='readerid', blank=True, null=True)

    class Meta:
        db_table = 'order_e4'


class ReaderE3(models.Model):
    accountname = models.CharField(primary_key=True, max_length=50)
    surname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    patronymic = models.CharField(max_length=30)
    login = models.CharField(max_length=20)
    pass_field = models.CharField(db_column='pass', max_length=50)  # Field renamed because it was a Python reserved word.
    detereg = models.DateField()
    adminid = models.ForeignKey(AdministratorE1, models.DO_NOTHING, db_column='adminid', blank=True, null=True)

    class Meta:
        db_table = 'reader_e3'


class ReceipteditionE7E9(models.Model):
    editionid = models.ForeignKey(EditionE7, models.DO_NOTHING, db_column='editionid', blank=True, null=True)
    receiptliteratureid = models.ForeignKey('ReceiptliteratureE9', models.DO_NOTHING, db_column='receiptliteratureid', blank=True, null=True)

    class Meta:
        db_table = 'receiptedition_e7e9'


class ReceiptliteratureE9(models.Model):
    receiptliteratureid = models.IntegerField(primary_key=True)
    publicationslist = models.TextField()
    receiptdate = models.DateField()
    librarianid = models.ForeignKey(LibrarianE2, models.DO_NOTHING, db_column='librarianid', blank=True, null=True)

    class Meta:
        db_table = 'receiptliterature_e9'


class RefusalE5(models.Model):
    refusalid = models.IntegerField(primary_key=True)
    publicationslist = models.TextField()
    refusaldate = models.DateField()
    refusalreason = models.TextField()
    orderid = models.ForeignKey(OrderE4, models.DO_NOTHING, db_column='orderid', blank=True, null=True)
    librarianid = models.ForeignKey(LibrarianE2, models.DO_NOTHING, db_column='librarianid', blank=True, null=True)

    class Meta:
        db_table = 'refusal_e5'


class SectionsE12(models.Model):
    sectionid = models.CharField(primary_key=True, max_length=50)
    descriptionssection = models.TextField()
    parentsection = models.ForeignKey('self', models.DO_NOTHING, db_column='parentsection', blank=True, null=True)

    class Meta:
        db_table = 'sections_e12'


class TreatyE11(models.Model):
    treatyid = models.IntegerField(primary_key=True)
    texttreaty = models.TextField()
    deteonclusion = models.DateField(db_column='dete�onclusion')  # Field name made lowercase.
    duration = models.DateField()
    accountname = models.ForeignKey(ReaderE3, models.DO_NOTHING, db_column='accountname', blank=True, null=True)

    class Meta:
        db_table = 'treaty_e11'


class WritingofeditionE7E10(models.Model):
    editionid = models.ForeignKey(EditionE7, models.DO_NOTHING, db_column='editionid', blank=True, null=True)
    writingofliteratureid = models.ForeignKey('WritingofliteratureE10', models.DO_NOTHING, db_column='writingofliteratureid', blank=True, null=True)

    class Meta:
        db_table = 'writingofedition_e7e10'


class WritingofliteratureE10(models.Model):
    writingofliteratureid = models.IntegerField(primary_key=True)
    publicationslist = models.TextField()
    writingofdate = models.DateField()
    librarianid = models.ForeignKey(LibrarianE2, models.DO_NOTHING, db_column='librarianid', blank=True, null=True)

    class Meta:
        db_table = 'writingofliterature_e10'
