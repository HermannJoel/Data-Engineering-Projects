import pandas as pd
import numpy as np
xrange = range
from datetime import datetime
import sys
pd.options.mode.chained_assignment=None

# adding etls/functions to the system path
sys.path.insert(0, 'D:/git-local-cwd/Data-Engineering-Projects/blx_mdp_data-eng/etls/functions')
from etl_functions import (RemoveP50P90TypeHedge, CreateDataFrame, 
                           MergeDataFrame, AdjustedByPct, ChooseCwd,
                           RemoveP50P90, ReadExcelFile, SelectColumns,CreateMiniDataFrame)
dest_dir="//DESKTOP-JDQLDT1/SharedFolder/d-eng/out/"
temp_dir="//DESKTOP-JDQLDT1/SharedFolder/d-eng/temp/"


def Extract(hedge_vmr_path, hedge_planif_path):
    ''' Function to extract excel files.
    Parameters
    ==========
    hedge_vmr_path: str
        path excel file containing data hedge in prod
    hedge_planif_path: str
        path excel file containing data hedge in planif    
    Returns
    =======
    df_hedge_vmr: DataFrame
        hedge vmr dataframe
    df_hedge_planif: DataFrame
        hedge planif dataframe
    '''
    try:
        df_hedge_vmr=ReadExcelFile(hedge_vmr_path)
        df_hedge_planif=ReadExcelFile(hedge_planif_path)
        return df_hedge_vmr, df_hedge_planif 
    except Exception as e:
        print("Data Extraction error!: "+str(e))

def transform(hedge_vmr, hedge_planif, **kwargs):
    """
    udf Function to generate template hedge
    Parameters
    ===========
    **kwargs
        hedge_vmr: DataFrame
                
        hedge_planif: DataFrame
    Returns
    =======
    hedge_template: DataFrame
        template asset dataframe
    """
    try:
        #===============     Hedge vmr     =======================
        #To create hedge df with vmr data
        df_hedge_vmr=hedge_vmr
        df_hedge_vmr["profil"]=np.nan
        df_hedge_vmr["pct_couverture"]=np.nan
        df_hedge_vmr["contrepartie"]=np.nan
        df_hedge_vmr["pays_contrepartie"]=np.nan
 
        df_hedge_vmr = df_hedge_vmr[["id", "hedge_id", "projet_id","projet", "technologie", "type_hedge", 
                              "cod", "date_merchant", "date_dementelement", "puissance_installée", "profil", 
                              "pct_couverture", "contrepartie", "pays_contrepartie", "en_planif"]]
 
        df_hedge_vmr.rename(columns={"cod":"date_debut", "date_merchant":"date_fin"}, inplace = True)

        ppa_vmr = ["NIBA" , "CHEP", "ALBE", "ALME", "ALMO", "ALVE", "PLOU"]

        df_hedge_vmr["type_hedge"] = df_hedge_vmr["type_hedge"].str.replace("FiT", "OA")
        df_hedge_vmr.loc[df_hedge_vmr.projet_id.isin(ppa_vmr) == True, "type_hedge"] = "PPA" 

        df_hedge_vmr.loc[df_hedge_vmr['type_hedge'] == "OA", "pct_couverture"] = 1
        df_hedge_vmr.loc[df_hedge_vmr['type_hedge'] != "OA", "pct_couverture"] = 1
        df_hedge_vmr.loc[df_hedge_vmr['type_hedge'] == "PPA", "pct_couverture"] = 1

        #===============     Hedge Planif     =======================
        #To import hedge_planif data. this was generated when creating the template_asset.
        df_hedge_planif=hedge_planif
        df_hedge_planif["type_hedge"] = "CR"
        df_hedge_planif["profil"] = np.nan
        df_hedge_planif["pct_couverture"] = np.nan
        df_hedge_planif["contrepartie"] = np.nan
        df_hedge_planif["pays_contrepartie"] = np.nan

        df_hedge_planif = df_hedge_planif[["id", "hedge_id", "projet_id", "projet", "technologie", "type_hedge", 
                                           "cod", "date_merchant", "date_dementelement", "puissance_installée", 
                                           "profil", "pct_couverture", "contrepartie", "pays_contrepartie", "en_planif"]]

        df_hedge_planif.rename(columns={"cod":"date_debut", "date_merchant":"date_fin"}, inplace = True)

        ppa_planif = ["SE19", "SE07"]
        df_hedge_planif.loc[df_hedge_planif.projet_id.isin(ppa_planif) == True, "type_hedge"] = "PPA"
        df_hedge_planif.loc[df_hedge_planif['type_hedge'] == "CR", "pct_couverture"] = 1
        df_hedge_planif.loc[df_hedge_planif['type_hedge'] == "PPA", "pct_couverture"] = 1

        #To merge both data frame
        frames = [df_hedge_vmr, df_hedge_planif]
        hedge_template = pd.concat(frames)
        hedge_template.reset_index(inplace=True, drop=True)
        hedge_template.drop("id", axis=1, inplace=True)
        hedge_template=hedge_template.assign(id=[1 + i for i in xrange(len(hedge_template))])[['id'] + hedge_template.columns.tolist()]
        
        return hedge_template
    
    except Exception as e:
        print("Template hedge transformation error!: "+str(e))



def Load(dest_dir, src_flow, file_name):
    try:
        src_flow.to_excel(dest_dir+file_name+'.xlsx', index=False, float_format="%.4f")
        print("Data loaded succesfully!")
    except Exception as e:
        print("Data load error!: "+str(e))
        