# -*- coding: utf-8 -*-
import csv , random, sys

#büyük boyutlu csv dosyaları için gerekli. Aksi taktirde hata verir.
csv.field_size_limit(sys.maxsize)

with open("/home/furkan/Masaüstü/data.csv") as f:
    r = csv.reader(f)
    header, l = next(r), list(r)

a = [x[0] for x in l]
random.shuffle(a)

b = [x[1] for x in l]
random.shuffle(b)

with open("/home/furkan/Masaüstü/karismis.csv", "wb") as f:
    csv.writer(f).writerows([header] + zip(a, b))