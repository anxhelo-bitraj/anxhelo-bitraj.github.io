// Refuse to be shown inside another site's frame (clickjacking / fake-page tricks).
// GitHub Pages can't send the X-Frame-Options header that would normally do this.
if (window.top !== window.self) {
  try {
    window.top.location.replace(window.self.location.href);
  } catch (_) {
    document.documentElement.hidden = true;
  }
}

const toast = document.querySelector('.toast');
const toastText = toast.querySelector('span');
const isTouch = matchMedia('(pointer: coarse)').matches;
let toastTimer;

function showToast(message) {
  toastText.textContent = message;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 1800);
}

// Older or locked-down browsers block the Clipboard API; a hidden textarea still works there.
function legacyCopy(text) {
  const area = document.createElement('textarea');
  area.value = text;
  area.setAttribute('readonly', '');
  area.style.cssText = 'position:fixed;top:0;left:0;opacity:0;';
  document.body.appendChild(area);
  area.select();
  const copied = document.execCommand('copy');
  area.remove();
  return copied;
}

async function copy(text, message) {
  try {
    await navigator.clipboard.writeText(text);
    showToast(message);
  } catch (_) {
    if (legacyCopy(text)) showToast(message);
    else window.prompt('Copy this:', text);
  }
}

// Phones get the native share sheet; computers get the link copied, which is what people expect there.
async function share(title, url) {
  if (isTouch && navigator.share) {
    try { await navigator.share({ title, url }); } catch (_) { /* share sheet closed */ }
    return;
  }
  copy(url, 'Link copied');
}

document.querySelectorAll('[data-action]').forEach((button) => {
  button.addEventListener('click', () => {
    const link = button.closest('.link').querySelector('a');
    if (button.dataset.action === 'copy') {
      copy(button.dataset.copy, button.dataset.done || 'Copied');
    } else {
      share(link.querySelector('.label').textContent, link.href);
    }
  });
});

// Move the glass highlight with the pointer
document.querySelectorAll('.link > a:not(.action)').forEach((link) => {
  link.addEventListener('pointermove', (event) => {
    const box = link.getBoundingClientRect();
    link.style.setProperty('--mx', `${event.clientX - box.left}px`);
    link.style.setProperty('--my', `${event.clientY - box.top}px`);
  });
});
