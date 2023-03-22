from data_pipelines.etl_template_hedge import*
import os
import configparser
pd.options.mode.chained_assignment=None

#Load Config
config_file=os.path.join(os.path.dirname("__file__"), 'config/config.ini') 
config=configparser.ConfigParser()
config.read(config_file)

# Initialize Variables
dest_dir=os.path.join(os.path.dirname("__file__"),config['develop']['dest_dir'])
temp_dir=os.path.join(os.path.dirname("__file__"),config['develop']['temp_dir'])
src_dir=os.path.join(os.path.dirname("__file__"),config['develop']['src_dir'])
vmr=os.path.join(os.path.dirname("__file__"),config['develop']['vmr'])
planif=os.path.join(os.path.dirname("__file__"),config['develop']['planif'])


vmr="//DESKTOP-JDQLDT1/SharedFolder/d-eng/in/Volumes_Market_Repowering.xlsx"
planif="//DESKTOP-JDQLDT1/SharedFolder/d-eng/in/Outils planification agrege 2022-2024.xlsm"
hedge_vmr="//DESKTOP-JDQLDT1/SharedFolder/d-eng/temp/hedge_vmr.xlsx"
hedge_planif="//DESKTOP-JDQLDT1/SharedFolder/d-eng/temp/hedge_planif.xlsx"


if __name__ == '__main__':
    df_hedge_vmr, df_hedge_planif=Extract(hedge_vmr_path=hedge_vmr, hedge_planif_path=hedge_planif)
    template_hedge=transform(hedge_vmr=df_hedge_vmr, hedge_planif=df_hedge_planif)
    Load(dest_dir=dest_dir, src_flow=template_hedge, file_name="template_hedge")