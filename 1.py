host = "http://slidevault-demo/"
public_key = "f123f526-ffdc-43f0-9e06-0ade63686c85"
private_key = "0cbb5496-de80-4007-b253-03aed40a4bb7"
from cytomine import Cytomine
from cytomine.utilities.descriptor_reader import read_descriptor
with Cytomine(host, public_key, private_key) as c:
	read_descriptor("descriptor.json")