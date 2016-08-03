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
print ("Please enter anti-%s secondary antibody host species (D, G)." % (ab_1_name))
sec_ab_1_host = input("  Host: ")
sec_ab_1_flo = input("  Enter 3 digit wavelength (nm): ")
sec_ab_1_c1 = int(input("  %s-anti-%s-%s stock concenctration (mg/ml): " % (sec_ab_1_host, ab_1_name, sec_ab_1_flo)))
sec_ab_1_c2 = int(input("  %s-anti-%s-%s dilution (ug/ml): " % (sec_ab_1_host, ab_1_name, sec_ab_1_flo)))
print ()

print ("Please enter anti-%s secondary antibody host species (D, G)." % (ab_2_name))
sec_ab_2_host = input("  Host: ")
sec_ab_2_flo = input("  Enter 3 digit wavelength (nm): ")
sec_ab_2_c1 = int(input("  %s-anti-%s-%s stock concenctration (mg/ml): " % (sec_ab_2_host, ab_2_name, sec_ab_2_flo)))
sec_ab_2_c2 = int(input("  %s-anti-%s-%s dilution (ug/ml): " % (sec_ab_2_host, ab_2_name, sec_ab_2_flo)))

print ()
print ()
print ("----Calculations----")
print ()
print ()


## Function for splitting volumes greater than 1 mL into < 1 mL factors for
## easy pipetting with P1000

def VolSplit(x):
    if x > 1:
        xEven = int(x) + 1 # For 2.5: 2 + 1 = 3. Note int() rounds down
        xFrac = round((x / xEven), 4) # 2.5 / 3 = 0.833
        print("    = %s mL x %s" % (xFrac, xEven)) # 2.5 = 0.833 uL x 3
    elif x <= 1:
        pass


## Fixation calculations:

total_fix_vol = (0.5 * w + (0.1 * (0.5 * w))) 
print ("Total fixation buffer volume =", round(total_fix_vol, 4), "mL")

# 10X PBS vol:
fix_pbs = 0.1 * total_fix_vol
print ("  10X PBS volume =", round(fix_pbs, 4), "mL")

# Formaldehyde:
fix_form = ((4 * total_fix_vol) / 16)
print ("  16% PFA volume =", round(fix_form, 4), "mL")
VolSplit(fix_form)

# H2O:
fix_h2o = round((total_fix_vol - (fix_pbs + fix_form)), 4)
print("  H20 Volume = %s mL" % (fix_h2o))
VolSplit(fix_h2o)
print()

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
quench_h2o = round(total_quench_vol - (quench_pbs + quench_gly), 4)
print("  H2O volume = %s mL" % (quench_h2o))
VolSplit(quench_h2o)
print()

## Permeabilization buffer calculations:
total_perm_vol = (0.5 * w) + (0.1 * (0.5 * w))
print ("Total permeabilization buffer volume =", round(total_perm_vol, 4), "mL")

# Detergent:
tri = (0.0025 * total_perm_vol)
print ("  Triton X-100 volume =", round((tri * 1000), 4), "uL")

# PBS:
perm_pbs = round((total_perm_vol - tri), 4)
print("  1X PBS volume = %s mL" % (perm_pbs))
VolSplit(perm_pbs)
print()

## Blocking buffer calculations:
total_block_vol = (3 * 0.25 * w) + (0.1 * (3 * 0.25 * w))
print ("Total blocking buffer volume =", round(total_block_vol, 4), "mL")
print ()


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
ab_block = round((total_prim_ab - (ab_1_vol + ab_2_vol)), 4)
print("  Blocking buffer = %s mL" % (ab_block))
VolSplit(ab_block)
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
sec_ab_block = round((total_sec_ab - (sec_ab_1_vol + sec_ab_2_vol)), 4)
print("  Blocking buffer = %s mL" % (sec_ab_block))
VolSplit(sec_ab_block)

print ()
print ()
print ("--------DONE-------")
print ()
print ()
