from pymongo import MongoClient

client = MongoClient()
db = client.myfirstdb
cursor = db.countries_data.find({"name":"Canada"})


def ad_country():
	db.countries_data.insert(
			   [{"name":"Canada"},
			    {"name":"Canada"},
			    {"name":"Pakistan"},
			    {"name":"India"}
			])

def update():
	db.countries_data.update({'name':'Italy'},{'$set':{'name':'ashish'}})

def get_country():
	for doc in cursor:
		print doc

if __name__ == "__main__":
	#ad_country()
	#update()
	get_country()
