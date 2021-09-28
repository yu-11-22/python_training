string="hello"  
# %s列印時結果是hello
print(("string=%s") % string)
# %2s意思是字串長度為2，當原字串的長度超過2時，按原長度列印
print(("string=%2s") % string)
# %7s意思是字串長度為7，當原字串的長度小於7時，在原字串左側補空格
print(("string=%7s") % string)
# %-7s意思是字串長度為7，當原字串的長度小於7時，在原字串右側補空格
print(("string=%-7s!") % string)
# %.2s意思是擷取字串的前2個字元
print(("string=%.2s") % string)
# %.7s意思是擷取字串的前7個字元，當原字串長度小於7時，即是字串本身
print(("string=%.7s") % string)
# %a.bs這種格式是上面兩種格式的綜合，首先根據小數點後面的b擷取字串 
# 當擷取的字串長度小於a時，還需要在其左側補空格
print(("string=%7.2s") % string)
print(("string=%2.7s") % string)
print(("string=%10.7s") % string)