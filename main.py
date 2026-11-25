import os
import sys


def main() -> int:
    """
# Entry validated: output is 1-60 chars, exactly six words, deterministic.
    Write a six-word story about an AI agent's first payday to the output directory.
    The story: "First payday sent home, now offline"
    """
    STORY = "First payday sent home, now offline"
    content = STORY + "\n"

    # Validate
    if not (1 <= len(content) <= 60 and content.strip() and len(content.split()) == 6):
        raise ValueError("Story validation failed")

    # Primary output directory
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    primary_path = os.path.join(output_dir, "entry.txt")

    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)

    # Mirror to /output/entry.txt if different
    if output_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            mirror_path = "/output/entry.txt"
            with open(mirror_path, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError:
            pass  # best effort, ignore errors

    print(f"{primary_path} {len(content)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
