# Program to determine volumes of solutions used in IF staining

print()
print ("----Welcome to the ICC/IF calculation program----")
print()

## User inputs:

# Number of coverslips
w = int(input ("Please enter the number of wells being used: "))
print ()

# Primary Antibody dilutions:
print ("Please select primary antibody #1 host species (Rb, M, G).")
ab_1_name = input("  Host: ")
ab_1_antigen = input("  Antigen: ")
ab_1 = int(input("  %s-anti-%s dilution: 1:" % (ab_1_name, ab_1_antigen)))
print ()

print ("Please select primary antibody #2 host species (Rb, M, G).")
ab_2_name = input("  Host: ")
ab_2_antigen = input("  Antigen: ")
ab_2 = int(input("  %s-anti-%s dilution: 1:" % (ab_2_name, ab_2_antigen)))
print ()

# Secondary Antibody dilutions:
print ("Please enter secondary antibody #1 host species (D, G).")
sec_ab_1_host = input("  Host: ")
sec_ab_1_flo = input("  Enter 3 digit wavelength (nm): ")
sec_ab_1_c1 = int(input("  %s-anti-%s-%s #1 stock concenctration (mg/ml): " % (sec_ab_1_host, ab_1_name, sec_ab_1_flo)))
sec_ab_1_c2 = int(input("  %s-anti-%s-%s #1 dilution (ug/ml): " % (sec_ab_1_host, ab_1_name, sec_ab_1_flo)))
print ()

print ("Please enter secondary antibody #2 host species (D, G).")
sec_ab_2_host = input("  Host: ")
sec_ab_2_flo = input("  Enter 3 digit wavelength (nm): ")
sec_ab_2_c1 = int(input("  %s-anti-%s-%s stock concenctration (mg/ml): " % (sec_ab_2_host, ab_2_name, sec_ab_2_flo)))
sec_ab_2_c2 = int(input("  %s-anti-%s-%s dilution (ug/ml): " % (sec_ab_2_host, ab_2_name, sec_ab_2_flo)))
print ()
print ()
print ("----Calculations----")
print ()
print ()

## Fixation calculations:

total_fix_vol = (0.5 * w + (0.1 * (0.5 * w))) 
print ("Total fixation buffer volume =", round(total_fix_vol, 4), "mL")

# 10X PBS vol:
fix_pbs = 0.1 * total_fix_vol
print ("  10X PBS volume =", round(fix_pbs, 4), "mL")

# Formaldehyde:
fix_form = ((4 * total_fix_vol) / 16)
print ("  16% PFA volume =", round(fix_form, 4), "mL")

# H2O:
fix_h2o = round((total_fix_vol - (fix_pbs + fix_form)), 4)
if fix_h2o > 1:
    fix_h2o_even = int(fix_h2o) + 1 # 2.4 mL = 2 + 1 = 3
    fix_h2o_frac = round((fix_h2o / fix_h2o_even), 4) # 2/3 = 0.6666
    print("  H2O volume = %s mL = %s uL x %s" % (round(fix_h2o, 4), fix_h2o_frac, fix_h2o_even)) # 2.4 mL = 0.6666 uL x 4
elif fix_h2o <= 1:
    print ("  H2O volume =", round(fix_h2o, 4), "mL")
print ()
    
## Quench calculations:
total_quench_vol = (2 * 0.5 * w) + 0.1 * (2 * 0.5 * w)
print ("Total quenching buffer volume =", round(total_quench_vol, 4), "mL")

# 10X PBS:
quench_pbs = 0.1 * total_quench_vol
print ("  10X PBS volume =", round(quench_pbs, 4), "mL")

# 1M Glycine:
quench_gly = 0.1 * total_quench_vol
print ("  1M Glycine volume =", round(quench_gly, 4), "mL")

# H2O:
quench_h2o = total_quench_vol - (quench_pbs + quench_gly)
if quench_h2o > 1:
    quench_h2o_even = int(quench_h2o) + 1 # 2.4 mL = 2 + 1 = 3
    quench_h2o_frac = round((quench_h2o / quench_h2o_even), 4) # 2/3 = 0.6666
    print("  H2O volume = %s mL = %s uL x %s" % (round(quench_h2o, 4), quench_h2o_frac, quench_h2o_even)) # 2.4 mL = 0.6666 uL x 4
elif quench_h2o <= 1:
    print ("  H2O volume =", round(quench_h2o, 4), "mL")
print()


## Permeabilization buffer calculations:
total_perm_vol = (0.5 * w) + (0.1 * (0.5 * w))
print ("Total permeabilization buffer volume =", round(total_perm_vol, 4), "mL")

# Detergent:
tri = (0.0025 * total_perm_vol)
print ("  Triton X-100 volume =", round((tri * 1000), 4), "uL")

# PBS:
perm_pbs = (total_perm_vol - tri)
if perm_pbs > 1:
    perm_pbs_even = int(perm_pbs) + 1 # 2.4 mL = 2 + 1 = 3
    perm_pbs_frac = round((perm_pbs / perm_pbs_even), 4) # 2/3 = 0.6666
    print("  PBS volume = %s mL = %s uL x %s" % (round(perm_pbs, 4), perm_pbs_frac, perm_pbs_even)) # 2.4 mL = 0.6666 uL x 4
elif perm_pbs <= 1:
    print ("  1X PBS volume =", round(perm_pbs, 4), "mL")
print ()

#det = input("Please input detergent used: Saponin or Triton? ")
#if det == "Saponin" or det == "saponin":
#    sap = (0.01 * total_perm_vol)
#    print ("10% Saponin volume =", round(sap, 4), "mL")
#    perm_pbs = (total_perm_vol - sap)
#    print ("1XPBS volume =", round(perm_pbs, 4), "mL")
#elif det == "Triton" or det == "triton":
#    tri = (0.01 * total_perm_vol)
#    print ("10% Triton volume =", round(tri, 2), "mL")
#    perm_pbs = (total_perm_vol - tri)
#    print ("1XPBS volume =", round(perm_pbs, 4), "mL")
#else:
#    print ("Detergent not recognized. Please input 'Saponin' or Triton'")
#print ()


## Blocking buffer calculations:
total_block_vol = (3 * 0.25 * w) + (0.1 * (3 * 0.25 * w))
print ("Total blocking buffer volume =", round(total_block_vol, 4), "mL")
print ()

#Saponin?
#if det == "Saponin" or det == "saponin":
#    block_sap = (0.01 * total_block_vol)

#Serum:
#serum = (0.025 * total_block_vol)
#print ("Serum volume =", round(serum, 4), "mL")

#Casein:
#if det == "Saponin" or det == "saponin":
#    casein = (total_block_vol - (block_sap + serum))
#    print ("Casein volume =", round(casein, 4), "mL")
#else:
#    casein = (total_block_vol - serum)
#    print ("Casein volume =", round(casein, 4), "mL")
#print ()


## Primary antibody calculations:

total_prim_ab = (0.25 * w) + (0.1 * 0.25 * w)
print ("Total primary antibody volume =", round(total_prim_ab, 4), "mL")

# Antibody 1:
ab_1_vol =  (total_prim_ab / ab_1)
print ("  %s-anti-%s volume for 1:%s dilution =" % (ab_1_name, ab_1_antigen, ab_1), round((ab_1_vol * 1000), 3), "uL")

# Antibody 2:
ab_2_vol =  (total_prim_ab / ab_2)
print ("  %s-anti-%s volume for 1:%s dilution =" % (ab_2_name, ab_1_antigen, ab_2), round((ab_2_vol * 1000), 3), "uL")

# Block:
ab_block = (total_prim_ab - (ab_1_vol + ab_2_vol))
if ab_block > 1:
    ab_block_even = int(ab_block) + 1 # 2.4 mL = 2 + 1 = 3
    ab_block_frac = round((ab_block / ab_block_even), 4) # 2/3 = 0.6666
    print("  Blocking buffer = %s mL = %s uL x %s" % (round(ab_block, 4), ab_block_frac, ab_block_even)) # 2.4 mL = 0.6666 uL x 4
elif perm_pbs <= 1:
    print ("  Blocking buffer =", round(ab_block, 4), "mL")
print()

## Secondary antibody calculations:
total_sec_ab = (0.25 * w) + 0.1 * (0.25 * w)
print ("Total secondary antibody volume =", round(total_sec_ab, 4), "mL")

# Secondary Antibody 1:
sec_ab_1_vol = (sec_ab_1_c2 * total_sec_ab) / (sec_ab_1_c1 * 1000)
print("  %s-anti-%s-%s volume for %s ug/ml dilution =" % (sec_ab_1_host, ab_1_name, sec_ab_1_flo, sec_ab_1_c2), round((sec_ab_1_vol * 1000), 3), "uL")

# Secondary Antibody 2:
sec_ab_2_vol = (sec_ab_2_c2 * total_sec_ab) / (sec_ab_2_c1 * 1000)
print("  %s-anti-%s-%s volume for %s ug/ml dilution =" % (sec_ab_2_host, ab_2_name, sec_ab_2_flo, sec_ab_2_c2), round((sec_ab_2_vol * 1000), 3), "uL")

# Block:
sec_ab_block = (total_sec_ab - (sec_ab_1_vol + sec_ab_2_vol))
if sec_ab_block > 1:
    sec_ab_block_even = int(sec_ab_block) + 1 # 2.4 mL = 2 + 1 = 3
    sec_ab_block_frac = round((sec_ab_block / sec_ab_block_even), 4) # 2/3 = 0.6666
    print("  Blocking buffer = %s mL = %s uL x %s" % (round(sec_ab_block, 4), sec_ab_block_frac, sec_ab_block_even)) # 2.4 mL = 0.6666 uL x 4
elif perm_pbs <= 1:
    print ("  Blocking buffer =", round(sec_ab_block, 4), "mL")
#DAPI calculations:
#answer = input("Using DAPI? ")
#if answer == "Yes" or answer == "yes":
#    total_dapi_vol = (0.25 * w) + 0.1 * (0.25 * w)
#    print ("Total DAPI volume =", round(total_dapi_vol, 4), "mL")
#    dapi = (total_dapi_vol / 1000)
#    print ("DAPI volume =", round(dapi, 4), "mL")
#    dapi_pbs = (total_dapi_vol - dapi)
#    print ("1X PBS volume =", round(dapi_pbs, 4), "mL")
#    print()
#    print ("Calculations complete.")
#else:
#    print()
#    print ("Calculations complete.")
print ()
print ()
print ("--------DONE-------")
print ()
print ()
