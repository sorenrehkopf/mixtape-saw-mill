import logging
import logging.handlers
from os import environ
from flask import Flask
from flask import request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, origins=['https://www.myxtape-dev.io'])

handler = logging.handlers.SysLogHandler(address=('logsene-receiver-syslog.sematext.com', 514))
            
formater = logging.Formatter("%(logsene_token)s:%(message)s")
handler.setFormatter(formater)
logger = logging.getLogger("LogseneLogger")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
print(environ['LOGSENE_LOGGING_TOKEN']);
logger = logging.LoggerAdapter(logger, {'logsene_token': environ['LOGSENE_LOGGING_TOKEN']})

@app.route('/', methods=['POST'])
def mill_logs():
	content = request.get_json()
	print(request, content);
	# logger.info(content)
	return '{ "data": "success" }', 200

if __name__ == "__main__":
	app.run(port=5000)

