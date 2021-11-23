import pandas as pd

class prepro(self)

def recortar(fecha,df1,ventana):
    fecha2 = pd.to_datetime(fecha)
    ventana_inf = fecha2+ pd.offsets.DateOffset(months=-ventana)
    ventana_sup = fecha2+ pd.offsets.DateOffset(months=ventana)
    filtro=  df1.loc[(df1['CREATION_DATE'] > ventana_inf) & (df1['CREATION_DATE'] < ventana_sup)]
    filtro.sort_values("CIF_ID", inplace = True)
    filtro.drop_duplicates(subset ="CIF_ID",
                     keep = False, inplace = True)

    df3 = filtro.loc[df1['mes']==fecha2.month]
    return df3