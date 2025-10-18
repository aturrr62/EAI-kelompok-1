# EAI-kelompok-1

# JWT Marketplace API

API sederhana dengan autentikasi JWT untuk marketplace, dibangun menggunakan **Python + Flask**.

## 🚀 Cara Menjalankan

1. Clone repo ini:
   ```bash
   git clone https://github.com/aturrr62/EAI-kelompok-1.git
   cd EAI-kelompok-1
   ```

2. Buat virtual environment:
   ```bash
   python -m venv venv
   ```

3. Aktivasi virtual environment:
   
   **Windows:**
   ```cmd
   venv\Scripts\activate
   ```
   
   **Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

4. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

5. Jalankan server:
   ```bash
   python app.py
   ```
   Server berjalan di: http://localhost:3000


## 📡 Endpoint

### 🔓 POST /auth/login (Publik)
Login dengan kredensial demo.

**Request:**
```json
{ "email": "user1@example.com", "password": "pass123" }
```

### 🔓 GET /items (Publik)
Mengembalikan daftar item marketplace.

**Sukses (200):**
```json
{
  "items": [
    { "id": 1, "name": "Laptop", "price": 15000000 },
    { "id": 2, "name": "Mouse Wireless", "price": 150000 }
  ]
}
```

### 🔒 PUT /profile (Terproteksi – Butuh JWT)
Update profil user (nama atau email).

**Header:**
```
Authorization: Bearer "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVtYWlsIjoidXNlcjFAZXhhbXBsZS5jb20iLCJleHAiOjE3NjA1NTE0NTh9.0b_xiwyJpesIT5rKcnwtYuKgGxScW8N1C_SZhq-c5v8"
```

**Request (minimal salah satu):**
```json
{ "name": "Alice" }
```

**Sukses (200):**
```json
{
  "message": "Profile updated",
  "profile": { "name": "Alice", "email": "user1@example.com" }
}
```

## 🧪 Contoh Pengujian (cURL)

1. **Login:**
   ```bash
   curl -X POST http://localhost:3000/auth/login \
   -H "Content-Type: application/json" \
   -d '{"email":"user1@example.com","password":"pass123"}'
   ```

2. **Akses Item (Publik):**
   ```bash
   curl http://localhost:3000/items
   ```

3. **Update Profile:**
   ```bash
   TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImVtYWlsIjoidXNlcjFAZXhhbXBsZS5jb20iLCJleHAiOjE3NjA1NTE0NTh9.0b_xiwyJpesIT5rKcnwtYuKgGxScW8N1C_SZhq-c5v8"
   curl -X PUT http://localhost:3000/profile \
   -H "Authorization: Bearer $TOKEN" \
   -H "Content-Type: application/json" \
   -d '{"name":"Nama Baru"}'
   ```

## 📦 Struktur Proyek

```
EAI-kelompok-1/
├── app.py                  # Kode utama Flask
├── .env.example            # Template konfigurasi
├── requirements.txt        # Dependensi Python
└── README.md               # Dokumentasi ini
