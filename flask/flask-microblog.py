# -----------------------------------------------------------
# flask microblog example application
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required modules
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# initialize the application and derive configuration
application = Flask(__name__)
application.config.from_object(__name__)

# load default configuration and override configuration from an
# environment variable
application.config.update(dict(
	DATABASE=os.path.join(application.root_path, 'flask-microblog.db'),
	DEBUG=True,
	SECRET_KEY='development key',
	USERNAME='admin',
	PASSWORD='default'
))
application.config.from_envvar('FLASK_MICROBLOG_SETTINGS', silent=True)

# define subroutines
def connectDb():
	"connects to the specified database"
	database = application.config['DATABASE']
	databaseHandle = sqlite3.connect(database)

	databaseHandle.row_factory = sqlite3.Row
	return databaseHandle

def initDb():
	"initialize the sqlite database"
	with application.app_context():
		database = getDb()
		# read sql command from file
		with application.open_resource("schema.sql", mode="r") as f:
			# execute sql command
			database.cursor().executescript(f.read())
		# commit sql action
		database.commit()
	return

def getDb():
	"open a database connection if there is none yet for the current application context"
	if not hasattr(g, "sqlite_db"):
		g.sqlite_db = connectDb()

	return g.sqlite_db

@application.route("/")
def showEntries():
	# display the blog entries
	database = getDb()
	
	# define sql command: all entries in descending order
	sqlCommand = "select title, text from entries order by id desc"
	
	# execute the sql command as defined above
	current = database.execute(sqlCommand)

	# fetch items from the database
	entries = current.fetchall()

	# return the rendered template
	return renderTemplate("show_entries.html", entries=entries)

@application.teardown_appcontext
def closeDb(error):
	"closes database connection"
	if hasattr(g, "sqlite_db"):
		g.sqlite_db.close()
	return

# run application
if __name__ == "__main__":
	# initialize the database
	initDb()

	# run the application
	application.run()