chuoi = input("Nhap chuoi: ")

ds_tu = chuoi.split()

print("So tu trong chuoi:", len(ds_tu))

print("Cac tu dai hon 5 ky tu:")

for tu in ds_tu:
    if len(tu) >= 5:
        print(tu)
