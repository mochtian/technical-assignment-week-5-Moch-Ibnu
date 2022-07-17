import time #library untuk meng-import modul waktu.
import board #library untuk meng-import pin GPIO raspberry.
import adafruit_dht #Reference khusus sensor DHT.
import psutil #library untuk mengambil informasi tentang proses yang sedang berjalan.

for proc in psutil.process_iter(): # Kembalikan iterator yang menghasilkan instance kelas Proses untuk semua proses yang berjalan di mesin lokal.
	if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
		proc.kill() #perintah menghentikan proses.
sensor = adafruit_dht.DHT11(board.D23) #menentukan tipe sensor dan pin yang digunakan pada raspberry.
while True: #perintah berjalan pada kondisi apa pun sampai keadaan break dalam loop di eksekusi.
	try:
		temp = sensor.temperature #membaca nilai suhu dari sensor.
		humidity = sensor.humidity #membaca nilai kelembaban dari sensor.
		print("Temperature: {}*C   Humidity: {}% ".format(temp, humidity)) #mencetak hasilnya di layar. Mempertimbangkan akurasi sensor yang terbatas, hasilnya diformat tanpa desimal.
	except RuntimeError as error: #menangani error apabila terdapat kesalahan pada saat runtime.
		print(error.args[0]) #mencetak hasil error.
		time.sleep(2.0) #hasil ditampilkan setiap 2 detik.
        	continue #sensor akan terus membaca.
	except Exception as error: #mendeteksi kesalahan selama dieksekusi.
		sensor.exit() #fungsi untuk keluar tanpa peruntah
		raise error #digunakan untuk membangkitkan ekspesi ketika kondisi error.
	time.sleep(2.0) #hasil ditampilkan setiap 2 detik.
