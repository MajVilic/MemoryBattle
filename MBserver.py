import falcon
import mainapi


api = application = falcon.API()

companies = mainapi.companies()
results = mainapi.allresult()
login = mainapi.login()
scrt = mainapi.scrt()


api.add_route('/poskus', companies)
api.add_route('/rezultati', results)
api.add_route('/login', login)
api.add_route('/scrt', scrt)