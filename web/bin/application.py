#!/usr/bin/env python

import tornado.ioloop
import tornado.web
import tornado.template

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		loader = tornado.template.Loader("../templates/")
		return loader.load("home.html").generate(title="x")

application = tornado.web.Application([
	(r"/", MainHandler),
])

if __name__ == "__main__":
	application.listen(1337)
	tornado.ioloop.IOLoop.instance().start()