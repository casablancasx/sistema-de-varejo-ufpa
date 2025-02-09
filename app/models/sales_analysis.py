class SalesAnalysis:
    @staticmethod
    def get_max_profit_product(df):
        return df.loc[df['LUCRO'].idxmax(), 'PROD'], df['LUCRO'].max()

    @staticmethod
    def get_min_profit_product(df):
        return df.loc[df['LUCRO'].idxmin(), 'PROD'], df['LUCRO'].min()

    @staticmethod
    def get_total_profit(df):
        return df['LUCRO'].sum()

    @staticmethod
    def get_month_with_max_sales(df):
        return df.drop(['PROD', 'QUANT', 'VV', 'VC', 'LUCRO', 'ESTOQUE_ATUAL'], axis=1).idxmax(axis=1)

    @staticmethod
    def get_total_invested(df):
        return (df['QUANT'] * df['VC']).sum()

    @staticmethod
    def get_total_sold(df):
        return (df['VENDIDOS'] * df['VV']).sum()