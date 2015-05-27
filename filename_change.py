import os
path = "C:\\code\\maplot pngs\\anim Aug\\"
#path = "D:\\Roy junk after 5-26-15\\"
#path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\pngs\\"
#path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\altFiles\\Historic_Ref_Apr20_v9823\\"
for filename in os.listdir(path):
    if filename[0] == 'Q':
        print filename
        filename2 = filename[:5]+filename[6:-4]+filename[5]+'.png'
        if filename2[5].isdigit(): filename2 = filename2[:5]+filename2[6:-4]+filename2[5]+'.png'
        else: filename2 = filename2[:5]+filename2[5:-5]+'0'+filename2[-5:]
        if filename2[5].isdigit(): filename2 = filename2[:5]+filename2[6:-4]+filename2[5]+'.png'
        else: filename2 = filename2[:5]+filename2[5:-6]+'0'+filename2[-6:]
        filename3 ='img'
        for letter in filename2:
            if letter.isdigit(): filename3 = filename3+letter
        filename3 = filename3+'.png'
        print filename3
        os.rename(path+filename, path+filename3)
#        print filename
#        os.rename(path+filename, path+filename[:-4]+"w EXTREME.png")
#        os.rename(path+filename, path+filename[:-4]+".csv")
#        os.rename(path+filename, path+filename[:-4]+".csv")
#    if "_Ref_" in filename:
#        filename_new = filename.replace("_Ref_", "_Historic_")
#        print filename_new
#        os.rename(path+filename, path+filename_new)
print 'all done'
