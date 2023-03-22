from data_pipelines.etl_template_productibles import*
import pandas as pd
import os
import configparser
pd.options.mode.chained_assignment=None

#Load Config
config_file=os.path.join(os.path.dirname("__file__"), 'config/config.ini') 
config=configparser.ConfigParser()
config.read(config_file)

# Initialize Variables
eng_conn=os.path.join(os.path.dirname("__file__"), config['develop']['conn_str'])
dest_dir=os.path.join(os.path.dirname("__file__"), config['develop']['dest_dir'])
temp_dir=os.path.join(os.path.dirname("__file__"),config['develop']['temp_dir'])
src_dir=os.path.join(os.path.dirname("__file__"),config['develop']['src_dir'])
vmr=os.path.join(os.path.dirname("__file__"),config['develop']['vmr'])
planif=os.path.join(os.path.dirname("__file__"),config['develop']['planif'])


productibles="//DESKTOP-JDQLDT1/SharedFolder/d-eng/in/Copie de Productibles - Budget 2022 - version 1 loadé du 21 09 2021.xlsx"
project_names="//DESKTOP-JDQLDT1/SharedFolder/d-eng/temp/project_names.xlsx"
template_asset="//DESKTOP-JDQLDT1/SharedFolder/d-eng/out/template_asset.xlsx"

if __name__ == '__main__':
    df_productibles, df_profile, df_project_names, df_template_asset=Extract(productible_path=productibles, 
                                                                             project_names_path=project_names, 
                                                                             template_asset_path=template_asset)
    df_prod, df_profile_id, df_profile, df_mean_profile, df_template_asset_with_prod=Transform(data_productible=df_productibles, 
                                                                                               data_profile=df_profile, 
                                                                                               data_project_names=df_project_names,
                                                                                               data_template_asset=df_template_asset)
    Load(dest_dir=dest_dir, src_productible=df_prod, src_profile_id=df_profile_id, 
         src_profile=df_profile, src_mean_profile=df_mean_profile, file_name="template_prod")
    load_template_asset(dest_dir=dest_dir, src_flow=df_template_asset_with_prod, file_name='template_asset')