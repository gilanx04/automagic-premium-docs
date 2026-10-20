# Automagic Premium — Arsip Dokumentasi

**Dokumentasi lengkap Automagic Premium untuk Android, dipulihkan dari Wayback Machine dan disusun ulang sebagai Markdown yang rapi.**

![Status](https://img.shields.io/badge/status-arsip%20tidak%20resmi-blue)
![Komponen](https://img.shields.io/badge/komponen-434-brightgreen)
![Panduan](https://img.shields.io/badge/panduan-4-informational)
![Referensi](https://img.shields.io/badge/referensi-6-informational)

> Automagic sudah tidak dikembangkan dan tidak lagi tersedia di Google Play. Halaman bantuan resminya di `automagic4android.com` sekarang banyak yang 404. Repo ini menyimpan dokumentasi yang masih bisa dipulihkan agar tetap bisa dibaca, dicari, dan dipelajari.

## Daftar isi

- [Automagic dalam 30 detik](#automagic-dalam-30-detik)
- [Mulai cepat](#mulai-cepat)
- [Unduh APK final](#unduh-apk-final)
- [Isi dokumentasi](#isi-dokumentasi)
- [Struktur repo](#struktur-repo)
- [Jalur belajar](#jalur-belajar)
- [Cara mencari](#cara-mencari)
- [Kompatibilitas Android](#kompatibilitas-android)
- [Sumber dan metode pemulihan](#sumber-dan-metode-pemulihan)
- [Kontribusi](#kontribusi)
- [Lisensi dan hak cipta](#lisensi-dan-hak-cipta)

## Automagic dalam 30 detik

Automagic adalah aplikasi otomasi Android berbasis **flow**. Nama lengkapnya **Automagic Premium**, dan versi final 1.37.0 serta 1.38.0 disediakan developer sebagai download resmi. Satu flow terdiri dari tiga jenis komponen:

| Komponen | Peran | Contoh |
| --- | --- | --- |
| **Trigger** | Memulai flow saat peristiwa terjadi | Baterai turun di bawah 20%, WiFi tersambung, jam 07:00 |
| **Condition** | Memeriksa keadaan dan memilih cabang true/false | Apakah sedang mengisi daya? Apakah hari ini Senin? |
| **Action** | Melakukan sesuatu | Matikan WiFi, kirim notifikasi, jalankan script |

Flow bisa memakai **variabel** untuk membawa data antar komponen, misalnya `{triggertime}` atau `{battery_level}`. Dengan menggabungkan ketiganya, Anda bisa membuat otomasi seperti “matikan WiFi saat baterai rendah” atau “kirim notifikasi jam 7 pagi berisi cuaca”.

## Mulai cepat

| Kebutuhan | Buka |
| --- | --- |
| Baru pertama kali mengenal Automagic | [Konsep Dasar](docs/guides/base-concepts.md) |
| Ingin langsung membuat flow | [Membuat Flow Pertama](docs/guides/creating-the-first-flow.md) |
| Ingin membuat widget sendiri | [Membuat Widget Kustom](docs/guides/creating-a-custom-widget.md) |
| Mencari trigger | [Indeks Trigger](docs/components/triggers/README.md) |
| Mencari condition | [Indeks Condition](docs/components/conditions/README.md) |
| Mencari action | [Indeks Action](docs/components/actions/README.md) |
| Butuh sintaks regex atau format tanggal | [Referensi](docs/reference/README.md) |
| Ingin membaca semua komponen sekaligus | [Katalog gabungan](docs/components/all-components.md) |
| Bingung dengan istilah | [Glosarium](docs/glossary.md) |
| Punya pertanyaan umum | [FAQ](docs/faq.md) |

## Unduh APK final

Dua build final Automagic tersedia sebagai aset [release v1.0.0](https://github.com/gilanx04/automagic-premium-docs/releases/tag/v1.0.0). Keduanya adalah file resmi dari halaman download developer, disalin tanpa modifikasi.

| Versi | Keterangan | Unduh |
| --- | --- | --- |
| **1.38.0** | Versi terbaru, disesuaikan untuk Android 10 | [Automagic_1_38_0.apk](https://github.com/gilanx04/automagic-premium-docs/releases/download/v1.0.0/Automagic_1_38_0.apk) |
| **1.37.0** | Versi Google Play terakhir, tanpa license check | [Automagic_1_37_0.apk](https://github.com/gilanx04/automagic-premium-docs/releases/download/v1.0.0/Automagic_1_37_0.apk) |

Checksum, keaslian tanda tangan, sumber resmi, dan cara memasang ada di [**docs/apk.md**](docs/apk.md). Ringkasnya:

```text
73700c9757a7419aa7052175a388af9f8ed3981500e3423fd76354304ddb9556  Automagic_1_37_0.apk
f3067405c527febcb3751ce08d06edd4455a6377baf1136ca49e015ed2b37518  Automagic_1_38_0.apk
```

## Isi dokumentasi

| Bagian | Jumlah | Keterangan |
| --- | ---: | --- |
| Trigger | 127 | Pemicu flow |
| Condition | 88 | Pemeriksa keadaan dan percabangan |
| Action | 219 | Operasi yang dijalankan |
| **Komponen** | **434** | Satu halaman per komponen |
| Panduan | 4 | Konsep dasar, flow pertama, widget, layar utama |
| Referensi | 6 | Regex, format tanggal/angka, script, Doze, device owner |
| Katalog gabungan | 1 | Semua komponen dalam satu berkas |
| **Total halaman** | **445** | Belum termasuk indeks dan halaman bantuan repo |

Setiap halaman komponen memuat deskripsi, contoh, penjelasan pengaturan, dan variabel yang dihasilkan. Sebagian besar juga menyebutkan apakah komponen tersebut bagian dari versi **Premium**.

## Struktur repo

```text
automagic-premium-docs/
├── README.md                  # halaman ini
├── CONTRIBUTING.md            # cara berkontribusi
├── CHANGELOG.md               # riwayat rilis arsip
├── LICENSE                    # catatan hak cipta
├── docs/
│   ├── README.md              # peta dokumentasi
│   ├── apk.md                 # versi APK, checksum, cara pasang
│   ├── glossary.md            # istilah Automagic
│   ├── faq.md                 # pertanyaan umum
│   ├── guides/                # 4 panduan
│   ├── components/
│   │   ├── README.md          # katalog komponen
│   │   ├── all-components.md  # 434 komponen dalam satu berkas
│   │   ├── catalog.json       # metadata untuk tooling
│   │   ├── triggers/          # 127 trigger + indeks
│   │   ├── conditions/        # 88 condition + indeks
│   │   └── actions/           # 219 action + indeks
│   ├── reference/             # 6 halaman referensi
│   └── assets/                # 56 gambar lokal
├── scripts/validate_docs.py   # pemeriksa tautan dan struktur
└── .github/                   # template issue dan CI
```

## Jalur belajar

### 1. Pemula — paham dulu, praktik kemudian

1. [Konsep Dasar](docs/guides/base-concepts.md) — pahami flow, trigger, condition, action, dan variabel.
2. [Membuat Flow Pertama](docs/guides/creating-the-first-flow.md) — ikuti tutorial notifikasi setiap 5 menit.
3. [Layar Utama](docs/guides/main-screens.md) — kenali daftar flow, editor, log, dan pengaturan.

### 2. Sudah paham dasar — bangun otomasi sendiri

1. Tentukan pemicunya di [indeks trigger](docs/components/triggers/README.md).
2. Tambahkan pemeriksaan di [indeks condition](docs/components/conditions/README.md) bila perlu.
3. Pilih operasinya di [indeks action](docs/components/actions/README.md).
4. Cek nama variabel di halaman komponen, lalu pakai di teks action.
5. Uji dengan tombol **Test execute** di editor flow dan periksa **Log** bila gagal.

### 3. Referensi teknis

- [Regular Expressions](docs/reference/regular-expressions.md) untuk pencocokan teks.
- [Date Format Patterns](docs/reference/date-format-patterns.md) dan [Number Format Patterns](docs/reference/number-format-patterns.md) untuk format nilai.
- [Script Examples](docs/reference/script-examples.md) untuk mengolah variabel.
- [Device Idle / Doze Mode](docs/reference/device-idle-mode.md) bila flow berhenti saat layar mati.

## Cara mencari

**Di GitHub:**

- Tekan `/` di halaman repo, lalu ketik kata kunci.
- Gunakan pencarian dengan cakupan repo: `repo:gilanx04/automagic-premium-docs "Battery Level"`.
- Buka [all-components.md](docs/components/all-components.md) lalu `Ctrl+F`.

**Secara lokal:**

```bash
git clone https://github.com/gilanx04/automagic-premium-docs.git
cd automagic-premium-docs

# cari kata kunci di semua komponen
grep -ril "wifi" docs/components

# cari nama komponen tertentu
grep -ril "battery level" docs/components
```

**Untuk tooling:** [catalog.json](docs/components/catalog.json) berisi nama, kategori, path, dan deskripsi setiap komponen.

## Kompatibilitas Android

Dokumentasi ini berasal dari arsip 2019–2020, ketika Automagic masih aktif dikembangkan. Beberapa hal yang perlu diingat:

- Automagic dirancang untuk Android versi lama. Di Android 10 ke atas, pembatasan latar belakang, scoped storage, dan perubahan izin bisa membuat sebagian trigger/action tidak berjalan.
- Doze mode dan optimasi baterai dapat menunda atau menghentikan flow. Lihat [Device Idle / Doze Mode](docs/reference/device-idle-mode.md).
- Sebagian fitur membutuhkan akses **root**, **device owner**, **accessibility service**, atau izin khusus lain.
- Hasil bisa berbeda antar perangkat dan ROM. Tidak ada jaminan semua fitur berjalan di Android modern.

## Sumber dan metode pemulihan

Halaman bantuan asli sudah banyak yang hilang. Dokumentasi di repo ini dipulihkan dari **Wayback Machine** (Internet Archive), lalu diubah dari HTML ke Markdown.

| Bagian | Sumber arsip | Tanggal capture |
| --- | --- | --- |
| Panduan | `automagic4android.com/*_en.html` | 24 April 2019 |
| Referensi | `automagic4android.com/*_patterns_en.html`, dll. | 17 Mei 2019 |
| Katalog komponen | `components_all_en.html` | 23 September 2020 |

Karena halaman komponen individual sudah tidak dapat diakses secara stabil, **356 dari 434 halaman komponen** direkonstruksi dengan memecah katalog gabungan `components_all_en.html`. Halaman tersebut diberi penanda `content_from: components_all_en.html` di front matter. **78 halaman** yang masih bisa diambil langsung tetap memakai hasil tangkapan masing-masing.

Setiap dokumen menyimpan jejak sumbernya:

```yaml
---
title: "Trigger - Battery Level"
source: https://automagic4android.com/trigger_battery_level_en.html
archived: 2020-09-23
archive_url: https://web.archive.org/web/20200923031138/https://automagic4android.com/components_all_en.html
content_from: components_all_en.html
category: trigger
---
```

## Kontribusi

Koreksi typo, perbaikan tautan, tambahan contoh, atau terjemahan penjelasan sangat diterima. Baca [CONTRIBUTING.md](CONTRIBUTING.md) terlebih dahulu.

Cara cepat:

1. Fork repo dan buat branch baru.
2. Ubah berkas yang perlu diperbaiki.
3. Jalankan `python3 scripts/validate_docs.py`.
4. Kirim pull request dengan penjelasan singkat.

## Lisensi dan hak cipta

Ini adalah **arsip preservasi tidak resmi**, bukan proyek resmi Automagic.

- Teks dokumentasi, nama komponen, dan tangkapan layar asli tetap menjadi hak cipta pembuat Automagic.
- Indeks, navigasi, glosarium, FAQ, dan tambahan dalam bahasa Indonesia dibuat untuk repo ini.
- Materi asli disimpan untuk tujuan preservasi, pembelajaran, dan referensi. Silakan kutip dengan atribusi ke `automagic4android.com`.
- Jika Anda pemegang hak cipta dan ingin materi tertentu dihapus, buka issue agar dapat ditindaklanjuti.

Detail ada di [LICENSE](LICENSE). Repo ini tidak menyediakan lisensi atau kunci Premium. APK di release adalah mirror dari distribusi resmi developer, bukan versi modifikasi.

## Kredit

- **Automagic** dan dokumentasi aslinya — pembuat Automagic.
- **Internet Archive / Wayback Machine** — sumber pemulihan halaman.
- Para kontributor yang merapikan, memvalidasi, dan menerjemahkan navigasi.

---

Jika repo ini membantu, beri bintang agar dokumentasi Automagic tetap mudah ditemukan.
