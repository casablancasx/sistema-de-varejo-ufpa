from data.data_loader import DataLoader
from data.data_processor import DataProcessor
from models.sales_analysis import SalesAnalysis
from plots.sales_plotter import SalesPlotter

# Carregar dados
data = DataLoader.load_data('base_de_varejo.csv')

# Processar dados
processed_data = DataProcessor.process_data(data)

# Análise de vendas
max_profit_product, max_profit_value = SalesAnalysis.get_max_profit_product(processed_data)
min_profit_product, min_profit_value = SalesAnalysis.get_min_profit_product(processed_data)
total_profit = SalesAnalysis.get_total_profit(processed_data)
month_with_max_sales = SalesAnalysis.get_month_with_max_sales(processed_data)
total_invested = SalesAnalysis.get_total_invested(processed_data)
total_sold = SalesAnalysis.get_total_sold(processed_data)

# Exibir resultados
print(f'Produto com maior lucro: {max_profit_product} ({max_profit_value})')
print(f'Produto com menor lucro: {min_profit_product} ({min_profit_value})')
print(f'Lucro total: {total_profit}')
print(f'Total investido: {total_invested}')
print(f'Total vendido: {total_sold}')
print(f'Mês com maior quantidade de vendas por produto:\n{month_with_max_sales}')

# Plotar gráficos
SalesPlotter.plot_sales(processed_data, processed_data.drop(['PROD', 'QUANT', 'VV', 'VC'], axis=1))
SalesPlotter.plot_remaining_stock(processed_data)
SalesPlotter.plot_total_sales(processed_data)

# Parecer sobre a saúde financeira da empresa
if total_profit > 0:
    print("A empresa está lucrando.")
else:
    print("A empresa está operando com prejuízo.")