import matplotlib.pyplot as plt

class SalesPlotter:
    @staticmethod
    def plot_sales(df, sales_table):
        plt.figure(figsize=(10, 6))
        for index, produto in df.iterrows():
            plt.plot(sales_table.columns, sales_table.loc[index], label=produto['PROD'])
        plt.title('Quantidade de Produtos Vendidos ao Longo dos Meses')
        plt.xlabel('Meses')
        plt.ylabel('Quantidade Vendida')
        plt.legend(title='Produtos')
        plt.grid(True)
        plt.xticks(rotation=90)
        plt.tight_layout()
        plt.show()