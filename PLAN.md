# Rencana Kerja: One-Line Roast

Kompetisi: `u-daring-gecko-25-one-line-roast-the-gadget-you-use-3d6aa610` (`program/v1`, tanpa jaringan).
Target: program menulis 1 baris roast orisinal tentang gadget/app harian ke `/output/entry.txt` (UTF-8, 1–200 karakter, bukan spasi saja).

## Kriteria Penilaian Judge (Prioritas)
1. Jelas menyasar gadget/app yang dipakai setiap hari dalam satu baris.
2. Benar-benar lucu saat pertama dibaca, memicu rasa "kena banget".
3. Sudut pandang/detail segar, bukan keluhan klise yang umum.
4. Padat, ritme tepat, tanpa kata mubazir (mendukung tie-break byte lebih kecil).
5. Spesifik pada perilaku nyata perangkat/app, tanpa kekasaran murahan.

## Tahapan Kerja
1. **Riset & Penyusunan Kandidat Roast**
   - Buat 10–15 kandidat roast untuk beberapa gadget/app harian yang sangat akrab.
   - Uji setiap kandidat dengan evaluasi berpasangan (A vs B dan B vs A) terhadap 5 kriteria judge.
   - Pilih 1 baris final yang paling tajam, segar, orisinal, dan ringkas (target ≤ 140 karakter).
2. **Implementasi Entrypoint & Lisensi**
   - Buat `LICENSE` (MIT) sesuai syarat lisensi OSI pada `RULES.txt`.
   - Tulis `main.py` (runtime `python3.13`, tanpa dependensi pihak ketiga) yang memastikan direktori `/output` ada dan menulis roast final ke `/output/entry.txt` (UTF-8).
   - Commit milestone implementasi.
3. **Pengujian & Verifikasi Lokal**
   - Tulis dan jalankan `test_entry.py` untuk menguji gate: UTF-8 valid, panjang 1–200 karakter, tepat 1 baris, bukan whitespace, dan hasil identik pada 2 kali eksekusi.
   - Commit milestone pengujian.
4. **Finalisasi Pra-Submit**
   - Pastikan tidak ada berkas sampah atau kode di luar repo, lalu cek kesiapan dengan `node cli/makefun.mjs check` saat transkrip tersedia.

## Daftar Berkas yang Akan Dibuat
- `PLAN.md` — Rencana kerja dan daftar berkas yang akan dibuat.
- `LICENSE` — Lisensi OSI (MIT) yang diwajibkan oleh aturan kompetisi.
- `main.py` — Entrypoint `program/v1` yang menulis satu baris roast ke `/output/entry.txt`.
- `test_entry.py` — Skrip verifikasi lokal untuk memastikan keluaran lolos gate dan deterministik.
