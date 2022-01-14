## Getting started

This application keeps track of devices. 
Using this application, 

* You can view the device list, 
![cihazListesi](https://user-images.githubusercontent.com/44245088/149583638-eed40b42-353d-444b-91da-d3d9ae0570d9.jpg)

* You can add new devices,
![cihazGiris](https://user-images.githubusercontent.com/44245088/149583615-d529385c-a69b-465c-aea9-baa263c78bc9.gif)


* Search among these devices, 
![cihazAra](https://user-images.githubusercontent.com/44245088/149583522-0d52cf66-70de-497e-85cb-a6f4a793d958.gif)


* Print reports about the work done, 
![genelAnaliz](https://user-images.githubusercontent.com/44245088/149583545-89310f97-6cc2-4cca-9204-ff94326fcb21.gif)


* View document files, 

![dokumanlar](https://user-images.githubusercontent.com/44245088/149583560-66bc4bdc-b999-4d6c-a5ec-f06fe2e1edce.gif)

* Or look in the phone book.
![telefonlar](https://user-images.githubusercontent.com/44245088/149583727-015bce60-ff40-4da0-8280-a064b0d5541f.jpg)


## Installation Options

1. Install django
```
pip install django
```
2. Install xhtml2pdf’s documentation
```
pip install xhtml2pdf
```
3. Enter the file path of the font file in the files mentioned below. It must be full path
```
toplam_ariza.html
toplam_is.html
toplam_servis.html
```

## Usage

```
Python manage.py runserver
```

```
http://127.0.0.1:8000
```
