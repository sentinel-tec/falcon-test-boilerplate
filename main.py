# main.py for trainer

import falcon
import os
import json
import traceback
import logging
import socket
import request

hostname = socket.gethostname()
logger_config = json.load(open('./logger_config.json'), encoding='utf-8')
if not os.path.exists('./log'):
    os.makedirs('./log')

info_logger = logging.getLogger('info')
error_logger = logging.getLogger('error')
warning_logger = logging.getLogger('warning')

'''
toutiao top 10 news responder
'''

class NewsResponder(object):
    
    def on_get(self, req, res):
        try: 
            new_num = req.params['news_num']

            res.status = falcon.HTTP_200
            res.body = json.dumps({
                'training_status': training_status,
                'status': {
                    'code': 200,
                    'is_error': False,
                    'error_message': ''
                }
            }, ensure_ascii=False)
            return

        except:
            res.status = falcon.HTTP_500
            res.body = json.dumps({
                'message': "Cannot fetch news",
                'status': {
                    'code': 500,
                    'is_error': True,
                    'error_message': "cannot fetch news"
                }
            }, ensure_ascii=False)

api = falcon.API(media_type='application/json')

api.add_route('/topNews', NewsResponder())