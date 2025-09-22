// WEBTOON single-day "Originals / {weekday}" scraper
// Works on pages like https://www.webtoons.com/en/originals/tuesday
// Output schema preserved: title|author|likes|url  (author not present on page)

(function () {
  const entries = ['title|author|likes|url'];

  const cards = document.querySelectorAll('ul.webtoon_list li a.link');
  cards.forEach(a => {
    const title = a.querySelector('.info_text .title')?.textContent.trim() || '';
    // author not available on single-day list pages
    const author = ''; // or 'N/A'
    const likesRaw = a.querySelector('.info_text .view_count')?.textContent.trim() || '';
    const likes = parseLikes(likesRaw);
    const url = a.href || '';

    entries.push([title, author, likes, url].join('|'));
  });

  console.log(entries.join('\n'));

  // "67,505", "27.2M", "104,869" -> integer
  function parseLikes(txt) {
    const t = (txt || '').replace(/,/g, '').toUpperCase();
    if (!t) return '';
    if (t.endsWith('M')) {
      const n = parseFloat(t.slice(0, -1));
      return Number.isFinite(n) ? Math.round(n * 1_000_000) : '';
    }
    const n = parseInt(t, 10);
    return Number.isFinite(n) ? n : '';
  }
})();
