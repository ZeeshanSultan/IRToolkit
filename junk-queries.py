win_queries = {
        'timestamp': "select timestamp from time",
        "ASLR_Config": "select * from registry where key='HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\moveImages'",
        "Kernel_Version": "select version from kernel_info",
        "Chrome_Extensions": "select * from users join chrome_extensions using (uid);",
        "OS_Version": "select * from os_version;",
        #"Drives": "select * from mounts;",
        #"Firefox_Addons": "select * from users join firefox_addons using (uid)",
        #"Installed_Programs": "select * from programs;"
        "Installed_Patches": "select * from patches;",
        "Drivers": "select * from drivers;",
        }