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