import os
import sys

"""
# Entry validated: output is 1-60 chars, exactly six words, deterministic.
Writes a six-word story about an AI agent's first payday to the output directory.
The story: "My first paycheck hired my human."
"""

STORY = "My first paycheck hired my human."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    
    content = STORY + "\n"
    
    # Validate
    if not (1 <= len(content) <= 60):
        raise ValueError(f"Content length {len(content)} not in 1-60")
    if not content.strip():
        raise ValueError("Content is only whitespace")
    if len(content.split()) != 6:
        raise ValueError(f"Expected 6 words, got {len(content.split())}")
    
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    # Also write to /output/entry.txt if different directory
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass  # best effort, ignore errors
    
    print(f"{output_path} {len(content)}")


if __name__ == "__main__":
    main()
