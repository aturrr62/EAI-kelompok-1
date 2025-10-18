# JWT Marketplace API

API sederhana dengan autentikasi **JWT (JSON Web Token)** untuk simulasi marketplace, dibangun menggunakan **Python** dan *web framework* **Flask**.

***

## ✨ Fitur Utama

Proyek ini mengimplementasikan mekanisme JWT untuk melindungi *endpoint* tertentu.

* **Autentikasi JWT**: Menggunakan *decorator* `jwt_required` untuk memverifikasi token pada *endpoint* yang terproteksi.
* **Login (`POST /auth/login`)**: *Endpoint* publik untuk mendapatkan token akses dengan kredensial demo (`user1@example.com`/`pass123`).
* **Lihat Item (`GET /items`)**: *Endpoint* publik untuk mengambil data produk.
* **Perbarui Profil (`PUT /profile`)**: *Endpoint* terproteksi yang memungkinkan pengguna mengubah nama atau email mereka.

***

## ⚙️ Teknologi yang Digunakan

* **Python**
* **Flask** (Web Framework)
* **PyJWT** (Implementasi JWT)
* **python-dotenv** (Manajemen variabel lingkungan)

***

## 🛠️ Prasyarat Instalasi

Pastikan Anda telah menginstal **Python 3.x** di sistem Anda.

1.  **Clone repositori**
    ```bash
    git clone https://github.com/aturrr62/EAI-kelompok-1.git
    cd EAI-kelompok-1
    ```

2.  **Buat dan aktifkan *virtual environment***
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Linux/macOS
    source venv/bin/activate
    ```

3.  **Install dependensi**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Konfigurasi Variabel Lingkungan**
    Buat file `.env` di root proyek dengan menyalin konten dari `.env.example`.
    ```bash
    cp .env.example .env
    ```
    Edit file `.env` dan ganti `your_strong_secret_here` dengan secret key yang kuat untuk `JWT_SECRET`.

5.  **Jalankan server**
    ```bash
    python app.py
    ```
    Server akan berjalan di: `http://localhost:3000` (default)

***

## 📂 Susunan Proyek
```
EAI-kelompok-1/
├── app.py                      # Kode utama aplikasi Flask, termasuk endpoints dan fungsi JWT.
├── .env.example                # Template untuk variabel lingkungan (JWT_SECRET, PORT).
├── requirements.txt            # Daftar dependensi Python (Flask, PyJWT, dsb.).
├── login.json                  # Contoh request body untuk /auth/login.
├── update.json                 # Contoh request body untuk /profile.
└── README.md                   # Dokumentasi proyek (file ini).

```
***

## 🚀 Contoh Penggunaan (cURL)

Gunakan kredensial demo: `email`: `user1@example.com`, `password`: `pass123`.

### 1. Login dan Dapatkan Token

```bash
curl -X POST http://localhost:3000/auth/login \
-H "Content-Type: application/json" \
-d '{"email":"user1@example.com","password":"pass123"}
```
### Respons Sukses (200):
```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVtYWlsIjoidXNlcjFAZXhhbXBsZS5jb20iLCJleHAiOjE3NjA1NTE0NTh9.0b_xiwyJpesIT5rKcnwtYuKgGxScW8N1C_SZhq-c5v8"
}
```
### 2. Akses Item (Publik)
```
curl http://localhost:3000/items
```
### Respons Sukses (200):
```
{
  "items": [
    { "id": 1, "name": "Laptop", "price": 15000000 },
    { "id": 2, "name": "Mouse Wireless", "price": 150000 }
  ]
}
```
### 3. Perbarui Profil (Terproteksi)
Gunakan token yang didapatkan dari langkah Login.
```
# Ganti nilai TOKEN dengan access_token Anda
TOKEN="[TOKEN_ANDA_DI_SINI]"

curl -X PUT http://localhost:3000/profile \
-H "Authorization: Bearer $TOKEN" \
-H "Content-Type: application/json" \
-d '{"name":"Nama Pengguna Baru"}'
```
### Respons Sukses (200):
```
{
  "message": "Profile updated",
  "profile": { "name": "Nama Pengguna Baru", "email": "user1@example.com" }
}
```




