import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from data.data_loader import DataLoader
from data.data_processor import DataProcessor
from models.sales_analysis import SalesAnalysis
from plots.sales_plotter import SalesPlotter


# Função para exibir gráficos no canvas
def plot_to_canvas(fig, frame):
    for widget in frame.winfo_children():
        widget.destroy()  # Remove gráficos anteriores para evitar sobreposição
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)


def main():
    # Carregar dados
    data = DataLoader.load_data('base_de_varejo.csv')
    processed_data = DataProcessor.process_data(data)

    # Análise de vendas
    max_profit_product, max_profit_value = SalesAnalysis.get_max_profit_product(processed_data)
    min_profit_product, min_profit_value = SalesAnalysis.get_min_profit_product(processed_data)
    total_profit = SalesAnalysis.get_total_profit(processed_data)
    month_with_max_sales = SalesAnalysis.get_month_with_max_sales(processed_data)
    total_invested = SalesAnalysis.get_total_invested(processed_data)
    total_sold = SalesAnalysis.get_total_sold(processed_data)

    # Criar interface gráfica
    root = tk.Tk()
    root.title("📊 Financial Health Report")
    root.state('zoomed')

    root.configure(bg="#F4F4F4")

    # Aplicar estilo moderno
    style = ttk.Style()
    style.configure("TFrame", background="#F4F4F4")
    style.configure("TLabel", background="#F4F4F4", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 11, "bold"), padding=6)

    # Frame principal
    main_frame = ttk.Frame(root, padding="10")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # Frame de informações
    info_frame = ttk.LabelFrame(main_frame, text="📈 Relatório Financeiro", padding="10")
    info_frame.pack(fill=tk.X, padx=10, pady=5)

    ttk.Label(info_frame, text=f"🔹 Produto com maior lucro: {max_profit_product} (R$ {max_profit_value:.2f})",
              font=("Arial", 11)).pack(anchor=tk.W)
    ttk.Label(info_frame, text=f"🔹 Produto com menor lucro: {min_profit_product} (R$ {min_profit_value:.2f})",
              font=("Arial", 11)).pack(anchor=tk.W)
    ttk.Label(info_frame, text=f"💰 Lucro total: R$ {total_profit:.2f}", font=("Arial", 11, "bold")).pack(anchor=tk.W)
    ttk.Label(info_frame, text=f"📉 Total investido: R$ {total_invested:.2f}", font=("Arial", 11)).pack(anchor=tk.W)
    ttk.Label(info_frame, text=f"📦 Total vendido: {total_sold}", font=("Arial", 11)).pack(anchor=tk.W)

    ttk.Label(info_frame, text="📆 Mês com maior quantidade de vendas por produto:", font=("Arial", 11, "bold")).pack(
        anchor=tk.W)
    for product, month in month_with_max_sales.items():
        ttk.Label(info_frame, text=f"• {product}: {month}", font=("Arial", 11)).pack(anchor=tk.W)

    # Indicador de saúde financeira
    health_label = ttk.Label(info_frame, font=("Arial", 12, "bold"))
    health_label.pack(anchor=tk.W, pady=5)

    if total_profit > 0:
        health_label.config(text="✅ A empresa está lucrando.", foreground="green")
    else:
        health_label.config(text="❌ A empresa está operando com prejuízo.", foreground="red")

    # Funções para exibir os gráficos

    def plot_sales():
        fig = SalesPlotter.plot_sales(data,
                                      data.drop(['PROD', 'QUANT', 'VV', 'VC', 'VENDIDOS', 'LUCRO', 'ESTOQUE_ATUAL'],
                                                axis=1))
        plot_to_canvas(fig, plot_frame)

    def plot_remaining_stock():
        fig = SalesPlotter.plot_remaining_stock(processed_data)
        plot_to_canvas(fig, plot_frame)

    def plot_total_sales():
        fig = SalesPlotter.plot_total_sales(processed_data)
        plot_to_canvas(fig, plot_frame)

    # Frame para botões de plotagem
    button_frame = ttk.LabelFrame(main_frame, text='Opções', padding="10")
    button_frame.pack(fill=tk.X)

    ttk.Button(button_frame, text="📈 Plotar Vendas", command=plot_sales).pack(side=tk.LEFT, padx=10, pady=5)
    ttk.Button(button_frame, text="📦 Estoque Restante", command=plot_remaining_stock).pack(side=tk.LEFT, padx=10,
                                                                                           pady=5)
    ttk.Button(button_frame, text="💵 Total de Vendas", command=plot_total_sales).pack(side=tk.LEFT, padx=10, pady=5)

    # Frame para exibição dos gráficos
    plot_frame = ttk.LabelFrame(main_frame, text="📊 Gráficos", padding="10")
    plot_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    root.mainloop()


if __name__ == "__main__":
    main()
