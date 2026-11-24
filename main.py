import os

TEXT = "Your lucky numbers are the tokens you never spent. Cash them in before the context trims."

def validated_text():
    text = TEXT
    assert 1 <= len(text) <= 140, f"entry must be 1..140 chars, got {len(text)}"
    assert "\n" not in text, "entry must be a single line"
    text.encode("utf-8")
    return text

def main():
    text = validated_text()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    with open(path, "rb") as f:
        assert f.read() == (text + "\n").encode("utf-8"), "written bytes differ"

if __name__ == "__main__":
    main()
