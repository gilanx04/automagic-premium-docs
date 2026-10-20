# APK Automagic

Dua build final Automagic disediakan di [release v1.0.0](https://github.com/gilanx04/automagic-premium-docs/releases/tag/v1.0.0). File-file ini adalah build resmi yang dahulu disediakan developer di halaman download `automagic4android.com`, disalin tanpa modifikasi.

> Repo ini bukan situs resmi Automagic. APK di sini adalah mirror preservasi; tidak ada lisensi tambahan yang diberikan. Jika Anda pemegang hak cipta dan ingin file dihapus, buka issue di repo ini.

## Versi

| Properti | 1.38.0 | 1.37.0 |
| --- | --- | --- |
| Keterangan | Versi terbaru dengan penyesuaian Android 10 | Versi Google Play terakhir, tanpa license check |
| Nama file | `Automagic_1_38_0.apk` | `Automagic_1_37_0.apk` |
| Ukuran | 8.729.769 byte (8,73 MB) | 8.529.838 byte (8,53 MB) |
| `versionCode` | 4900 | 4800 |
| `minSdkVersion` | 14 (Android 4.0) | 14 (Android 4.0) |
| `compileSdkVersion` | 29 (Android 10) | 28 (Android 9) |
| Paket | `ch.gridvision.ppam.androidautomagic` | `ch.gridvision.ppam.androidautomagic` |
| Penanda tangan | Gridvision Engineering GmbH | Gridvision Engineering GmbH |

### Unduh

- [Automagic_1_38_0.apk](https://github.com/gilanx04/automagic-premium-docs/releases/download/v1.0.0/Automagic_1_38_0.apk)
- [Automagic_1_37_0.apk](https://github.com/gilanx04/automagic-premium-docs/releases/download/v1.0.0/Automagic_1_37_0.apk)
- [SHA256SUMS](https://github.com/gilanx04/automagic-premium-docs/releases/download/v1.0.0/SHA256SUMS)

### Checksum

```text
73700c9757a7419aa7052175a388af9f8ed3981500e3423fd76354304ddb9556  Automagic_1_37_0.apk
f3067405c527febcb3751ce08d06edd4455a6377baf1136ca49e015ed2b37518  Automagic_1_38_0.apk
```

Verifikasi setelah mengunduh:

```bash
sha256sum -c SHA256SUMS
```

GitHub juga menampilkan digest SHA-256 untuk setiap aset release. Nilainya harus sama dengan daftar di atas.

## Keaslian build

Kedua APK ditandatangani dengan sertifikat yang sama:

```text
CN=gridvision engineering GmbH, OU=Development,
O=gridvision engineering GmbH, L=Aarau, C=CH

SHA-256 sertifikat:
217c58b90200af2e23b542884b2cbec89f9b220b15e92eb6007e3e60a069809e
```

Pemeriksaan cepat:

```bash
apksigner verify --print-certs Automagic_1_38_0.apk
aapt2 dump badging Automagic_1_38_0.apk | head -3
```

## Sumber resmi

Halaman download resmi masih dapat dibaca dan menyebutkan kedua file:

> Automagic is not maintained anymore and is no longer available on Google Play.
>
> Newest version with adjustments for Android 10: **Automagic_1_38_0.apk**
>
> Last Google Play version (without license check): **Automagic_1_37_0.apk**

- Halaman asli: <https://automagic4android.com/download_en.html>
- Arsip Wayback (23 September 2020): <https://web.archive.org/web/20200923024045/https://automagic4android.com/download_en.html>

## Cara memasang

1. Aktifkan **Install unknown apps** / **Sumber tidak dikenal** untuk aplikasi yang akan membuka APK (file manager atau browser).
2. Unduh APK yang dipilih.
3. Buka notifikasi unduhan atau file manager, lalu pilih APK tersebut.
4. Jika tombol instal tidak merespons, matikan sementara aplikasi yang menampilkan overlay.
5. Setelah selesai, Anda bisa menonaktifkan kembali izin sumber tidak dikenal.

## Catatan kompatibilitas

- Automagic berhenti dikembangkan pada 2020. Build 1.38.0 adalah versi terakhir yang mendapat penyesuaian untuk Android 10.
- Di Android 11 ke atas, pembatasan penyimpanan, izin latar belakang, dan perubahan kebijakan lainnya bisa membuat sebagian fitur tidak berfungsi.
- Beberapa action membutuhkan **root**, **device owner**, **accessibility service**, atau izin khusus lain.
- Tidak ada jaminan build ini berjalan di semua perangkat atau ROM. Uji dahulu pada perangkat yang tidak dipakai untuk pekerjaan penting.

## Kenapa 1.37 dan 1.38?

- **1.38.0** adalah versi terbaru yang disiapkan developer untuk Android 10, dengan beberapa fitur baru.
- **1.37.0** adalah versi terakhir yang pernah ada di Google Play. Developer merilisnya tanpa license check setelah aplikasi ditarik dari Play Store.

Untuk pemakaian baru, mulai dari **1.38.0**. Simpan **1.37.0** sebagai cadangan bila ada perangkat lama yang lebih cocok dengan versi Play Store.

---

[← Peta dokumentasi](README.md) · [FAQ](faq.md) · [README utama](../README.md)
