# Berkontribusi

Terima kasih sudah ingin membantu. Repo ini adalah arsip dokumentasi, jadi prinsip utamanya: **jangan mengubah makna dokumentasi asli**.

## Yang bisa dikontribusikan

- Memperbaiki typo, format Markdown, atau tautan yang rusak.
- Menambahkan contoh pemakaian yang jelas dan sudah diuji.
- Memperbaiki ringkasan di indeks agar lebih mudah dipahami.
- Menambahkan terjemahan penjelasan (bukan mengganti teks asli).
- Melaporkan halaman yang hilang atau gambar yang tidak tampil.

## Yang tidak boleh

- Mengunggah APK, file Premium, atau materi berhak cipta baru.
- Mengubah teks dokumentasi asli sehingga berbeda makna.
- Menghapus atribusi, front matter, atau tautan ke arsip.
- Mengirim perubahan besar tanpa diskusi terlebih dahulu.

## Alur kontribusi

1. Fork repo ini.
2. Buat branch dengan nama yang jelas, misalnya `fix/tautan-regex`.
3. Lakukan perubahan.
4. Jalankan validator:

   ```bash
   python3 scripts/validate_docs.py
   ```

5. Commit dengan pesan singkat, lalu buka pull request.
6. Jelaskan apa yang diubah dan, kalau relevan, tautkan issue terkait.

## Aturan penulisan

- Gunakan Markdown standar GitHub.
- Pertahankan front matter di setiap halaman dokumentasi:
  `title`, `source`, `archived`, `archive_url`, `category`.
- Jangan menambahkan `content_from` kecuali halaman memang direkonstruksi dari katalog gabungan.
- Gunakan tautan relatif untuk berkas di dalam repo.
- Simpan gambar baru di `docs/assets/` dan rujuk dengan path relatif.
- Teks dokumentasi asli berbahasa Inggris. Navigasi dan penjelasan tambahan boleh berbahasa Indonesia.
- Satu pull request sebaiknya fokus pada satu topik.

## Melaporkan masalah

Gunakan template issue **Koreksi dokumentasi**. Sertakan:

- path berkas atau URL halaman;
- apa yang salah;
- usulan perbaikan (kalau ada).

Untuk masalah hak cipta, tulis jelas di issue dan sertakan bukti kepemilikan.

## Menjalankan pemeriksaan secara lokal

Validator memeriksa:

- jumlah komponen (127 trigger, 88 condition, 219 action);
- front matter pada halaman dokumentasi;
- tautan relatif yang rusak;
- gambar yang hilang;
- sisa HTML mentah atau tautan lama `*_en.html`.

Tidak ada dependensi di luar Python 3 standar.
