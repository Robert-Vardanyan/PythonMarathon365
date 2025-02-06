from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    console = Console()
    console.print(Panel("[bold cyan]Factorial Calculator[/bold cyan]", expand=False))
    
    while True:
        number = Prompt.ask("[green]Enter a number (or 'exit' to quit)[/green]")
        if number.lower() == 'exit':
            console.print("[bold red]Exiting...[/bold red]")
            break
        
        if number.isdigit():
            result = factorial(int(number))
            console.print(Panel(f"[bold green]✔ Factorial of {number} is {result}![/bold green]", expand=False))
        else:
            console.print(Panel(f"[bold red]✖ Invalid input. Please enter a non-negative integer.[/bold red]", expand=False))

if __name__ == "__main__":
    main()