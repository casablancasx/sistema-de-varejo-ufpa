import matplotlib.pyplot as plt

class SalesPlotter:
    @staticmethod
    def plot_sales(df, sales_table):
        fig, ax = plt.subplots(figsize=(10, 6))
        for index, produto in df.iterrows():
            ax.plot(sales_table.columns, sales_table.loc[index], label=produto['PROD'])
        ax.set_title('Quantidade de Produtos Vendidos ao Longo dos Meses')
        ax.set_xlabel('Meses')
        ax.set_ylabel('Quantidade Vendida')
        ax.legend(title='Produtos')
        ax.grid(True)
        plt.xticks(rotation=90)
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_remaining_stock(df):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['PROD'], df['ESTOQUE_ATUAL'])
        ax.set_title('Estoque Restante de Cada Produto Após 12 Meses')
        ax.set_xlabel('Produtos')
        ax.set_ylabel('Estoque Restante')
        plt.xticks(rotation=90)
        plt.tight_layout()
        return fig

    @staticmethod
    def plot_total_sales(df):
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(df['PROD'], df['VENDIDOS'])
        ax.set_title('Quantidade de Vendas de Cada Produto Após 12 Meses')
        ax.set_xlabel('Produtos')
        ax.set_ylabel('Quantidade Vendida')
        plt.xticks(rotation=90)
        plt.tight_layout()
        return fig