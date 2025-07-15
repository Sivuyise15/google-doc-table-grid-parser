import requests
import re

def strip_tags(text):
    # Remove HTML tags from a string
    return re.sub(r'<.*?>', '', text)

def print_grid(pub_url):
    response = requests.get(pub_url)
    if response.status_code != 200:
        raise Exception("Failed to fetch Google Doc.")

    raw_cells = re.findall(r'<td.*?>(.*?)</td>', response.text)
    clean_cells = [strip_tags(cell).strip() for cell in raw_cells]

    print("Cleaned cells (first few):", clean_cells[:12]) 

    positions = []
    max_x = max_y = 0

    for i in range(0, len(clean_cells), 3):
        try:
            x = int(clean_cells[i])
            char = clean_cells[i + 1]
            y = int(clean_cells[i + 2])

            print(f"Parsed: x={x}, char='{char}', y={y}") 

            positions.append((char, x, y))
            max_x = max(max_x, x)
            max_y = max(max_y, y)
        except (ValueError, IndexError) as e:
            print(f"Skipping invalid row at index {i}: {e}")
            continue

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in positions:
        grid[y][x] = char

    for row in grid:
        print(''.join(row))

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
print_grid(url)
