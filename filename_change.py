import os
path = "C:\\Users\\haggertr\\Desktop\\Documents\\work - OSU\\research\\WW2100\\Research\\results2\\altFiles\\Historic_Ref_Apr20_v9823\\"
for filename in os.listdir(path):
    print filename
    if "_Ref_" in filename:
        filename_new = filename.replace("_Ref_", "_Historic_")
        print filename_new
        os.rename(path+filename, path+filename_new)
#        print filename
print 'all done'
