# Google-Doc-Table-Grid-Parser
This code fetches the HTML content from a published Google Doc URL and extracts table cell data from it. It cleans the extracted data by removing any HTML tags and then groups the cleaned cells into triples representing x-cod, characters, and y-cod. It builds a 2D grid based on the max x, y values and places each character in its correct position.

## 🚀 Features
- Extracts `<td>` data from a published Google Doc
- Parses x-coordinates, characters, and y-coordinates
- Dynamically builds and prints a visual character grid
- Skips invalid or malformed data gracefully

Install dependencies:
```bash
pip install requests

## How It Works
- You publish a Google Doc that contains an HTML-style table (with <td> cells).
- The script downloads and parses the HTML content.
- It extracts characters with associated x and y coordinates.
- The grid is built using the coordinates, and the character is placed at its correct position.
- The result is printed in the terminal.

## Content of the google doc
"https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
Check out the above link and it should be of that format or simmilar. You can also use this one. Great way of hiding some stuffs.
