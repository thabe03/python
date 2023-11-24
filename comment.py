import fitz

def main(filepath: str) -> str:
    doc = fitz.open(filepath)
    highlights = [
        _parse_highlight(annot, page.get_text("words"))
        for page in doc
        for annot in page.annots()
        if annot.type[0] == 8
    ]

    return "\n".join(highlights)

def _parse_highlight(annot, wordlist) -> str:
    return " ".join(
        [
            " ".join(w[4] for w in wordlist if fitz.Rect(w[:4]).intersects(fitz.Quad(points).rect))
            for points in [annot.vertices[i : i + 4] for i in range(0, len(annot.vertices), 4)]
        ]
    )

if __name__ == "__main__":
    print(main("C:/Users/xi1le/OneDrive/Bureau/static/fichier.pdf"))
