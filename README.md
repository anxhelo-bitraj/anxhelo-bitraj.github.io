# anxhelo-bitraj.github.io

My personal links page: GitHub, LinkedIn, CV, email, WhatsApp and a "Save contact" card, all on one page.

**Live at https://anxhelo-bitraj.github.io**

It's a single static HTML file served free by [GitHub Pages](https://pages.github.com/) straight from the `main` branch of this repo. There's no build step, framework or server. Every push to `main` goes live in about a minute.

The page adapts to the screen:

- **Phones (portrait):** one column, kept clear of the notch / Dynamic Island.
- **iPad portrait and tall screens:** one bigger, centred column.
- **iPad landscape, laptops, desktops and phones held sideways:** photo on the left, links on the right.

Sizes scale smoothly in between. The page is marked `noindex`, so search engines leave it out of their results and people reach it through the link or QR code.

## What's in here

| File | What it is |
| --- | --- |
| `index.html` | The whole page: HTML, CSS and a little JS for the share/copy buttons |
| `photo.jpg` | Profile photo (600×600). Used for the favicon, the link-preview image and the contact card |
| `photo-cutout.webp` | The same photo with the background removed. This is the one shown on the page |
| `Angelo_Bitraj_CV.pdf` | My CV, opened by the CV button |
| `icons/` | The GitHub, LinkedIn, CV, Outlook and WhatsApp icons |
| `contact.vcf` | vCard 3.0 contact card with the photo embedded. The "Save contact" button (top right) downloads it |
| `tools/make_vcard.py` | Rebuilds `contact.vcf` from the details at the top of the script |
| `tools/update-photo.sh` | Run after replacing `photo.jpg`: rebuilds the cut-out and the contact card |
| `tools/cutout.swift` | Removes the photo background with macOS subject lifting (used by `update-photo.sh`) |
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

## Updating the CV

Replace `Angelo_Bitraj_CV.pdf` with the new PDF, keeping **exactly the same filename**. Then commit and push. The button, the download link and anyone's saved link keep working because the URL stays the same: https://anxhelo-bitraj.github.io/Angelo_Bitraj_CV.pdf

Everything in this repo is public, so check a new CV has nothing in it you wouldn't post online, such as a home address or date of birth. Removing something from git history later is a lot harder than leaving it out.

## The small button on the right of each row

| Row | Button | What it does |
| --- | --- | --- |
| GitHub, LinkedIn | Share ↑ | Phone: opens the share sheet (AirDrop, WhatsApp, Messages…). Computer: copies the link |
| CV | Download ↓ | Downloads the PDF (tapping the row itself opens it in the browser) |
| Email | Copy | Copies the address, for people whose computer has no mail app set up |
| WhatsApp | Copy | Copies the phone number, for a normal call or text instead of WhatsApp |

Each button is set with `data-action="share"` or `data-action="copy" data-copy="text to copy"`. To remove one, delete its `<button class="action">…</button>`.

## Adding a new link

Copy one whole `<li class="link">…</li>` block inside the edit block, paste it where you want the new button, then change the `href`, the icon `src` and the label. Put a square icon (around 192×192) in `icons/`.

## Replacing the photo

Save the new photo as `photo.jpg`: square, about 600×600, with your head near the top. A plain background cuts out best. Then run:

```bash
./tools/update-photo.sh
```

That cuts you out of the background into `photo-cutout.webp` and re-embeds the photo in `contact.vcf`. It needs macOS (for subject lifting) and ImageMagick (`brew install imagemagick`). Check the page, then commit and push as above.

## The QR code

The QR code points to `https://anxhelo-bitraj.github.io`. That URL never changes when you edit the page, so printed QR codes keep working. The QR files are kept out of git on purpose (see `.gitignore`).
