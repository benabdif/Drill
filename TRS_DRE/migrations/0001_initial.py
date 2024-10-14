# Generated by Django 4.2.14 on 2024-10-14 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cellar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cellar_Installation', models.CharField(blank=True, max_length=100, null=True)),
                ('Soil_Test_Request', models.IntegerField(blank=True, null=True)),
                ('REQ_Date', models.DateField(blank=True, null=True)),
                ('Cellar_REQ_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('Soil_Test_Contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('Conducted_by', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Clean_Up_Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clean_up_request_Number', models.IntegerField(blank=True, null=True)),
                ('clean_up_request_Date', models.DateField(blank=True, null=True)),
                ('clean_up_request_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_construction_contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_KPI', models.IntegerField(blank=True, null=True)),
                ('clean_up_start_Date', models.DateField(blank=True, null=True)),
                ('clean_Up_start_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_completion_date', models.DateField(blank=True, null=True)),
                ('clean_up_post_clean_Up_Turnover', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_monitored_by', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_Quantities_details', models.CharField(blank=True, max_length=200, null=True)),
                ('clean_up_project_team_details', models.CharField(blank=True, max_length=200, null=True)),
                ('clean_up_pre_Clean_Up_Turnover', models.CharField(blank=True, max_length=100, null=True)),
                ('clean_up_Criticality', models.CharField(choices=[('YES', 'YES'), ('No', 'No')], default='N/A', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Construction_Departmeent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CONSTR_REQ', models.IntegerField(blank=True, null=True)),
                ('REQ_Start_Date', models.DateField(blank=True, null=True)),
                ('REQ_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('CONSTR_Contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('CONSTR_KPI', models.IntegerField(blank=True, null=True)),
                ('CONSTR_KOM', models.DateField(blank=True, null=True)),
                ('Conducted_by_KOM', models.CharField(blank=True, max_length=100, null=True)),
                ('Construction_Status', models.IntegerField(blank=True, null=True)),
                ('CONSTR_Skid_ROAD_DIST', models.IntegerField(blank=True, null=True)),
                ('Final_Survey', models.CharField(blank=True, max_length=100, null=True)),
                ('Conducted_by_Final_Survey', models.CharField(blank=True, max_length=100, null=True)),
                ('Unit', models.CharField(blank=True, max_length=100, null=True)),
                ('Post_CONSTR_Rurn_OVER', models.CharField(blank=True, max_length=100, null=True)),
                ('REQ_End_Date', models.DateField(blank=True, null=True)),
                ('Quanatities_Detities', models.CharField(blank=True, max_length=100, null=True)),
                ('Project_team_Details', models.CharField(blank=True, max_length=100, null=True)),
                ('Remark_and_Hold', models.CharField(blank=True, max_length=100, null=True)),
                ('Criticality', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes/No', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Contractor',
            fields=[
                ('contractor_ID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('contractor_name', models.CharField(max_length=100)),
                ('update_L', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Engineering',
            fields=[
                ('Eng_ID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('Eng_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='HDPE_Installation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lining_Installation', models.CharField(blank=True, max_length=100, null=True)),
                ('REQ_Lining_Number', models.IntegerField(blank=True, null=True)),
                ('HDPE_REQ_Date', models.DateField(blank=True, null=True)),
                ('HDPE_REQ_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('Installation_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('Total_Area_Installed', models.IntegerField(blank=True, null=True)),
                ('Lining_Contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('Conducted_by_info', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantities_Details', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='location_Support',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_location_support_Request_Number', models.IntegerField(blank=True, null=True)),
                ('on_location_support_Request_date', models.DateField(blank=True, null=True)),
                ('on_location_support_Request_status', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_dispatch_By', models.CharField(blank=True, max_length=100, null=True)),
                ('on_location_support_Remark', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pre_Construction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Approval_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('CONDTR_REQ', models.CharField(blank=True, choices=[('Strip', 'Strip'), ('Logistic', 'Logistic'), ('Access', 'Access')], max_length=100, null=True)),
                ('Approved_Lay_out', models.CharField(blank=True, max_length=100, null=True)),
                ('Date_Approved_Lay_out', models.DateField(blank=True, null=True)),
                ('Approval_Date', models.DateField(blank=True, null=True)),
                ('R_Completio_Date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RepairSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sand_removal', models.BooleanField(blank=True, default=False)),
                ('Extension', models.BooleanField(blank=True, default=False)),
                ('Re_Compaction', models.BooleanField(blank=True, default=False)),
                ('Change_Cellar', models.BooleanField(blank=True, default=False)),
                ('Modification', models.BooleanField(blank=True, default=False)),
                ('Complete_Repair', models.BooleanField(blank=True, default=False)),
                ('Additional', models.BooleanField(blank=True, default=False)),
                ('REQ_Repair_NUMBER', models.IntegerField(blank=True, null=True)),
                ('REQ_Repair_Status', models.CharField(blank=True, max_length=100, null=True)),
                ('REQ_Repair_Date', models.DateField(blank=True, null=True)),
                ('Contractor_Contractor_Repair', models.CharField(blank=True, null=True)),
                ('Repair_Start_Date', models.CharField(blank=True, null=True)),
                ('Repair_Start_date', models.DateField(blank=True, null=True)),
                ('Repair_status', models.CharField(blank=True, max_length=100, null=True)),
                ('Repair_completion_Date', models.DateField(blank=True, null=True)),
                ('monitored_By_Repair', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantities_Details_Repair', models.CharField(blank=True, max_length=100, null=True)),
                ('Project_team_Details_Repair', models.CharField(blank=True, max_length=100, null=True)),
                ('Repair_Criticality', models.CharField(choices=[('Yes', 'No')], default='N/A', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Rig_Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RIG_MOVE_REQ', models.IntegerField(blank=True, null=True)),
                ('RIG_MOVE_NAME', models.CharField(blank=True, max_length=100, null=True)),
                ('RIG_MOVE_WELL', models.CharField(blank=True, max_length=100, null=True)),
                ('RIG_MOVE_STATUS', models.CharField(blank=True, max_length=100, null=True)),
                ('RIG_MOVE_DOCUMENTS', models.FileField(blank=True, null=True, upload_to='rig_move_documents/')),
                ('RIG_MOVE_CONDUCTED_BY', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rigg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rig_name', models.CharField(max_length=100)),
                ('Rig_Type', models.CharField(blank=True, choices=[('Exp', 'Exp'), ('Gas Dev...', 'Gas Dev...'), ('UR', 'UR')], max_length=100, null=True)),
                ('Operation_Department', models.CharField(blank=True, max_length=100, null=True)),
                ('Operation_Manager', models.CharField(blank=True, max_length=100, null=True)),
                ('Permanent_Construction_Cc', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Update_Permanent_Construction_Cc', models.DateField(blank=True, null=True)),
                ('Permanent_HDPE_Contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Update_Permanent_HDPE_Contractor', models.DateField(blank=True, null=True)),
                ('Permanent_Soil_Test_Contractor', models.CharField(blank=True, max_length=100, null=True)),
                ('Last_Update_Permanent_Soil_Test_Contractor', models.DateField(blank=True, null=True)),
                ('Current_Assigned_Unit', models.CharField(blank=True, max_length=100, null=True)),
                ('Current_Assigned_WS_Engineer', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('ID', models.IntegerField(blank=True, primary_key=True, serialize=False)),
                ('name_unit', models.CharField(max_length=100)),
                ('Unit_supervision', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Well_Construction_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('well_construction_name', models.CharField(max_length=100)),
                ('well_construction_objective', models.CharField(choices=[('New', 'New'), ('Workover', 'Workover')], default='New', max_length=10)),
                ('well_construction_BI', models.IntegerField(blank=True, null=True)),
                ('well_construction_Spud_date', models.DateTimeField(blank=True, null=True)),
                ('well_construction_Reference_Number', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_DWO_Engineer', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_Producing_Engineer', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_Drillsite_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_fluid_Type_choices', models.CharField(choices=[('Oil', 'Oil'), ('Gas', 'Gas'), ('Water', 'Water')], default='NA', max_length=10)),
                ('well_construction_Charge_Account', models.IntegerField(blank=True, null=True)),
                ('well_construction_Released_date', models.DateTimeField(blank=True, null=True)),
                ('well_construction_Direct_distance_DH', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_Engineering_department', models.CharField(blank=True, max_length=100, null=True)),
                ('well_construction_GOSP_WIP_Department', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wellg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('progress', models.PositiveIntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movementg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_cleaned_up', models.BooleanField(default=False)),
                ('Cellar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.cellar')),
                ('Construction_Departmeent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.construction_departmeent')),
                ('Contractor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.contractor')),
                ('Eng', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.engineering')),
                ('HDPE_Installation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.hdpe_installation')),
                ('Pre_Construction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.pre_construction')),
                ('Rig_Move', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.rig_move')),
                ('Units', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.units')),
                ('Well_Construction_Infotion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.well_construction_info')),
                ('rig', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.rigg')),
                ('well', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TRS_DRE.wellg')),
            ],
        ),
        ]
