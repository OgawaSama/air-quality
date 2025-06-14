import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from collections import Counter




if __name__ == "__main__":
    df = pd.read_csv('data.csv')

    #retirar valores inconsistentes (negativos onde não é temperatura)
    df['PM10'] = df['PM10'].apply(lambda x: max(x, 0))
    df['PM2.5'] = df['PM2.5'].apply(lambda x: max(x, 0))
    df['NO2'] = df['NO2'].apply(lambda x: max(x, 0))
    df['CO'] = df['CO'].apply(lambda x: max(x, 0))
    df['SO2'] = df['SO2'].apply(lambda x: max(x, 0))
    df['Humidity'] = df['Humidity'].apply(lambda x: max(x, 0))
    df['Population_Density'] = df['Population_Density'].apply(lambda x: max(x, 0))



    # separar label do resto dos dados e converter label em números 
    x = df.drop(columns=['Air Quality'])
    y = df['Air Quality']

    # Normalizar os dados
    x_scaled = StandardScaler().fit_transform(x)
    df = pd.DataFrame(x_scaled, columns=x.columns)

    # transformar categorias em números
    encoded = LabelEncoder().fit_transform(y)
    df['Air Quality'] = encoded

    # balancear os dados
    x_resampled, y_resampled = RandomOverSampler(random_state = 10).fit_resample(x_scaled, encoded)
    df = pd.DataFrame(x_resampled, columns=x.columns)
    df['Air Quality'] = y_resampled


    df.to_csv('cleaned.csv', index=False)

