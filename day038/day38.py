from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    console = Console()
    console.print(Panel("[bold cyan]Temperature Converter[/bold cyan]", expand=False))
    
    while True:
        choice = Prompt.ask("[green]Convert: 1) Celsius to Fahrenheit, 2) Fahrenheit to Celsius, or 'exit' to quit[/green]")
        if choice.lower() == 'exit':
            console.print("[bold red]Exiting...[/bold red]")
            break
        
        if choice in ['1', '2']:
            temp = Prompt.ask("[green]Enter the temperature value[/green]")
            try:
                temp = float(temp)
                if choice == '1':
                    result = celsius_to_fahrenheit(temp)
                    console.print(Panel(f"[bold green]✔ {temp}°C is {result:.2f}°F[/bold green]", expand=False))
                else:
                    result = fahrenheit_to_celsius(temp)
                    console.print(Panel(f"[bold green]✔ {temp}°F is {result:.2f}°C[/bold green]", expand=False))
            except ValueError:
                console.print(Panel("[bold red]✖ Invalid input. Please enter a numeric value.[/bold red]", expand=False))
        else:
            console.print(Panel("[bold red]✖ Invalid choice. Please enter 1, 2, or 'exit'.[/bold red]", expand=False))

if __name__ == "__main__":
    main()
