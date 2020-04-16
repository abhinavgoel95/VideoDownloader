import json
import argparse

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--id", help="id to change", type=str)
	parser.add_argument("--link", required = False, help="link to change to", type=str)
	args = parser.parse_args()

	json_file = open ('ids_links.json', 'r') 
	data = json.loads(json_file.read())
	print('before', data[args.id])
	if (args.link):
		data[args.id] = args.link
		print('after', data[args.id])

	json_file.close()
	json_file = open ('ids_links.json', 'w')

	json_file.write(json.dumps(data))
	json_file.close()
	
if __name__ == '__main__':
	main()
