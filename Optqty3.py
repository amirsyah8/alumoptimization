#ni file excell nk cakap jumlah panjang
cutLi = global_vars.get('cutLi', [])
cutLiExt = global_vars.get('cutLiExt', [])
rawMate = global_vars.get('rawMate', 0)
calcExt = global_vars.get('calcExt', [])

totalPanjang = len(cutLi)*rawMate
#f"\nTotal Panjang: {totalPanjang} mm\n"

if totalPanjang < 1000:
    result = totalPanjang
    unit = "mm"
elif totalPanjang < 1000000:
    result = totalPanjang/1000
    unit = "m"
else:
    result = totalPanjang/1000000
    unit = "Km"
f"\nTotal panjang : {result} {unit}"