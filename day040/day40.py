from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.table import Table

def convert_currency(amount, rate):
    return amount * rate

def main():
    console = Console()
    console.print(Panel("[bold cyan]💰 Currency Converter 💰[/bold cyan]", expand=False))
    
    while True:
        amount = Prompt.ask("[bold yellow]💵 Enter the amount (or 'exit' to quit)[/bold yellow]")
        if amount.lower() == 'exit':
            console.print("[bold red]🚪 Exiting...[/bold red]")
            break
        
        rate = Prompt.ask("[bold magenta]📈 Enter the exchange rate[/bold magenta]")
        currency_from = Prompt.ask("[bold blue]🔄 From currency (e.g., USD)[/bold blue]")
        currency_to = Prompt.ask("[bold green]🔄 To currency (e.g., EUR)[/bold green]")
        
        try:
            amount = float(amount)
            rate = float(rate)
            converted = convert_currency(amount, rate)
            
            table = Table(title="Currency Conversion", header_style="bold white")
            table.add_column("From", style="bold blue")
            table.add_column("To", style="bold green")
            table.add_column("Amount", style="bold yellow")
            table.add_column("Converted", style="bold magenta")
            
            table.add_row(currency_from, currency_to, f"{amount:.2f}", f"{converted:.2f}")
            console.print(table)
        except ValueError:
            console.print(Panel("[bold red]✖ Invalid input. Please enter numeric values.[/bold red]", expand=False))

if __name__ == "__main__":
    main()
