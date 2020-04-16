import json

id_file = open('streamlink_master_id.txt', 'r')
link_file = open('streamlink_master_list.txt', 'r')

id = id_file.readline().strip()
link = link_file.readline().strip()

json_file =  open('ids_links.json', 'w')

d = {}

while (id):
	d[id] = link
	id = id_file.readline().strip()
	link = link_file.readline().strip()

#print(d)	

json_file.write(json.dumps(d))

