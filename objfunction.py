# -*- coding: utf-8 -*-
"""
Created on Wed May 16 00:00:49 2018

@author: partha
"""
def objfunction(x):
    import numpy as np
    import flopy
    import pandas as pd
    import os
    import flopy.modflow as fpm
    import flopy.utils as fpu
    import matplotlib.pyplot as plt
    import flopy.utils.binaryfile as bf
    import xlsxwriter
    import random
    import linecache
    from get_line_number import get_line_number
       
    # Assign name and create modflow model object
    modelname = 'Ex4'
    mf = flopy.modflow.Modflow(modelname, exe_name='mf2005')
    
    # Model domain and grid definition
    Lx = 480
    Ly = 640
    ztop = 20.
    zbot = np.array([0., -10.])
    nlay = 2
    nrow = 8
    ncol = 6
    delr = Lx/ncol
    delc = Ly/nrow
    delv = (ztop - zbot) / nlay
    
    
    # Create the discretization object
    dis = flopy.modflow.ModflowDis(mf, nlay, nrow, ncol, delr=delr, delc=delc,
                                   top=ztop, botm=zbot)
    
    ibd = pd.read_excel('Ex4_Ibound.xlsx',header=None)
    ib = ibd.as_matrix()
    ibound = np.zeros((nlay, nrow, ncol), dtype=np.int64)
    ibound[0,:,:]=ib
    ibound[1,:,:]=ib
    
    shd1=pd.read_excel('Ex4_Starting_Head_Layer1.xlsx',header=None)
    sh1=shd1.as_matrix()
    
    shd2=pd.read_excel('Ex4_Starting_Head_Layer2.xlsx',header=None)
    sh2=shd2.as_matrix()
    
    strt = np.zeros((nlay, nrow, ncol), dtype=np.float32)
    
    strt[0,:,:]=sh1*16.3
    strt[1,:,:]=sh2*16.3
    
    bas = flopy.modflow.ModflowBas(mf, ibound=ibound, strt=strt, ifrefm=False) # For fixed format, ifrefm=False; Free format=True
    
    
    # Add OC package to the MODFLOW model
    spd = {(0, 0): ['print head', 'print budget','print drawdown', 'save head', 'save budget','save drawdown']}
    oc = flopy.modflow.ModflowOc(mf, stress_period_data=spd, compact=True)
    
    # Add PCG package to the MODFLOW model
    pcg = flopy.modflow.ModflowPcg(mf)
    
    # Add River Package to the MODFLOW model
    riv_spd_Lay1=pd.read_excel('Ex4_River_Layer1.xlsx',header=None,dtype=object)
    riv_spd=riv_spd_Lay1.as_matrix()
    riv = flopy.modflow.ModflowRiv(mf,ipakcb=-1, stress_period_data=riv_spd)
    
    # Add Well Package
    #well_group_both=pd.read_excel('Ex4_Pumping_Well.xlsx',header=None,dtype=object)
    #well_group=well_group_both.as_matrix()
    #wel1=well_group[0,:]
    #wel2=well_group[1,:]
    #wel3=well_group[2,:]
    #wel4=well_group[3,:]
    
    #x=np.array([-1.01, -1.02, -1.03, -1.04, -1.05, -1.06, -1.07, -1.08, -1.09, -1.10, -1.11, -1.12]) # Extraction Well
    
    
    #bin_extract_well_vect=[1,1,1,1,0,0,0,0,0,0,0,0]     # Six Extraction Well, only 2 are active,
    
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
    
    
    #x1=-1204.93
    #x2=-1000
    #x3=-1000
    #x4=-338.22
    
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
    
    #y3=1726.51
    #y4=1816.64
    
    
    
    # Domestic Pumping Well : Do not touch them
    welm1=np.array([0, 2, 0, -1171.66], dtype=object) #Constant
    welm2=np.array([1, 2, 0, -556.34], dtype=object)  # Constant
    
    weln1=np.array([0, 2, 4, -683.66], dtype=object)  # Constant
    weln2=np.array([1, 2, 4, -324.63], dtype=object)  # Constant
    
    # Injection Well
    
    weli1=np.array([0, 3, 0, y1], dtype=object)  # on/off : Well1
    weli2=np.array([1, 3, 0, y2], dtype=object)  # on/off : Well2
    
    weli3=np.array([0, 3, 4, y3], dtype=object)  #on/off  : Well3
    weli4=np.array([1, 3, 4, y4], dtype=object)  # on /off : Well4
    
    weli5=np.array([0, 2, 1, y5], dtype=object)   # Well5
    weli6=np.array([1, 2, 1, y6], dtype=object)
    
    weli7=np.array([0, 2, 2, y7], dtype=object)   # Well6
    weli8=np.array([1, 2, 2, y8], dtype=object)
    
    weli9=np.array([0, 2, 3, y9], dtype=object)  # Well 7
    weli10=np.array([1, 2, 3, y10], dtype=object)
    
    # Extraction Well 
    wele11=np.array([0, 4, 1, x1], dtype=object)   # Well1
    wele12=np.array([1, 4, 1, x2], dtype=object)   # Well1
    
    wele13=np.array([0, 4, 2, x3], dtype=object)   #Well2
    wele14=np.array([1, 4, 2, x4], dtype=object)   #Well2
    
    wele15=np.array([0, 4, 3, x5], dtype=object)  #Well3
    wele16=np.array([1, 4, 3, x6], dtype=object)  #Well3
    
    wele17=np.array([0, 5, 1, x7], dtype=object)  #Well4
    wele18=np.array([1, 5, 1, x8], dtype=object)  #Well4
    
    wele19=np.array([0, 5, 2, x9], dtype=object)  #Well5
    wele20=np.array([1, 5, 2, x10], dtype=object)  # Well5
    
    wele21=np.array([0, 5, 3, x11], dtype=object) # Well6
    wele22=np.array([1, 5, 3, x12], dtype=object) # Well6
    
    
    
    
    stress_period_data ={0:[welm1, welm2, weln1, weln2, weli1, weli2, weli3, weli4,
                            weli5, weli6, weli7,weli8, weli9,weli10, wele11,
                            wele12, wele13,wele14,wele15, wele16, wele17, wele18,
                            wele19, wele20, wele21, wele22]}
    
    WEL=flopy.modflow.ModflowWel(mf, stress_period_data=stress_period_data)
    
    # MODFLOW BCF package
    
    bcf=flopy.modflow.ModflowBcf(mf,laycon=[1,0],hy=91.5,tran=866.7, vcont=0.0297)
    
    # MODFLOW RCH Package
    rch_T=pd.read_excel('Ex4_Recharge.xlsx',header=None,dtype=object)
    rch_M=rch_T.as_matrix()
    rch_v=rch_M*0.001016
    
    rch = flopy.modflow.ModflowRch(mf, nrchop=1, rech=rch_v)
    
    flopy.modflow.ModflowLmt(mf, output_file_name='Ex4_mt.ftl', 
                             output_file_unit=10, output_file_header='extended', 
                             output_file_format='unformatted', extension='lmt6')
    
    
    
    # Write the MODFLOW model input files
    mf.write_input()
    
    [success, buff] = mf.run_model()
    
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
    
    #plt.contour(head_Layer1)
    
    
    ###############################################################################
    ############# MT3DMS###########################################################
    modelname='Ex4_mt'
    model_ws = 'data'
    icbd = pd.read_excel('Ex4_ICbound.xlsx',header=None)
    icb = icbd.as_matrix()
    icbound = np.zeros((nlay, nrow, ncol), dtype=np.int64)
    icbound[0,:,:]=icb
    icbound[1,:,:]=icb
    
    species1_layer1_T= pd.read_excel('EX4_Contaminant_Species1_Layer1.xlsx',
                                     header=None)
    species1_layer1=species1_layer1_T.as_matrix()
    
    
    species2_layer2_T= pd.read_excel('EX4_Contaminant_Species2_Layer2.xlsx',
                                     header=None)
    species2_layer2=species2_layer2_T.as_matrix()
    Species1 = np.zeros((nlay, nrow, ncol), dtype=np.float64)
    Species2 = np.zeros((nlay, nrow, ncol), dtype=np.float64)
    Species1[0,:,:]=species1_layer1
    Species2[1,:,:]=species2_layer2
    perlen=[180, 90, 95]
    
    
    mt1 = flopy.mt3d.Mt3dms(modflowmodel=mf, modelname=modelname,
                           namefile_ext='nam',ftlfilename='Ex4_mt.ftl',exe_name='mt3dms.exe', structured=True)
    #mt = flopy.mt3d.Mt3dms(modflowmodel=mf, modelname=modelname,model_ws=model_ws,namefile_ext='mtnam')
    
    btn = flopy.mt3d.Mt3dBtn(mt1, MFStyleArr=False, nper=3,perlen=perlen, icbund=icbound, prsity=0.3,
                             ncomp=2, mcomp=2,  sconc=Species1, sconc2=Species2)
    
    dsp=flopy.mt3d.Mt3dDsp(mt1, al=4.0, trpt=0.2, trpv=0.001, 
                           dmcoef=[8.64e-05, 8.64e-05],dmcoef2=[8.64e-05, 8.64e-05],
                           multiDiff=1)
    adv=flopy.mt3d.Mt3dAdv(mt1,mixelm=-1)
    ssm = flopy.mt3d.Mt3dSsm(mt1,crch=None,crch2=0)
    gcg = flopy.mt3d.Mt3dGcg(mt1, mxiter=10, iter1=50, isolve=3, ncrs=0,
                       accl=1, cclose=1e-6, iprgcg=1)
    rct1=flopy.mt3d.Mt3dRct(mt1,isothm=1,ireact=0, igetsc=0, rhob=4100.529,
                            srconc=None, sp1=0.2266e-4, sp2=0.4531e-4)
      
    
    #mtsf=flopy.mt3d.mt.Mt3dList(mt1, extension='list1', listunit=7)
    
    mt1.write_input()
    [success1, buff1]=mt1.run_model()
    
    ucnobj = bf.UcnFile('MT3D001.UCN', precision='single')
    UCN_Species1=ucnobj.list_records()
    Con_Species1_Layer1=ucnobj.get_alldata(mflay=0, nodata=-9999)
    Con_Species1_Layer2=ucnobj.get_alldata(mflay=1, nodata=-9999)
    
    ucnobj = bf.UcnFile('MT3D002.UCN', precision='single')
    UCN_Species2=ucnobj.list_records()
    Con_Species2_Layer1=ucnobj.get_alldata(mflay=0, nodata=-9999)
    Con_Species2_Layer2=ucnobj.get_alldata(mflay=1, nodata=-9999)
    
    
    #modelmap = flopy.plot.ModelMap(model=mf, layer=0)
    #qm = modelmap.plot_ibound()
    #lc = modelmap.plot_grid()
    
    
    
    #np.savetxt('Con_Species1_Layer1_SP1.csv', Con_Species1_Layer1[0,:,:])
    #np.savetxt('Con_Species1_Layer1_SP2.csv', Con_Species1_Layer1[1,:,:])
    #np.savetxt('Con_Species1_Layer1_SP3.csv', Con_Species1_Layer1[2,:,:])
    
    #np.savetxt('Con_Species1_Layer2_SP1.csv', Con_Species1_Layer2[0,:,:])
    #np.savetxt('Con_Species1_Layer2_SP2.csv', Con_Species1_Layer2[1,:,:])
    #np.savetxt('Con_Species1_Layer2_SP3.csv', Con_Species1_Layer2[2,:,:])
    
    #np.savetxt('Con_Species2_Layer1_SP1.csv', Con_Species2_Layer1[0,:,:])
    #np.savetxt('Con_Species2_Layer1_SP2.csv', Con_Species2_Layer1[1,:,:])
    #np.savetxt('Con_Species2_Layer1_SP3.csv', Con_Species2_Layer1[2,:,:])
    
    
    #np.savetxt('Con_Species2_Layer2_SP1.csv', Con_Species2_Layer2[0,:,:])
    #np.savetxt('Con_Species2_Layer2_SP2.csv', Con_Species2_Layer2[1,:,:])
    #np.savetxt('Con_Species2_Layer2_SP3.csv', Con_Species2_Layer2[2,:,:])
    
    #Cleanup zone
    concen_clean_species1_L1=Con_Species1_Layer1[2,:,:]>=5   #Stress Period 3: 365 days
    concen_clean_species1_L1=concen_clean_species1_L1*1
    concen_clean_species1_L2=Con_Species1_Layer2[2,:,:]>=5
    concen_clean_species1_L2=concen_clean_species1_L2*1
    
    concen_clean_species2_L1=Con_Species2_Layer1[2,:,:]>=5
    concen_clean_species2_L1=concen_clean_species2_L1*1
    concen_clean_species2_L2=Con_Species2_Layer2[2,:,:]>=5
    concen_clean_species2_L2=concen_clean_species2_L2*1
    
    
    species1_penlt_number=sum(map(sum,concen_clean_species1_L1))+sum(map(sum,concen_clean_species1_L2))-8*2                      
                          
    species2_penlt_number=sum(map(sum,concen_clean_species2_L1))+sum(map(sum,concen_clean_species2_L2))-8*2                       
    
    #..............................................................................
    
    
    
    
    
    
    
    
    # Containtment (Exclusion) zone: Stress Period 1 (180 days) 
    
    
    #..............................................................................Mass file
    linenumber1=get_line_number('365.00','MT3D001.MAS')
    linenumber2=get_line_number('365.00','MT3D002.MAS')
    
    line_species1=linecache.getline('MT3D001.MAS', linenumber1)
    line_species2=linecache.getline('MT3D002.MAS', linenumber2)
    
    
    
    
    #line_species1_mass=np.fromstring(line_species1,  sep=',')
    #line_species2_mass=np.fromstring(line_species2,  sep=',')
    
    line_species1_MAS=line_species1[85:100]
    line_species1_MAS=float(line_species1_MAS)
    line_species2_MAS=line_species2[85:100]
    line_species2_MAS=float(line_species2_MAS)
    
    penlt=10000000
    F=(line_species1_MAS+line_species2_MAS)+(species1_penlt_number*penlt)+(species2_penlt_number*penlt)+(head_penlt_number*penlt) 
    
    
    F1=np.array([F,0])
    F1=np.array_str(F1)
    x=np.array_str(x)
    y=np.array_str(y)
    
    #fid=open('Optimization_File_PSO.txt', 'a')
    fid=open('Optimization_File_ABC.txt', 'a')
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
    
    
    
    
    
    
    
    
    
    
    
