import os
import time
import subprocess
from rich.console import Console
from rich.progress import track

console = Console()

def ping_google():
    console.print("[bold cyan]Memulai ping ke Google untuk stabilisasi jaringan...[/bold cyan]")
    try:
        while True:
            response = subprocess.run(["ping", "-c", "1", "8.8.8.8"], stdout=subprocess.PIPE)
            if response.returncode == 0:
                console.print("[green]Jaringan Stabil![/green]")
            else:
                console.print("[red]Koneksi Bermasalah, mencoba memperbaiki...[/red]")
                flush_dns()
            time.sleep(2)
    except KeyboardInterrupt:
        console.print("[yellow]Dihentikan oleh pengguna.[/yellow]")

def flush_dns():
    console.print("[bold magenta]Melakukan simulasi Flush DNS...[/bold magenta]")
    for _ in track(range(5), description="Flushing..."):
        subprocess.run(["ping", "-c", "1", "1.1.1.1"], stdout=subprocess.DEVNULL)
    console.print("[bold green]Flush DNS selesai![/bold green]")

def main():
    console.print("[bold blue]=== WIFI Stabilizer Tools ===[/bold blue]")
    console.print("1. Mulai Stabilisasi Jaringan (Ping Google)")
    console.print("2. Flush DNS Manual")
    console.print("3. Keluar")

    choice = input("\nPilih Menu: ")

    if choice == "1":
        ping_google()
    elif choice == "2":
        flush_dns()
    elif choice == "3":
        console.print("[bold red]Keluar...[/bold red]")
        exit()
    else:
        console.print("[bold red]Pilihan tidak valid![/bold red]")

if __name__ == "__main__":
    main()
