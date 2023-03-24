# Zi.Care Test - Aryo nurwanto w

## 1. Technical (Membuat api) 
### CRUD Pasient Documentation

### Requirment
- Python 3
- MariaDB/Mysql
  
### Framework 
- FastAPI 
- SQLAlchemy 2.0.5 
- Elambic

### Install Requirements

```bash
$ pip3 install -r requirements.txt
```

### databse config
databse type list:
- mariadb+mariadbconnector
- mysql+mysqlconnector
edit file untuk connection DB pada file `alembic.ini`:
``` 
sqlalchemy.url = <database type>://<user>:<password>@<host>:<port>/<database name>
```

dan `server.py`:
```
engine = create_engine("<database type>://<user>:<password>@<host>:<port>/<database name>")
```

#### Database Migration
jika ingin mendeploy model structure database baru:
```
alembic revision --autogenerate -m "[message command]"
```

migrate model database:
```
alembic upgarade heads
```

#### start
jika menggunakan ubuntu pastikan terdapat `uvicorn` jika belum, jalankan command berikut :
```
sudo apt install uvicorn
```

untuk menjalan aplikasi, jalankan command berikut pada terminal:
```
uvicorn main:app --reload
```

Atau jika ingin menggunakan **docker**.

```bash
$ docker build . -t zicare
$ docker run -p 8000:8000 zicare
```

#### API Documentation
dokumntasi dapa di lihat pada : 
```
http://127.0.0.1:8000/docs
```
#

## 2. Logial
### Soal
    1. Anda memiliki 25 tamiya dan anda ingin memilih 3 tamiya tercepat. Berapa kali percobaan yang harus anda lakukan untuk bisa mendapatkan 5 tamiya tercepat yang anda miliki jika :
       1. Anda hanya memiliki 5 lintasan(hanya bisa menandingkan 5 tamiya sekaligus)
       2. Anda tidak memiliki stopwatch, alat ukur kecepatan, atau alat ukur waktu (cara menentukan hanya dengan menandingkan tamiya)
       3. Kecepatan tamiya tiap pertandingan adalah konstan/tidak berubah.
               Silahkan jawab pertanyaan dengan menyertakan penjelasannya.
### Jawaban
```
    untuk mendapatkan 3 tamia tecepat di butuh kan 6 kali percobaan sedangkan untuk 5 tamia tercepat di butuh kan 5 kali percobaan. dari 25 tamia di buat dalam 5 grup lalu lakukan 1 kali cobaan pada setiap group dan ambil satu tamia tercepat pada masing-masing grup. setelah mendapatkan tamia tercepat pada masing masing group kemudia lakukan ujicoba kembali untuk mendapaknya 3 tamia tecepat 
```