#!/bin/sh
# After replacing photo.jpg, run from the repo root:  ./tools/update-photo.sh
# 1. Cuts you out of the photo's background (macOS subject lifting) -> photo-cutout.webp, used on the page
# 2. Rebuilds contact.vcf so the contact card gets the new photo
set -e
cd "$(dirname "$0")/.."
swift tools/cutout.swift photo.jpg /tmp/photo-cutout.png
magick /tmp/photo-cutout.png -resize '600x600>' -strip -quality 88 -define webp:alpha-quality=90 photo-cutout.webp
rm /tmp/photo-cutout.png
python3 tools/make_vcard.py
echo "Done. Check the page, then commit and push."
