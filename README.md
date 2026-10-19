# anxhelo-bitraj.github.io

My personal links page: GitHub, LinkedIn, email, WhatsApp and a "Save contact" card, all on one page.

**Live at https://anxhelo-bitraj.github.io**

It's a single static HTML file served free by [GitHub Pages](https://pages.github.com/) straight from the `main` branch of this repo. There's no build step, framework or server. Every push to `main` goes live in about a minute.

## What's in here

| File | What it is |
| --- | --- |
| `index.html` | The whole page: HTML, CSS and a little JS for the share buttons |
| `photo.jpg` | Profile photo (600×600). Also used as the favicon and the link-preview image |
| `icons/` | The GitHub, LinkedIn, Outlook and WhatsApp icons |
| `contact.vcf` | vCard 3.0 contact card with the photo embedded. The "Save contact" button downloads it |
| `tools/make_vcard.py` | Rebuilds `contact.vcf` from the details at the top of the script |
| `.nojekyll` | Tells GitHub Pages to serve the files as they are, without running Jekyll |

## Changing a link

1. Open `index.html` and find the block between
   `<!-- EDIT YOUR DETAILS HERE -->` and `<!-- END OF YOUR DETAILS -->`.
2. Change the `href="…"` of the link you want (and the visible text, if needed).
   - WhatsApp links use `https://wa.me/<country code + number, digits only>`, e.g. `https://wa.me/447447705513`.
3. If the same detail is in your contact card (email, phone, LinkedIn, GitHub), also change it at the top of `tools/make_vcard.py` and run:
   ```bash
   python3 tools/make_vcard.py
   ```
4. Check it locally (optional): `python3 -m http.server` and open http://localhost:8000
5. Publish:
   ```bash
   git add -A
   git commit -m "Update LinkedIn link"
   git push
   ```
6. Wait about a minute and refresh https://anxhelo-bitraj.github.io. If you still see the old version, hard-refresh with Cmd+Shift+R.

## Adding a new link

Copy one whole `<li class="link">…</li>` block inside the edit block, paste it where you want the new button, then change the `href`, the icon `src` and the label. Put a square icon (around 192×192) in `icons/`.

## Replacing the photo

Save the new photo as `photo.jpg`, square and about 600×600. Then run `python3 tools/make_vcard.py` so the contact card picks it up, and commit and push as above.

## The QR code

The QR code points to `https://anxhelo-bitraj.github.io`. That URL never changes when you edit the page, so printed QR codes keep working. The QR files are kept out of git on purpose (see `.gitignore`).
