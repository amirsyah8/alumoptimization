#ini pon dalam excel , ni nak cakap peratus kerugian
cutLi = global_vars.get('cutLi', [])
cutLiExt = global_vars.get('cutLiExt', [])
rawMate = global_vars.get('rawMate', 0)
calcExt = global_vars.get('calcExt', [])

total_sum_cutLiExt = sum(sum(sublist) for sublist in cutLiExt)
peratusWaste = (rawMate*len(cutLi)-total_sum_cutLiExt)/(rawMate*len(cutLi))
peratusWaste = peratusWaste*100
f"\nPeratus kerugian : {round(peratusWaste,2)} %\n"