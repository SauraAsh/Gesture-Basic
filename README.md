# Gesture Basic - Control Mouse with Hand Gestures

Projek ini memungkinkan Anda untuk mengontrol kursor mouse di komputer menggunakan gerakan tangan (hand gestures) melalui webcam.

## 🚀 Fitur & Gestur

1. **Menggerakkan Kursor (Move Cursor):**
   - **Gestur:** Angkat/Tegakkan jari telunjuk Anda (pastikan ujung jari telunjuk lebih tinggi dari sendi tengahnya).
   - **Aksi:** Kursor mouse akan mengikuti pergerakan jari telunjuk Anda. Pergerakan dikalikan dengan `MULTIPLIER` agar pergerakan kecil di kamera bisa menggerakkan kursor ke seluruh layar.

2. **Klik Kiri (Click):**
   - **Gestur:** Jepit (Pinch) ujung jari telunjuk dan ujung ibu jari Anda secara bersamaan.
   - **Aksi:** Melakukan klik kiri pada mouse. Terdapat `CLICK_DELAY` untuk mencegah klik beruntun yang tidak disengaja.

3. **Berhenti / Keluar (Exit):**
   - **Gestur/Tombol:** Tekan tombol `ESC` pada keyboard Anda.
   - **Aksi:** Menutup jendela kamera dan menghentikan program.

## 🛠️ Cara Menjalankan Projek

### 1. Persiapan Awal
Pastikan Anda sudah menginstal **Python** (versi 3.7 atau lebih baru disarankan) di sistem Anda.

### 2. Buka Terminal / Command Prompt
Arahkan ke direktori projek ini:
```bash
cd D:\gemos\Gesture-Basic
```

### 3. Instalasi Dependensi
Instal semua pustaka (libraries) yang dibutuhkan dengan menjalankan perintah berikut:
```bash
pip install -r requirements.txt
```
*(Ini akan menginstal `opencv-python`, `mediapipe`, dan `pyautogui`)*

### 4. Jalankan Aplikasi
Eksekusi script utama dengan perintah:
```bash
python gesture_basic.py
```
*(Lampu webcam Anda akan menyala, dan jendela pratinjau kamera akan muncul. Anda sudah bisa mulai mengontrol kursor dengan gerakan tangan!)*

## ⚙️ Konfigurasi Tambahan
Jika Anda ingin menyesuaikan pergerakan atau sensitivitas, Anda dapat mengubah nilai variabel berikut di bagian atas file `gesture_basic.py`:
- `MULTIPLIER`: Mengatur seberapa sensitif jarak kursor dengan pergerakan tangan (default: 8.0).
- `SMOOTH`: Mengatur seberapa halus pergerakan kursor (default: 0.25).
- `CLICK_DELAY`: Jeda waktu minimal antar klik otomatis (default: 0.5 detik).