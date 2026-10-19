"""Build contact.vcf (vCard 3.0) with photo.jpg embedded.

Run from the repo root after changing a detail below or replacing photo.jpg:
    python3 tools/make_vcard.py
"""
import base64
from pathlib import Path

# ---- EDIT YOUR DETAILS HERE ----
FIRST_NAME = "Angelo"
LAST_NAME = "Bitraj"
TITLE = "Graduate Software Engineer"
EMAIL = "angelobitraj@outlook.com"
PHONE = "+44 7447 705513"
WEBSITE = "https://anxhelo-bitraj.github.io/"
LINKEDIN = "https://www.linkedin.com/in/angelo-bitraj"
GITHUB = "https://github.com/anxhelo-bitraj"
# --------------------------------

ROOT = Path(__file__).resolve().parent.parent
MAX_OCTETS = 75  # RFC 2425 5.8.1: fold lines longer than 75 octets


def escape(text):
    """Escape a vCard TEXT value (RFC 2426 section 4)."""
    return text.replace("\\", "\\\\").replace(",", "\\,").replace(";", "\\;").replace("\n", "\\n")


def fold(line):
    """Split a content line into <=75-octet pieces; continuation lines start with one space."""
    pieces, current, limit = [], b"", MAX_OCTETS
    for char in line:
        encoded = char.encode("utf-8")
        if len(current) + len(encoded) > limit:
            pieces.append(current)
            current, limit = b"", MAX_OCTETS - 1  # the leading space counts toward 75
        current += encoded
    pieces.append(current)
    return b"\r\n ".join(pieces).decode("utf-8")


def build():
    photo = base64.b64encode((ROOT / "photo.jpg").read_bytes()).decode("ascii")
    lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"N:{escape(LAST_NAME)};{escape(FIRST_NAME)};;;",
        f"FN:{escape(FIRST_NAME)} {escape(LAST_NAME)}",
        f"TITLE:{escape(TITLE)}",
        f"EMAIL;TYPE=INTERNET,PREF:{EMAIL}",
        f"TEL;TYPE=CELL,VOICE,PREF:{PHONE}",
        f"URL:{WEBSITE}",
        # itemN.X-ABLabel gives the URL a readable label in Apple Contacts; others just show the URL.
        f"item1.URL:{LINKEDIN}",
        "item1.X-ABLabel:LinkedIn",
        f"item2.URL:{GITHUB}",
        "item2.X-ABLabel:GitHub",
        f"PHOTO;ENCODING=b;TYPE=JPEG:{photo}",
        "END:VCARD",
    ]
    vcard = "\r\n".join(fold(line) for line in lines) + "\r\n"
    (ROOT / "contact.vcf").write_bytes(vcard.encode("utf-8"))
    print(f"Wrote contact.vcf ({len(vcard):,} bytes)")


if __name__ == "__main__":
    build()
