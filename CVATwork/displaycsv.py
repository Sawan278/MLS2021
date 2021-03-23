def displaycsv(path1,path2):
    import pandas as pd
    import cv2
    
    data=pd.read_csv(path1)
    frameno2=[]
    
    for i in data.frameno:
        if i//10==0:
            frameno2.append("00"+str(i))
        elif i//100==0:
            frameno2.append("0"+str(i))
        else:
            frameno2.append(str(i))
    
    data.frameno=frameno2
    for i in range(len(data.frameno)):
        j=data.iloc[i,0]
        img1=cv2.imread(path2+j+".jpg")
        img1=cv2.rectangle(img1, (int(data.iloc[i,1]),int(data.iloc[i,2])), (int(data.iloc[i,3]),int(data.iloc[i,4])), (255,0,0), 3)
        cv2.imwrite(path2+str(data.iloc[i,0])+".jpg",img1)
