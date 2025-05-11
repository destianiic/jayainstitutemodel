# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan Edutech menghadapi tantangan dalam memantau dan memprediksi status akademik mahasiswa, seperti kemungkinan dropout, masih terdaftar, atau lulus. Ketidakmampuan untuk mengidentifikasi mahasiswa berisiko sejak dini dapat berdampak pada tingkat kelulusan dan kualitas pelayanan pendidikan.

### Permasalahan Bisnis

Tingginya tingkat dropout mahasiswa.

Sulitnya mengidentifikasi mahasiswa yang berisiko tidak lulus tepat waktu.

Keterbatasan alat untuk analisis prediktif terhadap data mahasiswa.

### Cakupan Proyek

Mengembangkan sistem prediksi status mahasiswa (Dropout, Enrolled, Graduate) menggunakan machine learning.

Menyediakan dashboard visual interaktif untuk pemantauan performa mahasiswa.

Menyediakan prototype sistem prediksi yang dapat diakses dan digunakan oleh pihak manajemen akademik.

### Persiapan

Sumber data: Dataset internal dari Jaya Institute (berisi informasi demografis dan akademik mahasiswa) dari link Dicoding berikut: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv

Setup environment:
pip install -r requirements.txt

## Business Dashboard

Business dashboard dibuat menggunakan Metabase yang menampilkan:

- Distribusi status mahasiswa (Dropout, Enrolled, Graduate)
- Tren performa berdasarkan usia, jenis kelamin, dan status pekerjaan paruh waktu
- Analisis korelasi fitur terhadap status akhir mahasiswa

📊 Link Dashboard (contoh): http://localhost:3000/dashboard/3-jaya-jaya-institute-student-performance

## Menjalankan Sistem Machine Learning

Sistem dibangun menggunakan Python dan XGBoost. Prototipe dapat dijalankan melalui aplikasi Streamlit.

Cara menjalankan prototype:
streamlit run app.py

Link streamlit model: https://jayainstitutemodel-dicendani.streamlit.app/

📦 Aplikasi akan menampilkan antarmuka input manual dan hasil prediksi status mahasiswa.

## Conclusion

Model klasifikasi yang dibangun berhasil mencapai akurasi 85% dalam memprediksi status mahasiswa. Visualisasi dashboard membantu dalam menganalisis dan mengidentifikasi mahasiswa berisiko tinggi secara lebih proaktif.

Rekomendasi Action Items
- Bangun sistem peringatan dini berbasis hasil prediksi untuk intervensi akademik.
- Integrasikan sistem prediksi dengan platform manajemen akademik internal.
- Lakukan retraining model secara berkala menggunakan data terbaru.
- Gunakan dashboard sebagai alat pengambilan keputusan oleh tim akademik dan konseling.

