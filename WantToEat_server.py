import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import pymongo

settings = {
    "cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
    "login_url": "/login",
    "xsrf_cookies": False,
    "debug":True
}

class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")

class MainHandler(BaseHandler):
    def get(self):
        self.write("Hello, world")

class LoginHandler(BaseHandler):
    def get(self):
        if self.get_current_user():
            self.redirect('/stage')
            return
        self.render("login.html",title='login page',state='You can login now')

    def post(self):
        if self.get_current_user():
            self.redirect('stage')
            return
        name=self.get_arguments("name")
        password=self.get_arguments("password")
        conn = pymongo.Connection("localhost", 27017)
        db=conn.test
        User_list=db.User
        User = User_list.find_one({"name":name[0]})
        if User:
            if(User['password']==password[0]):
                self.write('Login Success')
                self.set_secure_cookie("user",name[0])
                self.redirect("/stage")
            else:
                 self.render("login.html",title='login page',state='Your password is wrong')
        else:
            self.render("login.html",title='login page',state='User not found')

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect("/login")
        return

class StageHandler(BaseHandler):
    def get(self):
        self.render("stage.html",title="my stage",user_name=self.get_current_user())

application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/login",LoginHandler),
    (r"/logout",LogoutHandler),
    (r"/stage",StageHandler)
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
 
