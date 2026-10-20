# Katalog Komponen

Dokumentasi lengkap **434 komponen** Automagic: **127 trigger**, **88 condition**, dan **219 action**. Setiap komponen punya halaman sendiri yang menjelaskan fungsi, contoh pemakaian, pengaturan, dan variabel yang dihasilkan.

| Kategori | Jumlah | Indeks | Baca sekaligus |
| --- | ---: | --- | --- |
| Trigger | 127 | [Indeks trigger](triggers/README.md) | [Bagian trigger](all-components.md#triggers) |
| Condition | 88 | [Indeks condition](conditions/README.md) | [Bagian condition](all-components.md#conditions) |
| Action | 219 | [Indeks action](actions/README.md) | [Bagian action](all-components.md#actions) |
| **Total** | **434** | | [Katalog gabungan](all-components.md) |

## Cara membaca halaman komponen

Sebagian besar halaman disusun dengan pola yang sama:

- **Paragraf pembuka** — apa yang dilakukan komponen dan kapan dipakai.
- **Examples** — contoh nyata penggunaan komponen.
- **Settings** — setiap opsi konfigurasi beserta artinya.
- **Variables** — nilai yang bisa dipakai di action lain, misalnya `{triggertime}`.

Nama variabel ditulis dengan kurung kurawal, misalnya `{battery_level}`. Saat dipakai di teks action, variabel akan diganti dengan nilainya ketika flow berjalan.

## Triggers

Trigger memulai flow saat sebuah peristiwa terjadi. Ada 127 trigger, dari waktu dan lokasi sampai perubahan jaringan, sensor, dan notifikasi.

[Lihat daftar lengkap trigger →](triggers/README.md)

## Conditions

Condition memeriksa keadaan dan menentukan cabang **true** atau **false**. Ada 88 condition, termasuk pemeriksaan baterai, jaringan, waktu, variabel, dan ekspresi.

[Lihat daftar lengkap condition →](conditions/README.md)

## Actions

Action melakukan operasi: mengubah setelan, mengirim pesan, menjalankan script, mengatur widget, dan banyak lagi. Ada 219 action.

[Lihat daftar lengkap action →](actions/README.md)

## Katalog gabungan dan data mesin

- [**all-components.md**](all-components.md) — seluruh 434 komponen dalam satu berkas, cocok untuk pencarian cepat dengan `Ctrl+F` atau `grep`.
- [**catalog.json**](catalog.json) — metadata komponen (nama, kategori, path, deskripsi) untuk dipakai oleh tooling atau situs statis.

---

[← Peta dokumentasi](../README.md) · [README utama](../../README.md)
