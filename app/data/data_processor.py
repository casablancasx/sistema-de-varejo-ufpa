class DataProcessor:
    @staticmethod
    def process_data(df):
        df['VC'] = df['VC'].str.replace(',', '.').astype('float32')
        df['VV'] = df['VV'].str.replace(',', '.').astype('float32')
        df['VENDIDOS'] = df.drop(['PROD', 'QUANT', 'VV', 'VC'], axis=1).sum(axis=1)
        df['LUCRO'] = ((df['VENDIDOS'] * df['VV']) - (df['QUANT'] * df['VC'])).round(2)
        df['ESTOQUE_ATUAL'] = df['QUANT'] - df['VENDIDOS']
        return df