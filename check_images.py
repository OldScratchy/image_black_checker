import os
import subprocess
from rich.console import Console
from rich.table import Table
import time

# Las defini a mano, pero ea
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif'}

def is_image(file_name):
    return any(file_name.lower().endswith(ext) for ext in IMAGE_EXTENSIONS)

def check_image_black(image_path):
    start_time = time.time()
    result = subprocess.run(['./image_black_checker', image_path], capture_output=True, text=True)
    end_time = time.time()
    elapsed_time = end_time - start_time
    is_black = result.stdout.strip() == '1'
    return is_black, elapsed_time

# Modificar a gusto y piacere
directory_path = '~/windows-home/demos/image_black_checker/examples'

if directory_path.startswith('~'):
    directory_path = os.path.expanduser(directory_path)

console = Console()

table = Table(title="Image Black Checker Results")
table.add_column("Image Name", justify="left", style="cyan", no_wrap=True)
table.add_column("Image Path", justify="left", style="magenta")
table.add_column("Is Black", justify="center", style="green")
table.add_column("Processing Time (s)", justify="center", style="yellow")

total_time = 0
image_count = 0

for root, _, files in os.walk(directory_path):
    for file in files:
        if is_image(file):
            image_path = os.path.join(root, file)
            is_black, elapsed_time = check_image_black(image_path)
            table.add_row(file, image_path, str(is_black), f"{elapsed_time:.6f}")
            total_time += elapsed_time
            image_count += 1

console.print(table)

# Tiempo promedio
if image_count > 0:
    average_time = total_time / image_count
    console.print(f"\nAverage processing time: {average_time:.6f} seconds ({average_time*1000:.2f} milliseconds)")
else:
    console.print("\nNo images found.")
