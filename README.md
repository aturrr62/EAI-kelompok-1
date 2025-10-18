# EAI-kelompok-1

# JWT Marketplace API

API sederhana dengan autentikasi JWT untuk marketplace, dibangun menggunakan **Python + Flask**.

## 🚀 Cara Menjalankan

1. Clone repo ini:
   ```bash
   git clone https://github.com/aturrr62/EAI-kelompok-1.git
   cd EAI-kelompok-1

2. Buat virtual environment:
   python -m venv venv
# Windows
```
venv\Scripts\activate
```
# Linux/macOS
```
source venv/bin/activate
```
3. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
5. Buat file .env berdasarkan .env.example :
   ```
   JWT_SECRET=supersecretkey123!
   PORT=3000
   ```
7. Jalankan server:
   ```
   python app.py
   ```
   Server berjalan di: http://localhost:3000
   
🔑 Environment Variables

File .env harus berisi:

```
JWT_SECRET=your_strong_secret_here
PORT=3000
```
 

📡 Endpoint

🔓 POST /auth/login (Publik)
Login dengan kredensial demo.

Request:
```
{ "email": "user1@example.com", "password": "pass123" }
```

🔓 GET /items (Publik)
Mengembalikan daftar item marketplace.


Sukses (200):
```
{
  "items": [
    { "id": 1, "name": "Laptop", "price": 15000000 },
    { "id": 2, "name": "Mouse Wireless", "price": 150000 }
  ]
}
```
🔒 PUT /profile (Terproteksi – Butuh JWT)
Update profil user (nama atau email).


Header:
```
Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVt
YWlsIjoidXNlcjFAZXhhbXBsZS5jb20iLCJleHAiOjE3NjA1NTE0NTh9.0b_xiwyJpesIT5rKcnwt
YuKgGxScW8N1C_SZhq-c5v8"
```
Request (minimal salah satu):
```
{ "name": "Alice" }
```
Sukses (200):
```
{
  "message": "Profile updated",
  "profile": { "name": "Alice", "email": "user1@example.com" }
}
```
🧪 Contoh Pengujian (cURL)

1. Login
   ```
   curl -X POST http://localhost:3000/auth/login \ -H "Content-Type: application/json" \ -d '{"email":"user1@example.com","password":"pass123"}'
   ```
2. Akses Item (Publik)
   ```
   curl http://localhost:3000/items
   ```
3. Update Profile
   ```
   TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVt YWlsIjoidXNlcjFAZXhhbXBsZS5jb20iLCJleHAiOjE3NjA1NTE0NTh9.0b_xiwyJpesIT5rKcnwtYuKgGxScW8N1C_SZhq-c5v8"
   curl -X PUT http://localhost:3000/profile \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"name":"Nama Baru"}'
   ```
📦 Struktur Proyek
```
EAI-kelompok-1/
├── app.py                  # Kode utama Flask
├── .env.example            # Template konfigurasi
├── requirements.txt        # Dependensi Python
└── README.md               # Dokumentasi ini

```
