def to_hm(hd):
    hm = 25/hd
    if hm > 1:
        hm = 1
    return hm

def to_vm(vd):
    vm = 1 - 0.003*abs(vd-75)
    return vm

def to_dm(vd0, vd1):
    dm = 0.82 + (4.5/(abs(vd0-vd1)))
    if dm > 1:
        dm = 1
    return dm

def to_am(asym):
    am = 1 - (0.0032*abs(asym))
    return am

def to_cm(vd0, coup):
    if vd0 < 75:
        if coup == "1":
            cm = 1
        elif coup == "2":
            cm = 0.95
        else:
            cm = 0.9
    if vd0 >= 75:
        if coup == "1" or coup == "2":
            cm = 1
        else:
            cm = 0.9
    return cm

def to_fm(vd0, freq):
    if vd0 < 75:
        if freq <= 0.2:
            fm = 1
        elif freq <= 0.5:
            fm = 0.97
        elif freq <= 1:
            fm = 0.94
        elif freq <= 2:
            fm = 0.91
        elif freq <= 3:
            fm = 0.88
        elif freq <= 4:
            fm = 0.84
        elif freq <= 5:
            fm = 0.8
        elif freq <= 6:
            fm = 0.75
        elif freq <= 7:
            fm = 0.7
        elif freq <= 8:
            fm = 0.6
        elif freq <= 9:
            fm = 0.52
        elif freq <= 10:
            fm = 0.45
        elif freq <= 11:
            fm = 0.41
        elif freq <= 12:
            fm = 0.37
        else: 
            fm = 0
    if vd0 >= 75:
        if freq <= 0.2:
            fm = 1
        elif freq <= 0.5:
            fm = 0.97
        elif freq <= 1:
            fm = 0.94
        elif freq <= 2:
            fm = 0.91
        elif freq <= 3:
            fm = 0.88
        elif freq <= 4:
            fm = 0.84
        elif freq <= 5:
            fm = 0.8
        elif freq <= 6:
            fm = 0.75
        elif freq <= 7:
            fm = 0.7
        elif freq <= 8:
            fm = 0.6
        elif freq <= 9:
            fm = 0.52
        elif freq <= 10:
            fm = 0.45
        elif freq <= 11:
            fm = 0.41
        elif freq <= 12:
            fm = 0.37
        elif freq <= 13:
            fm = 0.34
        elif freq <= 14:
            fm = 0.31
        elif freq <= 15:
            fm = 0.28
        else: 
            fm = 0
    return fm

print("Lifting Analysis")
print("Program ini menentukan tingkat resiko terjadinya Musculoskeletal Disorders (MSDs) atau cedera akibat mengangkat ")
print("beban yang terlalu berat atau posisi tubuh yang tidak ideal saat mengangkat beban tersebut.")
mass = float(input("Massa beban (kg): "))
hd = float(input("Jarak horizontal antara beban dan pengangkat (cm): "))
vd0 = float(input("Tinggi beban sebelum pengangkatan (cm): "))
vd1 = float(input("Tinggi beban setelah pengangkatan (cm): "))
asym = float(input("Kemiringan beban (" + str('\u00B0') + "): "))
coup = input("Kualitas pegangan (1: baik, 2: biasa, 3: buruk)(Ketik angkanya): ")
freq = float(input("Jumlah pengangkatan per menit : "))

hm = to_hm(hd)
vm = to_vm(vd0)
dm = to_dm(vd0, vd1)
am = to_am(asym)
cm = to_cm(vd0, coup)
fm = to_fm(vd0, freq)

rwl = 23*hm*vm*dm*am*cm*fm
li = mass/rwl

print("==========================================================")
if li <= 1:
    print("Anda memiliki resiko rendah mengalami cedera.")
elif li < 3:
    print("Anda memiliki resiko tinggi mengalami cedera.")
elif li >= 3:
    print("Anda memiliki resiko sangat tinggi mengalami cedera.")

print("Massa beban yang dianjurkan dalam posisi tubuh tersebut: <= " + str(rwl) + " kg")



