class Configuration(object):
	Debug = True
	use_reloader=True
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/test1'