# Nuvora.webdev

Website resmi Nuvora.webdev yang dibangun sebagai proyek statis multi-halaman dengan HTML, CSS, dan JavaScript vanilla. Arah visualnya adalah **Luminous Systems**: ruang gelap yang tenang, kaca transparan dengan cahaya ungu, dan aksen lime yang berfungsi sebagai sinyal.

## Yang sudah dibangun

Website memiliki homepage dengan floating navbar, hero cinematic, panel glassmorphism utama, empat benefit hero yang disetujui, introduction, services, pricing, extras, portfolio preview, work process, about, FAQ, final CTA, dan footer. Halaman pendukung tersedia untuk portfolio, privacy policy, thank-you, custom 404, dan padanan bahasa Inggris.

Sistem bahasa tersentralisasi berada di `assets/js/translations.js`. Bahasa Indonesia menjadi default dan English tersedia melalui language switcher. Preferensi disimpan di `localStorage` dengan key `nuvora-lang`. Konten layanan, paket, extras, dan portfolio berada pada data terpusat di `assets/js/content.js`; portfolio dimulai dengan empty state karena tidak ada proyek terverifikasi di brief.

CTA kontak menggunakan WhatsApp dengan nomor internasional `6285196322176` dan pesan sesuai konteks, email `nuvorawebdev@gmail.com`, serta Instagram `@nuvora.webdev`. Tidak ada form palsu atau backend fiktif.

## Struktur direktori

```text
nuvora/
├── index.html
├── portfolio/index.html
├── privacy-policy/index.html
├── thank-you/index.html
├── 404.html
├── en/index.html
├── en/portfolio/index.html
├── en/privacy-policy/index.html
├── en/thank-you/index.html
├── assets/
│   ├── css/style.css
│   ├── css/responsive.css
│   ├── css/animations.css
│   ├── js/content.js
│   ├── js/translations.js
│   ├── js/language.js
│   ├── js/navigation.js
│   ├── js/portfolio.js
│   ├── js/interactions.js
│   ├── js/main.js
│   └── images/
│       ├── nuvora-logo.png
│       ├── nuvora-mark.png
│       ├── hero-background.jpg
│       └── portfolio/
├── manifest.webmanifest
├── manus-routes.json
├── robots.txt
├── sitemap.xml
├── .htaccess
├── package.json
├── plan.md
└── TODO.md
```

## Logo resmi

Logo dari arsip pengguna sudah ditempatkan di `assets/images/nuvora-logo.png` dan dipakai di navbar serta footer. File `assets/images/nuvora-mark.png` juga dipertahankan sebagai aset mark untuk favicon dan manifest. Jika ingin mengganti logo, pertahankan nama file `nuvora-logo.png`, format PNG transparan, dan aspect ratio asli.

## Preview lokal

Dari folder project, jalankan:

```bash
python3 -m http.server 3000
```

Lalu buka `http://localhost:3000/`. Untuk menghentikan server, tekan `Ctrl+C`.

Alternatif melalui npm script:

```bash
npm run serve
```

## Deployment

Project ini tidak membutuhkan dependency build. Upload seluruh folder ke static hosting yang mendukung `index.html` dan folder route. Pastikan konfigurasi hosting melayani `404.html` sebagai fallback dan menjaga file `robots.txt` serta `sitemap.xml` pada root domain. `.htaccess` disertakan sebagai opsi untuk Apache.

Sebelum deployment publik, ganti domain canonical, Open Graph, sitemap, dan URL di `assets/js/translations.js` bila domain final berbeda dari `https://nuvorawebdev.site`.

## Aset visual

`assets/images/hero-background.jpg` adalah aset lokal bernuansa abstract neon dari hasil pencarian Pexels, dipilih agar mendukung atmosfer gelap, ungu, dan refleksi cahaya pada hero. Screenshot portfolio asli dari tiga demo resmi disimpan di `assets/images/portfolio/` sebagai `west-coffee.webp`, `drasa-restaurant.webp`, dan `assyifa-dental-clinic.webp`.

## Data resmi yang sudah diterapkan

Pricing Starter, Growth, dan Business; seluruh Extras; tujuh tahap proses; aturan pembayaran 40/60; estimasi timeline; FAQ; dan tiga demo website resmi sudah tersentralisasi di `assets/js/translations.js`. Portfolio menggunakan screenshot lokal yang diambil dari URL demo resmi dan CTA membuka URL sumber dengan `target="_blank"` serta `rel="noopener noreferrer"`.

Sebelum go-live, tinjau kembali tanggal pada privacy policy dan pastikan domain canonical `https://nuvorawebdev.site` sudah aktif. Website tidak mengklaim hosting termasuk, ranking SEO, booking otomatis, SLA, client result, atau legal credentials yang tidak tersedia.
