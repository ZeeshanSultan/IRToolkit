from exfiltrator import *

#Checking SMEP


def check_smep():
	smep_hw = 0
	smep_sw = 0
	if cpu_features["smep"] == '1':
		smep_hw = 1
		print "SMEP supported by hardware"
	if os_version >= 6.2:
	    smep_sw = 1
	    print "SMEP supported by Operating System"


def check_smap():
	smap_hw = 0
	smap_sw = 0
	if cpu_features["smap"] == '1':
		smap_hw = 1
		print "SMAP supported by hardware"
	if os_version >= 6.3:
		smap_sw = 1
		print "SMAP supported by Operating System"


def check_uefi():
	uefi_hw = 0
	uefi_sw = 0
	####UEFI Hardware implementation left
	if os_version >= 6.2:
		uefi_sw = 1
		print "UEFI supported by Operating System"
	#### Secure Boot Check to be implemented


def check_font_blocking():
	fb_os_ver = 0
	fb_os_conf = 0
	if os_version >= 10:
		fb_os_ver = 1
		print "Font Blocking supported by Operating System"
	#FontBlocking Options to be implemented when tested on win10


def check_dep():
    dep_hw = 0
    dep_sw = 0
    if os_version > 5.2:
        print "DEP supported by Operating System"
    if cpu_features["pae"] == "1":### Further checks to be implemented
    	print "DEP Supported by Operating System"

#########Business Logic
#'''
check_smep()
check_smap()
check_uefi()
check_font_blocking()
check_dep()
'''
#print(secure_boot[0])
print(os_arch)
#'''