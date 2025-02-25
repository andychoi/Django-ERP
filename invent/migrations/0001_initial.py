# Generated by Django 4.1.5 on 2023-01-17 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basedata', '0003_alter_address_address_type_alter_address_id_and_more'),
        ('selfhelp', '0001_initial'),
        ('organ', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('purchase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InOutDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='create time')),
                ('status', models.BooleanField(default=0, verbose_name='executed')),
                ('event_time', models.DateTimeField(blank=True, null=True, verbose_name='event time')),
                ('cnt', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='count')),
                ('batch', models.CharField(blank=True, max_length=20, null=True, verbose_name='batch')),
                ('price', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='price')),
                ('prop', models.CharField(choices=[('+', 'PLUS'), ('-', 'MINUS')], default='+', max_length=2, verbose_name='plus or minus property')),
                ('source', models.CharField(blank=True, max_length=20, null=True, verbose_name='source')),
                ('material', models.ForeignKey(blank=True, limit_choices_to={'is_virtual': '0'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.material', verbose_name='material')),
                ('measure', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.measure', verbose_name='measure')),
                ('warehouse', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.warehouse', verbose_name='warehouse')),
            ],
        ),
        migrations.CreateModel(
            name='StockOut',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='money of amount')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('9', 'EXECUTED')], default='0', max_length=2, verbose_name='status')),
                ('execute_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.project', verbose_name='project')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='out user')),
                ('wo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='selfhelp.workorder', verbose_name='work order')),
            ],
            options={
                'verbose_name': 'StockOut',
                'verbose_name_plural': 'StockOut',
            },
        ),
        migrations.CreateModel(
            name='OutItem',
            fields=[
                ('inoutdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invent.inoutdetail')),
            ],
            options={
                'verbose_name': 'out item',
                'verbose_name_plural': 'out item',
            },
            bases=('invent.inoutdetail',),
        ),
        migrations.CreateModel(
            name='WareReturn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='money of amount')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('9', 'EXECUTED')], default='0', max_length=2, verbose_name='status')),
                ('execute_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('out', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='invent.stockout', verbose_name='StockOut')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='out user')),
            ],
            options={
                'verbose_name': 'ware return',
                'verbose_name_plural': 'ware return',
            },
        ),
        migrations.CreateModel(
            name='WareAdjust',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('1', 'IN PROGRESS'), ('9', 'EXECUTED')], default='0', max_length=2, verbose_name='status')),
                ('execute_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='out user')),
            ],
            options={
                'verbose_name': 'ware adjust',
                'verbose_name_plural': 'ware adjust',
            },
        ),
        migrations.CreateModel(
            name='StockIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('1', 'QUALITY TESTING'), ('9', 'EXECUTED')], default='0', max_length=2, verbose_name='status')),
                ('execute_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='stock in money of amount')),
                ('batch', models.CharField(blank=True, max_length=20, null=True, verbose_name='batch')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('po', models.ForeignKey(blank=True, limit_choices_to={'entry_status': '0'}, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='purchase.purchaseorder', verbose_name='purchase order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.warehouse', verbose_name='warehouse')),
            ],
            options={
                'verbose_name': 'StockIn',
                'verbose_name_plural': 'StockIn',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('cnt', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='count')),
                ('batch', models.CharField(blank=True, max_length=20, null=True, verbose_name='batch')),
                ('price', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='price')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.material', verbose_name='material')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.measure', verbose_name='measure')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('warehouse', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='basedata.warehouse', verbose_name='warehouse')),
            ],
            options={
                'verbose_name': 'Inventory',
                'verbose_name_plural': 'Inventory',
                'ordering': ['material'],
            },
        ),
        migrations.CreateModel(
            name='InitialInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin', models.DateField(blank=True, null=True, verbose_name='begin date')),
                ('end', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('creator', models.CharField(blank=True, max_length=20, null=True, verbose_name='creator')),
                ('modifier', models.CharField(blank=True, max_length=20, null=True, verbose_name='modifier')),
                ('creation', models.DateTimeField(auto_now_add=True, null=True, verbose_name='creation')),
                ('modification', models.DateTimeField(auto_now=True, null=True, verbose_name='modification')),
                ('code', models.CharField(blank=True, max_length=20, null=True, verbose_name='code')),
                ('title', models.CharField(max_length=40, verbose_name='title')),
                ('status', models.CharField(choices=[('0', 'NEW'), ('9', 'EXECUTED')], default='0', max_length=2, verbose_name='status')),
                ('execute_time', models.DateTimeField(blank=True, null=True, verbose_name='execute time')),
                ('attach', models.FileField(blank=True, help_text='参考FD0002模板文档', null=True, upload_to='inventory', verbose_name='attach')),
                ('amount', models.DecimalField(blank=True, decimal_places=4, max_digits=14, null=True, verbose_name='money of amount')),
                ('org', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='organ.organization', verbose_name='organization')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Initial Inventory',
                'verbose_name_plural': 'Initial Inventory',
            },
        ),
        migrations.CreateModel(
            name='ReturnItem',
            fields=[
                ('inoutdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invent.inoutdetail')),
                ('out_cnt', models.DecimalField(decimal_places=4, max_digits=14, verbose_name='out count')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.warereturn')),
                ('out_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invent.outitem', verbose_name='out item')),
            ],
            options={
                'verbose_name': 'return item',
                'verbose_name_plural': 'return item',
            },
            bases=('invent.inoutdetail',),
        ),
        migrations.AddField(
            model_name='outitem',
            name='inventory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invent.inventory', verbose_name='inventory material'),
        ),
        migrations.AddField(
            model_name='outitem',
            name='master',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.stockout'),
        ),
        migrations.CreateModel(
            name='InitItem',
            fields=[
                ('inoutdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invent.inoutdetail')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.initialinventory')),
            ],
            options={
                'verbose_name': 'init item',
                'verbose_name_plural': 'init item',
            },
            bases=('invent.inoutdetail',),
        ),
        migrations.CreateModel(
            name='InItem',
            fields=[
                ('inoutdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invent.inoutdetail')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.stockin')),
                ('po_item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='purchase.poitem', verbose_name='po item')),
            ],
            options={
                'verbose_name': 'in item',
                'verbose_name_plural': 'in item',
            },
            bases=('invent.inoutdetail',),
        ),
        migrations.CreateModel(
            name='AdjustItem',
            fields=[
                ('inoutdetail_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='invent.inoutdetail')),
                ('inventory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invent.inventory', verbose_name='inventory material')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invent.wareadjust')),
            ],
            options={
                'verbose_name': 'adjust item',
                'verbose_name_plural': 'adjust item',
            },
            bases=('invent.inoutdetail',),
        ),
    ]
