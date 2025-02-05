from rich.console import Console
from rich.prompt import Prompt
from rich.panel import Panel
from rich.text import Text

def is_palindrome(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    return s == s[::-1]

def main():
    console = Console()
    console.print(Panel("[bold cyan]Palindrome Checker[/bold cyan]", expand=False))
    
    while True:
        text = Prompt.ask("[green]Enter a string (or 'exit' to quit)[/green]")
        if text.lower() == 'exit':
            console.print("[bold red]Exiting...[/bold red]")
            break
        
        if is_palindrome(text):
            console.print(Panel(f"[bold green]✔ '{text}' is a palindrome![/bold green]", expand=False))
        else:
            console.print(Panel(f"[bold red]✖ '{text}' is not a palindrome.[/bold red]", expand=False))

if __name__ == "__main__":
    main()
