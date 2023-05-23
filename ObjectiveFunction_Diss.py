# -*- coding: utf-8 -*-
"""
Created on Wed May 16 00:00:49 2018

@author: partha
"""
def ObjectiveFunction_Diss(x):
    import numpy as np
    import flopy
    import pandas as pd
    import os
    import subprocess 
    import flopy.modflow as fpm
    import flopy.utils as fpu
    import matplotlib.pyplot as plt
    import flopy.utils.binaryfile as bf
    import xlsxwriter
    import random
    import linecache
    from get_line_number import get_line_number
    
    delr=80
    delc=80
    modelname = 'Ex4'
    mf = flopy.modflow.Modflow(modelname, exe_name='mf2005')
    
    #x=np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) # Extraction Well   #(1)
    
    random_bin_vect=np.array([random.uniform(0,1),random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)])
    sum_random=np.sum(random_bin_vect)
    random_bin_vect1=random_bin_vect/sum_random
    
    xp1=random_bin_vect1[0]
    xp2=random_bin_vect1[1]
    xp3=random_bin_vect1[2]
    xp4=random_bin_vect1[3]
    
    bin_extract_well_vect=[xp1,xp2,xp3,xp4,0,0,0,0,0,0,0,0]  
    x=np.multiply(x, bin_extract_well_vect) 
    x1=x[0]
    x2=x[1]
    x3=x[2]
    x4=x[3]
    x5=x[4]
    x6=x[5]
    x7=x[6]
    x8=x[7]
    x9=x[8]
    x10=x[9]
    x11=x[10]
    x12=x[11]
    
    
    #x1=-1424                                           #   (2)
    #x2=-721
    #x3=-900.6
    #x4=-437.6
    
    injection_sum=-(x1+x2+x3+x4)
    
    y3=random.uniform(0,1)*injection_sum
    y4=injection_sum-y3
    
    y=np.array([0, 0, y3, y4, 0, 0, 0, 0, 0, 0])
    bin_inject_well_vect=[0,0,1,1,0,0,0,0,0,0]  # Seven Injection Well 
    y=np.multiply(y, bin_inject_well_vect) 
    y1=y[0]
    y2=y[1]
    y3=y[2]
    y4=y[3]
    y5=y[4]
    y6=y[5]
    y7=y[6]
    y8=y[7]
    y9=y[8]
    y10=y[9]
    
    #y3=1727                      #(3)
    #y4=1817
    
    
    # Domestic Pumping Well : Do not touch them
    welm1=np.array([1, 3, 1, -1171.66], dtype=object) #Constant
    welm2=np.array([2, 3, 1, -556.34], dtype=object)  # Constant
    
    weln1=np.array([1, 3, 5, -683.66], dtype=object)  # Constant
    weln2=np.array([2, 3, 5, -324.63], dtype=object)  # Constant
    
    # Injection Well
    
    weli1=np.array([1, 4, 1, y1], dtype=object)  # on/off : Well1
    weli2=np.array([2, 4, 1, y2], dtype=object)  # on/off : Well2
    
    weli3=np.array([1, 4, 5, y3], dtype=object)  #on/off  : Well3
    weli4=np.array([2, 4, 5, y4], dtype=object)  # on /off : Well4
    
    weli5=np.array([1, 3, 2, y5], dtype=object)   # Well5
    weli6=np.array([2, 3, 2, y6], dtype=object)
    
    weli7=np.array([1, 3, 3, y7], dtype=object)   # Well6
    weli8=np.array([2, 3, 3, y8], dtype=object)
    
    weli9=np.array([1, 3, 4, y9], dtype=object)  # Well 7
    weli10=np.array([2, 3, 4, y10], dtype=object)
    
    # Extraction Well 
    wele11=np.array([1, 5, 2, x1], dtype=object)   # Well1
    wele12=np.array([2, 5, 2, x2], dtype=object)   # Well1
    
    wele13=np.array([1, 5, 3, x3], dtype=object)   #Well2
    wele14=np.array([2, 5, 3, x4], dtype=object)   #Well2
    
    wele15=np.array([1, 5, 4, x5], dtype=object)  #Well3
    wele16=np.array([2, 5, 4, x6], dtype=object)  #Well3
    
    wele17=np.array([1, 6, 2, x7], dtype=object)  #Well4
    wele18=np.array([2, 6, 2, x8], dtype=object)  #Well4
    
    wele19=np.array([1, 6, 3, x9], dtype=object)  #Well5
    wele20=np.array([2, 6, 3, x10], dtype=object)  # Well5
    
    wele21=np.array([1, 6, 4, x11], dtype=object) # Well6
    wele22=np.array([2, 6, 4, x12], dtype=object) # Well6
    
    
    welm1=np.array_str(welm1)
    welm1=welm1[1:-1]
    welm2=np.array_str(welm2)
    welm2=welm2[1:-1]
    
    weln1=np.array_str(weln1)
    weln1=weln1[1:-1]
    weln2=np.array_str(weln2)
    weln2=weln2[1:-1]
    #..............................
    
    weli1=np.array_str(weli1)
    weli1=weli1[1:-1]
    weli2=np.array_str(weli2)
    weli2=weli2[1:-1]
    weli3=np.array_str(weli3)
    weli3=weli3[1:-1]
    weli4=np.array_str(weli4)
    weli4=weli4[1:-1]
    
    weli5=np.array_str(weli5)
    weli5=weli5[1:-1]
    weli6=np.array_str(weli6)
    weli6=weli6[1:-1]
    
    weli7=np.array_str(weli7)
    weli7=weli7[1:-1]
    weli8=np.array_str(weli8)
    weli8=weli8[1:-1]
    
    weli9=np.array_str(weli9)
    weli9=weli9[1:-1]
    weli10=np.array_str(weli10)
    weli10=weli10[1:-1]
    
    #...................................................
    wele11=np.array_str(wele11)
    wele11=wele11[1:-1]
    wele12=np.array_str(wele12)
    wele12=wele12[1:-1]
    wele13=np.array_str(wele13)
    wele13=wele13[1:-1]
    wele14=np.array_str(wele14)
    wele14=wele14[1:-1]
    wele15=np.array_str(wele15)
    wele15=wele15[1:-1]
    wele16=np.array_str(wele16)
    wele16=wele16[1:-1]
    wele17=np.array_str(wele17)
    wele17=wele17[1:-1]
    wele18=np.array_str(wele18)
    wele18=wele18[1:-1]
    wele19=np.array_str(wele19)
    wele19=wele19[1:-1]
    wele20=np.array_str(wele20)
    wele20=wele20[1:-1]
    wele21=np.array_str(wele21)
    wele21=wele21[1:-1]
    wele22=np.array_str(wele22)
    wele22=wele22[1:-1]
    
    fid=open('Ex4.wel','w')
    fid.writelines('26         0')
    fid.writelines('\n')
    fid.writelines('26         0')
    fid.writelines('\n')
    
    
    fid.writelines(welm1)
    fid.writelines('\n')
    fid.writelines(welm2)
    fid.writelines('\n')
    fid.writelines(weln1)
    fid.writelines('\n')
    fid.writelines(weln2)
    fid.writelines('\n')
    
    #.........................
    fid.writelines(weli1)
    fid.writelines('\n')
    fid.writelines(weli2)
    fid.writelines('\n')
    fid.writelines(weli3)
    fid.writelines('\n')
    fid.writelines(weli4)
    fid.writelines('\n')
    fid.writelines(weli5)
    fid.writelines('\n')
    fid.writelines(weli6)
    fid.writelines('\n')
    fid.writelines(weli7)
    fid.writelines('\n')
    fid.writelines(weli8)
    fid.writelines('\n')
    fid.writelines(weli9)
    fid.writelines('\n')
    fid.writelines(weli10)
    fid.writelines('\n')
     #...................................
    
    fid.writelines(wele11)
    fid.writelines('\n')
    fid.writelines(wele12)
    fid.writelines('\n')
    fid.writelines(wele13)
    fid.writelines('\n')
    fid.writelines(wele14)
    fid.writelines('\n')
    fid.writelines(wele15)
    fid.writelines('\n')
    fid.writelines(wele16)
    fid.writelines('\n')
    fid.writelines(wele17)
    fid.writelines('\n')
    fid.writelines(wele18)
    fid.writelines('\n')
    fid.writelines(wele19)
    fid.writelines('\n')
    fid.writelines(wele20)
    fid.writelines('\n')
    fid.writelines(wele21)
    fid.writelines('\n')
    fid.writelines(wele22)
    fid.writelines('\n')
    fid.close()
    
#    subprocess.run("mf2005 Ex4.nam")
    subprocess.run("mf2k Ex4.nam")
    
    fpth = os.path.join('Ex4.hds')
    hfile = fpu.HeadFile(fpth)
    times=hfile.get_times()
    hydraulic_head = hfile.get_data(totim=1.0)
    head_Layer1=hydraulic_head[0,:,:]
    head_Layer2=hydraulic_head[1,:,:]
    #np.savetxt('hydraulic_head_layer1.csv',head_Layer1)
    #np.savetxt('hydraulic_head_layer2.csv',head_Layer2)
    head_Layer1_bin=head_Layer1<13 
    head_Layer1_bin=head_Layer1_bin*1
    head_Layer2_bin=head_Layer2<13 
    head_Layer2_bin=head_Layer2_bin*1
    head_penlt_number=sum(map(sum,head_Layer1_bin))+sum(map(sum,head_Layer2_bin))-16
    
    hfile.close()
    
    ###############################################################################
    ############# MT3DMS###########################################################
#   subprocess.run("mt3dms53 Ex4_mt.nam") 
    subprocess.run("mt3dms4b Ex4_mt.nam") 
       
    ucnobj = bf.UcnFile('MT3D001.UCN', precision='single')
    #UCN_Species1=ucnobj.list_records()
    Con_Species1_Layer1=ucnobj.get_alldata(mflay=0, nodata=-9999)
    Con_Species1_Layer2=ucnobj.get_alldata(mflay=1, nodata=-9999)
    
    ucnobj = bf.UcnFile('MT3D002.UCN', precision='single')
    #UCN_Species2=ucnobj.list_records()
    Con_Species2_Layer1=ucnobj.get_alldata(mflay=0, nodata=-9999)
    Con_Species2_Layer2=ucnobj.get_alldata(mflay=1, nodata=-9999)
     #.................................................................................
    c_s1_Cm_1T_L1=Con_Species1_Layer1[0,:,:] # Con_Species1_Containmentzone_180T_Layer1
    c_s1_Cm_1T_L1_val=np.array([c_s1_Cm_1T_L1[1,0],c_s1_Cm_1T_L1[1,1],c_s1_Cm_1T_L1[1,2],
                            c_s1_Cm_1T_L1[1,3],c_s1_Cm_1T_L1[1,4],c_s1_Cm_1T_L1[1,5],
                            c_s1_Cm_1T_L1[2,0],c_s1_Cm_1T_L1[2,4],c_s1_Cm_1T_L1[2,5],
                            c_s1_Cm_1T_L1[3,5]])
    c_s1_Cm_1T_L1_val_F=c_s1_Cm_1T_L1_val>=5
    c_s1_Cm_1T_L1_val_F=c_s1_Cm_1T_L1_val_F*1


    c_s1_Cm_2T_L1=Con_Species1_Layer1[1,:,:] # Con_Species1_Containmentzone_270T_Llayer1
    c_s1_Cm_2T_L1_val=np.array([c_s1_Cm_2T_L1[1,0],c_s1_Cm_2T_L1[1,1],c_s1_Cm_2T_L1[1,2],
                            c_s1_Cm_2T_L1[1,3],c_s1_Cm_2T_L1[1,4],c_s1_Cm_2T_L1[1,5],
                            c_s1_Cm_2T_L1[2,0],c_s1_Cm_2T_L1[2,4],c_s1_Cm_2T_L1[2,5],
                            c_s1_Cm_2T_L1[3,5]])
    c_s1_Cm_2T_L1_val_F=c_s1_Cm_2T_L1_val>=5
    c_s1_Cm_2T_L1_val_F=c_s1_Cm_2T_L1_val_F*1

    c_s1_Cm_1T_L2=Con_Species1_Layer2[0,:,:] # Con_Species1_Containmentzone_180T_Layer2
    c_s1_Cm_1T_L2_val=np.array([c_s1_Cm_1T_L2[1,0],c_s1_Cm_1T_L2[1,1],c_s1_Cm_1T_L2[1,2],
                            c_s1_Cm_1T_L2[1,3],c_s1_Cm_1T_L2[1,4],c_s1_Cm_1T_L2[1,5],
                            c_s1_Cm_1T_L2[2,0],c_s1_Cm_1T_L2[2,4],c_s1_Cm_1T_L2[2,5],
                            c_s1_Cm_1T_L2[3,5]])
    c_s1_Cm_1T_L2_val_F=c_s1_Cm_1T_L2_val>=5
    c_s1_Cm_1T_L2_val_F=c_s1_Cm_1T_L2_val_F*1


    c_s1_Cm_2T_L2=Con_Species1_Layer2[1,:,:] # Con_Species1_Containmentzone_270T_Llayer2
    c_s1_Cm_2T_L2_val=np.array([c_s1_Cm_2T_L2[1,0],c_s1_Cm_2T_L2[1,1],c_s1_Cm_2T_L2[1,2],
                            c_s1_Cm_2T_L2[1,3],c_s1_Cm_2T_L2[1,4],c_s1_Cm_2T_L2[1,5],
                            c_s1_Cm_2T_L2[2,0],c_s1_Cm_2T_L2[2,4],c_s1_Cm_2T_L2[2,5],
                            c_s1_Cm_2T_L2[3,5]])
    c_s1_Cm_2T_L2_val_F=c_s1_Cm_2T_L2_val>=5
    c_s1_Cm_2T_L2_val_F=c_s1_Cm_2T_L2_val_F*1

    #...............................................................................
    c_s2_Cm_1T_L1=Con_Species2_Layer1[0,:,:] # Con_Species1_Containmentzone_180T_Layer1
    c_s2_Cm_1T_L1_val=np.array([c_s2_Cm_1T_L1[1,0],c_s2_Cm_1T_L1[1,1],c_s2_Cm_1T_L1[1,2],
                            c_s2_Cm_1T_L1[1,3],c_s2_Cm_1T_L1[1,4],c_s2_Cm_1T_L1[1,5],
                            c_s2_Cm_1T_L1[2,0],c_s2_Cm_1T_L1[2,4],c_s2_Cm_1T_L1[2,5],
                            c_s2_Cm_1T_L1[3,5]])
    c_s2_Cm_1T_L1_val_F=c_s2_Cm_1T_L1_val>=5
    c_s2_Cm_1T_L1_val_F=c_s1_Cm_1T_L1_val_F*1


    c_s2_Cm_2T_L1=Con_Species2_Layer1[1,:,:] # Con_Species1_Containmentzone_270T_Llayer1
    c_s2_Cm_2T_L1_val=np.array([c_s2_Cm_2T_L1[1,0],c_s2_Cm_2T_L1[1,1],c_s2_Cm_2T_L1[1,2],
                            c_s2_Cm_2T_L1[1,3],c_s2_Cm_2T_L1[1,4],c_s2_Cm_2T_L1[1,5],
                            c_s2_Cm_2T_L1[2,0],c_s2_Cm_2T_L1[2,4],c_s2_Cm_2T_L1[2,5],
                            c_s2_Cm_2T_L1[3,5]])
    c_s2_Cm_2T_L1_val_F=c_s2_Cm_2T_L1_val>=5
    c_s2_Cm_2T_L1_val_F=c_s2_Cm_2T_L1_val_F*1

    c_s2_Cm_1T_L2=Con_Species2_Layer2[0,:,:] # Con_Species1_Containmentzone_180T_Layer2
    c_s2_Cm_1T_L2_val=np.array([c_s2_Cm_1T_L2[1,0],c_s2_Cm_1T_L2[1,1],c_s2_Cm_1T_L2[1,2],
                            c_s2_Cm_1T_L2[1,3],c_s2_Cm_1T_L2[1,4],c_s2_Cm_1T_L2[1,5],
                            c_s2_Cm_1T_L2[2,0],c_s2_Cm_1T_L2[2,4],c_s2_Cm_1T_L2[2,5],
                            c_s2_Cm_1T_L2[3,5]])
    c_s2_Cm_1T_L2_val_F=c_s2_Cm_1T_L2_val>=5
    c_s2_Cm_1T_L2_val_F=c_s2_Cm_1T_L2_val_F*1


    c_s2_Cm_2T_L2=Con_Species2_Layer2[1,:,:] # Con_Species1_Containmentzone_270T_Llayer2
    c_s2_Cm_2T_L2_val=np.array([c_s2_Cm_2T_L2[1,0],c_s2_Cm_2T_L2[1,1],c_s2_Cm_2T_L2[1,2],
                            c_s2_Cm_2T_L2[1,3],c_s2_Cm_2T_L2[1,4],c_s2_Cm_2T_L2[1,5],
                            c_s2_Cm_2T_L2[2,0],c_s2_Cm_2T_L2[2,4],c_s2_Cm_2T_L2[2,5],
                            c_s2_Cm_2T_L2[3,5]])
    c_s2_Cm_2T_L2_val_F=c_s2_Cm_2T_L2_val>=5
    c_s2_Cm_2T_L2_val_F=c_s2_Cm_2T_L2_val_F*1


    con_penlt=(c_s1_Cm_1T_L1_val_F+c_s1_Cm_2T_L1_val_F+c_s1_Cm_1T_L2_val_F+
    c_s1_Cm_2T_L2_val_F+c_s2_Cm_1T_L1_val_F+c_s2_Cm_2T_L1_val_F+c_s2_Cm_1T_L2_val_F
    +c_s2_Cm_2T_L2_val_F)

    con_penlt_total=sum(con_penlt)
          

   #.............................................................................
    
     
 
    #Cleanup zone: #Stress Period 3: 365 days
    concen_clean_species1_L1=Con_Species1_Layer1[2,:,:]>=5   #Stress Period 3: 365 days
    concen_clean_species1_L1=concen_clean_species1_L1*1
    concen_clean_species1_L2=Con_Species1_Layer2[2,:,:]>=5
    concen_clean_species1_L2=concen_clean_species1_L2*1

    concen_clean_species2_L1=Con_Species2_Layer1[2,:,:]>=5
    concen_clean_species2_L1=concen_clean_species2_L1*1
    concen_clean_species2_L2=Con_Species2_Layer2[2,:,:]>=5
    concen_clean_species2_L2=concen_clean_species2_L2*1


    species1_penlt_number_365=sum(map(sum,concen_clean_species1_L1))+sum(map(sum,concen_clean_species1_L2))                         
    species2_penlt_number_365=sum(map(sum,concen_clean_species2_L1))+sum(map(sum,concen_clean_species2_L2))

    
    head_L1=np.array([head_Layer1[2,1],head_Layer1[2,2],head_Layer1[2,3],
                      head_Layer1[3,0],head_Layer1[3,1],head_Layer1[3,2],
                      head_Layer1[3,3],head_Layer1[3,4],head_Layer1[4,0],
                      head_Layer1[4,1],head_Layer1[4,2],head_Layer1[4,3],
                      head_Layer1[4,4],head_Layer1[5,0],head_Layer1[5,1],
                      head_Layer1[5,2],head_Layer1[5,3],head_Layer1[5,4],
                      head_Layer1[6,0],head_Layer1[6,1],head_Layer1[6,2],
                      head_Layer1[6,3],head_Layer1[6,4],head_Layer1[7,0],
                      head_Layer1[7,1],head_Layer1[7,2],head_Layer1[7,3]])
    
    head_L2=np.array([head_Layer2[2,1],head_Layer2[2,2],head_Layer2[2,3],
                      head_Layer2[3,0],head_Layer2[3,1],head_Layer2[3,2],
                      head_Layer2[3,3],head_Layer2[3,4],head_Layer2[4,0],
                      head_Layer2[4,1],head_Layer2[4,2],head_Layer2[4,3],
                      head_Layer2[4,4],head_Layer2[5,0],head_Layer2[5,1],
                      head_Layer2[5,2],head_Layer2[5,3],head_Layer2[5,4],
                      head_Layer2[6,0],head_Layer2[6,1],head_Layer2[6,2],
                      head_Layer2[6,3],head_Layer2[6,4],head_Layer2[7,0],
                      head_Layer2[7,1],head_Layer2[7,2],head_Layer2[7,3]])
    
    
    
    
    con_S1_L1=Con_Species1_Layer1[2,:,:]
    con_S1L1=np.array([con_S1_L1[2,1],con_S1_L1[2,2],con_S1_L1[2,3],con_S1_L1[3,0],
                       con_S1_L1[3,1],con_S1_L1[3,2],con_S1_L1[3,3],con_S1_L1[3,4],
                       con_S1_L1[4,0],con_S1_L1[4,1],con_S1_L1[4,2],con_S1_L1[4,3],
                       con_S1_L1[4,4],con_S1_L1[5,0],con_S1_L1[5,1],con_S1_L1[5,2],
                       con_S1_L1[5,3],con_S1_L1[5,4],con_S1_L1[6,0],con_S1_L1[6,1],
                       con_S1_L1[6,2],con_S1_L1[6,3],con_S1_L1[6,4],con_S1_L1[7,0],
                       con_S1_L1[7,1],con_S1_L1[7,2],con_S1_L1[7,3]])
    con_S1_L2=Con_Species1_Layer2[2,:,:]
    con_S1L2=np.array([con_S1_L2[2,1],con_S1_L2[2,2],con_S1_L2[2,3],con_S1_L2[3,0],
                       con_S1_L2[3,1],con_S1_L2[3,2],con_S1_L2[3,3],con_S1_L2[3,4],
                       con_S1_L2[4,0],con_S1_L2[4,1],con_S1_L2[4,2],con_S1_L2[4,3],
                       con_S1_L2[4,4],con_S1_L2[5,0],con_S1_L2[5,1],con_S1_L2[5,2],
                       con_S1_L2[5,3],con_S1_L2[5,4],con_S1_L2[6,0],con_S1_L2[6,1],
                       con_S1_L2[6,2],con_S1_L2[6,3],con_S1_L2[6,4],con_S1_L2[7,0],
                       con_S1_L2[7,1],con_S1_L2[7,2],con_S1_L2[7,3]])
    
    con_S2_L1=Con_Species2_Layer1[2,:,:]
    con_S2L1=np.array([con_S2_L1[2,1],con_S2_L1[2,2],con_S2_L1[2,3],con_S2_L1[3,0],
                       con_S2_L1[3,1],con_S2_L1[3,2],con_S2_L1[3,3],con_S2_L1[3,4],
                       con_S2_L1[4,0],con_S2_L1[4,1],con_S2_L1[4,2],con_S2_L1[4,3],
                       con_S2_L1[4,4],con_S2_L1[5,0],con_S2_L1[5,1],con_S2_L1[5,2],
                       con_S2_L1[5,3],con_S2_L1[5,4],con_S2_L1[6,0],con_S2_L1[6,1],
                       con_S2_L1[6,2],con_S2_L1[6,3],con_S2_L1[6,4],con_S2_L1[7,0],
                       con_S2_L1[7,1],con_S2_L1[7,2], con_S2_L1[7,3]])
    
    con_S2_L2=Con_Species2_Layer1[2,:,:]
    con_S2L2=np.array([con_S2_L2[2,1],con_S2_L2[2,2],con_S2_L2[2,3],con_S2_L2[3,0],
                       con_S2_L2[3,1],con_S2_L2[3,2],con_S2_L2[3,3],con_S2_L2[3,4],
                       con_S2_L2[4,0],con_S2_L2[4,1],con_S2_L2[4,2],con_S2_L2[4,3],
                       con_S2_L2[4,4],con_S2_L2[5,0],con_S2_L2[5,1],con_S2_L2[5,2],
                       con_S2_L2[5,3],con_S2_L2[5,4],con_S2_L2[6,0],con_S2_L2[6,1],
                       con_S2_L2[6,2],con_S2_L2[6,3],con_S2_L2[6,4],con_S2_L2[7,0],
                       con_S2_L2[7,1],con_S2_L2[7,2],con_S2_L2[7,3]])
    
    for ii in range(con_S1L1.size):
        if con_S1L1[ii]<0:
           con_S1L1[ii]=0
           
    for ii in range(con_S1L2.size):
        if con_S1L2[ii]<0:
           con_S1L2[ii]=0
           
    for ii in range(con_S2L1.size):
        if con_S2L1[ii]<0:
           con_S2L1[ii]=0  
           
    for ii in range(con_S2L2.size):
        if con_S2L2[ii]<0:
           con_S2L2[ii]=0   
    
    species1_mass_array=np.multiply(head_L1,con_S1L1)+np.multiply(10,con_S1L2)
    species1_mass=0.3*delr*delc*(np.sum(species1_mass_array))
    
    species2_mass_array=np.multiply(head_L1,con_S2L1)+np.multiply(10,con_S2L2)
    species2_mass=0.3*delr*delc*(np.sum(species2_mass_array))
    
    
    ############################
    #############################################################
    #TOTAL
    #Species1

    head_Layer1_Flaten=head_Layer1.flatten()
    Con_Species1_Layer1_Flatten=Con_Species1_Layer1[2,:,:].flatten()
    Con_Species1_Layer2_Flatten=Con_Species1_Layer2[2,:,:].flatten()
    for ii in range(head_Layer1_Flaten.size):
        if head_Layer1_Flaten[ii]<0:
           head_Layer1_Flaten[ii]=0      
   
    for ii in range(Con_Species1_Layer1_Flatten.size):
        if Con_Species1_Layer1_Flatten[ii]>100:
           Con_Species1_Layer1_Flatten[ii]=0  
           
    for ii in range(Con_Species1_Layer1_Flatten.size):
        if Con_Species1_Layer1_Flatten[ii]<0:
           Con_Species1_Layer1_Flatten[ii]=0 
           
    
    for ii in range(Con_Species1_Layer2_Flatten.size):
        if Con_Species1_Layer2_Flatten[ii]>100:
           Con_Species1_Layer2_Flatten[ii]=0        
           
    for ii in range(Con_Species1_Layer2_Flatten.size):
        if Con_Species1_Layer2_Flatten[ii]<0:
            Con_Species1_Layer2_Flatten[ii]=0        
   
   

    species1_mass_array_T=np.multiply(head_Layer1_Flaten,Con_Species1_Layer1_Flatten)+np.multiply(10,Con_Species1_Layer2_Flatten)
    species1_mass_T=0.3*delr*delc*(np.sum(species1_mass_array_T))
    
    #Species2
    head_Layer1_Flaten=head_Layer1.flatten()
    Con_Species2_Layer1_Flatten=Con_Species2_Layer1[2,:,:].flatten()
    Con_Species2_Layer2_Flatten=Con_Species2_Layer2[2,:,:].flatten()
    for ii in range(head_Layer1_Flaten.size):
        if head_Layer1_Flaten[ii]<0:
           head_Layer1_Flaten[ii]=0      
           
    for ii in range(Con_Species2_Layer1_Flatten.size):
        if Con_Species2_Layer1_Flatten[ii]>100:
           Con_Species2_Layer1_Flatten[ii]=0  
           
    for ii in range(Con_Species2_Layer1_Flatten.size):
        if Con_Species2_Layer1_Flatten[ii]<0:
           Con_Species2_Layer1_Flatten[ii]=0 
           
    
    for ii in range(Con_Species2_Layer2_Flatten.size):
        if Con_Species2_Layer2_Flatten[ii]>100:
           Con_Species2_Layer2_Flatten[ii]=0        
           
    for ii in range(Con_Species2_Layer2_Flatten.size):
        if Con_Species2_Layer2_Flatten[ii]<0:
           Con_Species2_Layer2_Flatten[ii]=0        
   
   

    species2_mass_array_T=np.multiply(head_Layer1_Flaten,Con_Species2_Layer1_Flatten)+np.multiply(10,Con_Species2_Layer2_Flatten)
    species2_mass_T=0.3*delr*delc*(np.sum(species2_mass_array_T))
    
    
    
    #Total_contaminant_mass_in_aquifer=(species1_mass_T*1.3103+species2_mass_T*1.6192)
    Total_dissolved_mass_in_aquifer=(species1_mass_T+species2_mass_T)




# Total 
#Species over
#..............................................................................Mass file
    
   
             
    penlt=10000000
    F=Total_dissolved_mass_in_aquifer+(species1_penlt_number_365*penlt)+(con_penlt_total*penlt)+(species2_penlt_number_365*penlt)+(head_penlt_number*penlt)

    
    F1=np.array([F,0])
    F1=np.array_str(F1)
    x=np.array_str(x)
    y=np.array_str(y)
          
    fid=open('Optimization_OUTPUT_PYSOT_Diss.txt', 'a')
    fid.writelines(F1)
    fid.writelines('\n')
    fid.writelines(x)
    fid.writelines('\n')
    fid.writelines(y)
    fid.writelines('\n')
    fid.writelines('.............................................................')
    fid.writelines('\n')
    fid.close()     
    ucnobj.close()
    linecache.clearcache()
    return F
    
    #print('Simulation Completed')








