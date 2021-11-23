import pandas as pd

def devolver_unicos(ventana, dataframe, columndate=None, id=None):
    '''
    Funcion para devolver unicos en una ventana temporal
    Puede ser usada con cualquier dataset pasandole la columna id y la columna date
    En caso de el mes ser mayor al maximo menos la ventana se puede obtar por no devolver ningún valor
    En este caso devuelvo los únicos del mes y no de la ventana en caso de no existir la ventana tanto superior cómo inferior
    uso: devolver_unicos(3,df)
    '''
    if columndate is None :
        columndate = "year_month"
    if id is None :
        id="CIF_ID"
    df1 = dataframe[[columndate, id]] #subseteo mi dataframe
    meses = df1[columndate].unique().map(str)
    maximo = (df1[columndate].max() - ventana)
    for mes in meses:
        if mes < str(maximo):
            ventana_inf = pd.to_datetime(mes) +pd.DateOffset(months=-ventana)
            ventana_sup = pd.to_datetime(mes) + pd.DateOffset(months=ventana)
            ventana_inf = (ventana_inf.strftime('%Y-%m'))
            ventana_sup = (ventana_sup.strftime('%Y-%m'))
            df1[(df1["year_month"] > ventana_inf) & (df1["year_month"] < ventana_sup)].drop_duplicates(subset ="CIF_ID",keep = "last", inplace = False)
            dfprueba[mes] = df1.CIF_ID

        else:
            mes_i = pd.to_datetime(mes)
            mes_i = (mes_i.strftime('%Y-%m'))
            df1[(df1[columndate] == mes)].drop_duplicates(subset ="CIF_ID", keep ="last", inplace = False)
            dfprueba[mes] = filtro.CIF_ID


    return dfprueba


3333333333333333+

3
3
3
3
3
3
3
3
3
333333333333333333333333333333333333333



















































































































































































































































































































































































3




++