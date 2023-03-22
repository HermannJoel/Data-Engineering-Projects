from data_pipelines.etl_template_asset import*
import pandas as pd
import configparser
import sys
import os
pd.options.mode.chained_assignment=None


#ChooseCwd(cwd='D:/git-local-cwd/Data-Engineering-Projects/') 
#Load Config    
config_file=os.path.join(os.path.dirname('__file__'), 'Config/config.ini') 
config=configparser.ConfigParser()
config.read(config_file)

# Initialize Variables
#eng_conn=os.path.join(os.path.dirname("__file__"), config['develop']['conn_str'])
#dest_dir=os.path.join(os.path.dirname("__file__"), config['develop']['dest_dir'])
#src_dir=os.path.join(os.path.dirname("__file__"),config['develop']['src_dir'])
#vmr=os.path.join(os.path.dirname("__file__"),config['develop']['vmr'])
#planif=os.path.join(os.path.dirname("__file__"),config['develop']['planif'])


vmr='//DESKTOP-JDQLDT1/SharedFolder/d-eng/in/Volumes_Market_Repowering.xlsx'
planif='//DESKTOP-JDQLDT1/SharedFolder/d-eng/in/Outils planification agrege 2022-2024.xlsm'

if __name__=='__main__':
    df_asset_vmr, df_asset_planif=Extract(asset_vmr_path=vmr, asset_planif_path=planif)
    template_asset_without_prod=Transform(data_asset_vmr=df_asset_vmr, data_asset_planif=df_asset_planif)  
    Load(dest_dir=dest_dir, src_flow=template_asset_without_prod, file_name="template_asset")