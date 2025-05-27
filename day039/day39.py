from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

def calculate_tip(amount, percentage):
    return amount * (percentage / 100)

def main():
    console = Console()
    console.print(Panel("[bold cyan]Tip Calculator[/bold cyan]", expand=False))
    
    while True:
        bill_amount = Prompt.ask("[green]Enter the bill amount (or 'exit' to quit)[/green]")
        if bill_amount.lower() == 'exit':
            console.print("[bold red]Exiting...[/bold red]")
            break
        
        tip_percentage = Prompt.ask("[green]Enter the tip percentage[/green]")
        
        try:
            bill_amount = float(bill_amount)
            tip_percentage = float(tip_percentage)
            tip = calculate_tip(bill_amount, tip_percentage)
            total = bill_amount + tip
            console.print(Panel(f"[bold green]✔ Tip: ${tip:.2f}, Total: ${total:.2f}[/bold green]", expand=False))
        except ValueError:
            console.print(Panel("[bold red]✖ Invalid input. Please enter numeric values.[/bold red]", expand=False))

if __name__ == "__main__":
    main()
