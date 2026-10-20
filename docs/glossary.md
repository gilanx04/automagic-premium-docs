# Glosarium

Istilah yang dipakai di seluruh dokumentasi. Nama Inggris dipertahankan karena itulah yang muncul di aplikasi Automagic.

| Istilah | Arti |
| --- | --- |
| **Flow** | Satu proses otomasi lengkap. Flow berisi trigger, condition, dan action yang dijalankan sebagai satu kesatuan. |
| **Trigger** | Pemicu. Bagian yang memulai flow ketika suatu peristiwa terjadi, misalnya baterai rendah atau WiFi tersambung. Satu flow boleh punya beberapa trigger; salah satu saja sudah cukup untuk menjalankannya. |
| **Condition** | Pemeriksa keadaan. Condition menghasilkan cabang **true** atau **false**, sehingga flow bisa mengambil keputusan. |
| **Action** | Operasi yang dilakukan flow, misalnya mengirim notifikasi, mengubah volume, atau menjalankan script. |
| **Action container** | Wadah untuk mengelompokkan beberapa action di editor flow. Berguna untuk merapikan urutan dan mengatur cabang. |
| **Cabang true / false** | Dua jalur keluaran condition. Flow melanjutkan ke action yang tersambung pada cabang yang sesuai. |
| **Variabel** | Wadah nilai yang bisa berubah, misalnya `{triggertime}` atau `{battery_level}`. Variabel membuat teks dan pengaturan menjadi dinamis. |
| **Global variable** | Variabel yang namanya diawali `global_`. Nilainya bisa dipakai di semua flow dan tetap tersimpan setelah flow selesai. |
| **Ekspresi** | Perhitungan atau perbandingan yang ditulis dalam bahasa script, dipakai di condition **Expression** dan action **Script**. |
| **Placeholder** | Penulisan variabel di dalam teks, misalnya `It is {triggertime}`. Saat flow berjalan, placeholder diganti dengan nilai sebenarnya. |
| **Format variabel** | Penulisan tambahan untuk mengolah nilai, misalnya `{triggertime,dateformat,HH:mm}` untuk menampilkan jam. |
| **Flow list** | Layar utama berisi daftar flow yang dibuat, beserta status aktif/nonaktif. |
| **Flow editor** | Layar untuk menyusun trigger, condition, dan action dengan cara menambah dan menghubungkan kotak. |
| **Widget** | Tampilan kecil di layar utama Android yang bisa menampilkan informasi atau tombol dari Automagic. |
| **Overlay** | Tampilan yang muncul di atas aplikasi lain, sering dipakai untuk widget kustom atau tombol mengambang. |
| **Execution** | Satu kali flow berjalan dari trigger sampai selesai atau berhenti di suatu cabang. |
| **Log** | Catatan eksekusi flow. Berguna untuk mencari tahu mengapa flow tidak berjalan seperti yang diharapkan. |
| **Device owner** | Status administrator khusus yang memberi aplikasi izin lebih luas. Sebagian fitur Automagic membutuhkannya. |
| **Doze mode** | Mode hemat daya Android yang membatasi aktivitas latar belakang. Bisa membuat trigger atau action terlambat berjalan. |
| **Root** | Akses superuser pada Android. Sebagian action lanjutan memerlukannya, tetapi banyak otomasi dasar tidak. |
| **Premium** | Nama aplikasinya, **Automagic Premium**. Beberapa komponen ditandai **(Premium)** sebagai fitur tambahan. Versi final 1.37.0 dan 1.38.0 dirilis developer sebagai download resmi, dengan 1.37.0 tanpa license check. |

## Istilah yang sering tertukar

- **Trigger vs condition:** trigger *memulai* flow; condition *memeriksa* dan bercabang. Kalau flow harus bereaksi pada suatu peristiwa, pakai trigger. Kalau hanya perlu bertanya “apakah keadaan ini benar?”, pakai condition.
- **Condition vs action:** condition tidak mengubah apa pun; ia hanya menghasilkan true/false. Action yang melakukan perubahan.
- **Variabel vs placeholder:** variabel adalah nilainya; placeholder adalah cara menuliskannya di dalam teks.

---

[← Peta dokumentasi](README.md) · [Konsep Dasar](guides/base-concepts.md)
