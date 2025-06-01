import subprocess
import os

# Ścieżka do twojego pliku .ipynb
notebook_path = r"C:\Users\jakub\OneDrive\Pulpit\Podstawy-Uczenia-Maszynowego\lab3\notebook.ipynb"
# Ścieżka do miejsca, gdzie chcesz zapisać plik HTML
output_path = r"C:\Users\jakub\OneDrive\Pulpit\Podstawy-Uczenia-Maszynowego\lab3\notebook_output.html"

# Komenda do konwersji
command = f"jupyter nbconvert --to html {notebook_path} --output {output_path}"

# Uruchomienie komendy w systemie
subprocess.run(command, shell=True)

print(f"Plik HTML zapisany jako: {output_path}")
