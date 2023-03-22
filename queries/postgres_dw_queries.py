dimasset_query = '''
    SELECT
         "AssetId"
        ,"ProjectId"
        ,"Project"
        ,"Technology"
        ,"Cod"
        ,"Mw"
        ,"SuccesPct"
        ,"InstalledPower"
        ,"Eoh"
        ,"DateMerchant"
        ,"DismentleDate"
        ,"Repowering"
        ,"DateMsi" 
        ,"InPlanif"
        ,"P50"
        ,"P90"
        FROM dwh."DimAsset"
        '''

dimhedge_query = '''
    SELECT
         "HedgeId"
        ,"AssetKey"
        ,"ProjectId"
        ,"Project"
        ,"Technology"
        ,"TypeHedge"
        ,"ContractStartDate"
        ,"ContractEndDate"
        ,"DismentleDate"
        ,"InstalledPower"
        ,"Profil"
        ,"HedgePct"
        ,"Counterparty"
        ,"CountryCounterparty"
        ,"InPlanif"
      FROM dwh."DimHedge" 
        '''

dimdate_query = '''
    SELECT
        "DateKey"
        ,"Date"
        ,"CalenderYear"
        ,"QuarterNumberOfYear"
        ,"MonthNumberOfYear"
        ,"MonthNameOfYear"
        ,"WeekNumberOfYear"
        ,"DayNumberOfWeek"
        ,"DayNumberOfYear"
        ,"DayNumberOfMonth"
        ,"DayNameOfWeek"
      FROM dwh."DimDate" 
        '''

factprodprices_query = '''
    SELECT 
        "Hedgekey"
        ,"DateKey"
        ,"ProjetId"
        ,"P50Asset"
        ,"P90Asset"
        ,"P50Hedge"
        ,"P90Hedge"
        ,"ContractPrice"
        ,"SettlementPrice"
      FROM dwh."FactProdPrices"
    '''
viewhedgeasset_query= '''
     SELECT * 
         FROM dwh."HedgeAsset"
    '''