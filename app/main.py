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

# Exibir resultados
print(f'Produto com maior lucro: {max_profit_product} ({max_profit_value})')
print(f'Produto com menor lucro: {min_profit_product} ({min_profit_value})')
print(f'Lucro total: {total_profit}')

# Plotar vendas
SalesPlotter.plot_sales(processed_data, processed_data.drop(['PROD', 'QUANT', 'VV', 'VC'], axis=1))