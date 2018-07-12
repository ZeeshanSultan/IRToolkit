import osquery

instance = osquery.SpawnInstance()
instance.open()

NSA_mitigation_top_10 = {
	"OS_Version": "select * from os_version;",
	"CPU_Features": "select * from cpuid;",
	"Secure_Boot": "SELECT * FROM registry WHERE key='HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\SecureBoot';",
}

# Returns Query Data or Error
def execute_query(query):
	data = instance.client.query(query)
	if data.status.code != 1:
		return data.response
	else:
		print(data.status.message)
		return False


#Maps Keys with values as result dict
def fetch_details(platform):
	results = {}
	for name,query in platform.iteritems():
		results[name] =  execute_query(query)
	return results


def cpu_features_extraction(cpuid):
	features = {}
	for data in cpuid:
		features[data["feature"]] = data["value"]
	return features


#Fetching Results
results = fetch_details(NSA_mitigation_top_10)

#Parsing Results
cpu_features = cpu_features_extraction(results["CPU_Features"])
os_version = results["OS_Version"][0]["version"]
os_version = float(".".join(os_version.split(".")[0:2])) #Making the version a float for processing
secure_boot = results["Secure_Boot"][0]
os_arch = results["OS_Version"][0]