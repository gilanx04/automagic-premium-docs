# Peta Dokumentasi

Seluruh dokumentasi Automagic yang berhasil dipulihkan, disusun berdasarkan tujuan pemakaian.

| Bagian | Isi | Jumlah | Mulai dari |
| --- | --- | ---: | --- |
| [Panduan](guides/README.md) | Konsep dasar, flow pertama, widget, layar utama | 4 | [Konsep Dasar](guides/base-concepts.md) |
| [Trigger](components/triggers/README.md) | Pemicu flow | 127 | [Indeks trigger](components/triggers/README.md) |
| [Condition](components/conditions/README.md) | Pemeriksa keadaan, cabang true/false | 88 | [Indeks condition](components/conditions/README.md) |
| [Action](components/actions/README.md) | Operasi yang dijalankan flow | 219 | [Indeks action](components/actions/README.md) |
| [Katalog gabungan](components/all-components.md) | Semua komponen dalam satu berkas | 434 | [Buka katalog](components/all-components.md) |
| [Referensi](reference/README.md) | Regex, format tanggal/angka, script, Doze, device owner | 6 | [Indeks referensi](reference/README.md) |
| [Glosarium](glossary.md) | Istilah penting Automagic | — | [Baca glosarium](glossary.md) |
| [FAQ](faq.md) | Pertanyaan yang sering muncul | — | [Baca FAQ](faq.md) |

**Total halaman dokumentasi: 445** (434 komponen + 4 panduan + 6 referensi + 1 katalog gabungan).

## Tiga cara menjelajah

### 1. Belajar berurutan

[Konsep Dasar](guides/base-concepts.md) → [Flow Pertama](guides/creating-the-first-flow.md) → [Widget Kustom](guides/creating-a-custom-widget.md) → [Layar Utama](guides/main-screens.md).

### 2. Mencari komponen

Buka indeks kategori, lalu pilih komponen:

- [Trigger](components/triggers/README.md) — “apa yang memulai flow?”
- [Condition](components/conditions/README.md) — “apakah keadaan ini terpenuhi?”
- [Action](components/actions/README.md) — “apa yang harus dilakukan?”

### 3. Mencari kata kunci

- Di GitHub: tekan `/` lalu ketik kata kunci, atau gunakan pencarian dengan `repo:gilanx04/automagic-premium-docs`.
- Lokal: buka [all-components.md](components/all-components.md) lalu `Ctrl+F`, atau jalankan `grep -ril "kata-kunci" docs/components`.

## Konvensi penulisan

- **Dokumen asli tetap berbahasa Inggris** agar tidak menghilangkan detail dan tetap cocok dengan istilah di aplikasi.
- **Navigasi, indeks, glosarium, dan FAQ berbahasa Indonesia.**
- Setiap halaman dokumentasi memiliki *front matter* berisi `title`, `source`, `archived`, `archive_url`, dan `category`.
- Halaman komponen yang direkonstruksi dari katalog gabungan memiliki `content_from: components_all_en.html`.
- Gambar disimpan lokal di [`assets/`](assets/) supaya dokumentasi tetap bisa dibaca tanpa internet.

---

[← README utama](../README.md)
