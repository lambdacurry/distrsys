from bottle import get, post, run, request

group = [{"name": "Nikita Smirnov", "citiz" : "Russia", "status" : "student"},
         {"name": "Thuc Nhat Truong Huynh", "citiz" : "Vietnam", "status" : "student"}
        ]

@get('/')
def get_info():
	return {'My group consists of:': group}

@post('/info')
def add_new():
	new = {"name" : request.json.get("name"), "citiz" : request.json.get("citiz"), 
	       "status" : request.json.get("status")}
	#
	'''
	to run in cmd:
    curl -d '{"name": "Valentin Poirot", "citiz" : "German", "status" : "tutor"}' 
    -H "Content-Type: application/json" -X POST http://localhost:8090/info
    '''
    #
	group.append(new)
	return{'Now my group consists of:': group}

run(host='localhost', port=8090, debug=True, reloader=True)