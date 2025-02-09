import pandas as pd


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
        # Define the month columns in the correct order
        month_map = {
                'JAN': 'Janeiro', 'FEV': 'Fervereiro', 'MAR': 'Março', 'ABR': 'Abril', 'MAI': 'Maio', 'JUN': 'Junho',
                'JUL': 'Julho', 'AGO': 'Agosto', 'SET': 'Setembro', 'OUT': 'Outubro', 'NOV': 'Novembro',
                'DEZ': 'Dezembro'
        }
        # Select only the monthly sales columns
        sales_columns = [col for col in df.columns if col in month_map]
        # Get the month with the highest sales for each product
        max_sales_months = df[sales_columns].idxmax(axis=1)
        # Map month abbreviations to full month names
        max_sales_months = max_sales_months.map(month_map)
        # Return a Series with the product and the corresponding month with max sales
        return pd.Series(max_sales_months.values, index=df['PROD'])

    @staticmethod
    def get_total_invested(df):
        return (df['QUANT'] * df['VC']).sum()

    @staticmethod
    def get_total_sold(df):
        return (df['VENDIDOS'] * df['VV']).sum()
