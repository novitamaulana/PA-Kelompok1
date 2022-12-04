import sklearn
from flask import Flask, render_template, request
from model import load, recommendations, recommendations_lembaga

app = Flask(__name__)

# load model dan scaler
load()

@app.route('/')
def home():
    return render_template('rs.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/predict', methods=["post"])
def predict():
        # menangkap data yang diinput user melalui form
        nama = (request.form['nama'])
        jenis_kelamin = (request.form['jenis_kelamin'])
        umur = (request.form['umur'])  
        provinsi = (request.form['provinsi'])
        jenis_kekerasan = (request.form['jenis_kekerasan'])
        jenis_lembaga = (request.form['jenis_lembaga'])

        # melakukan prediksi menggunakan model yang telah dibuat
        #data = [[jenis_kelamin, umur, provinsi, jenis_kekerasan, jenis_lembaga]]
        index, nama_lembaga, jenis_lembaga, profile_lembaga, provinsi, alamat, kontak, jenis_kelamin, umur, jenis_kekerasan = recommendations(jenis_lembaga, provinsi, jenis_kelamin, umur, jenis_kekerasan)
        rekomendasi = recommendations_lembaga(index, number_of_recommendations=1)
        return render_template('rs.html', hasil_alamat=alamat, hasil_nama=nama_lembaga, hasil_kontak=kontak, rekom=rekomendasi)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)