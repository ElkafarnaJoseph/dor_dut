# # Blog Flask application
#
# import os
# import psycopg2
# import psycopg2.extras
# from flask import Flask, request, render_template, g
#
# # PostgreSQL IP address
# # IP_ADDR = 'localhost'
#
# # Create the application
# app = Flask(__name__)
#
#
# #####################################################
# # Database handling
#
# def connect_db():
#     """Connects to the database."""
#     debug("Connecting to DB.")
#     conn = psycopg2.connect(host='localhost', user="postgres", password="postgres", dbname="blogdb",
#                             cursor_factory=psycopg2.extras.DictCursor)
#     return conn
#
#
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     if not hasattr(g, 'pg_db'):
#         g.pg_db = connect_db()
#     return g.pg_db
#
#
# @app.teardown_appcontext
# def close_db(error):
#     """Closes the database automatically when the application
#     context ends."""
#     debug("Disconnecting from DB.")
#     if hasattr(g, 'pg_db'):
#         g.pg_db.close()
#
#
# ######################################################
# # Command line utilities
#
# def init_db():
#     db = get_db()
#     with app.open_resource('schema.sql', mode='r') as f:
#         db.cursor().execute(f.read())
#     db.commit()
#
#
# @app.cli.command('initdb')
# def init_db_command():
#     """Initializes the database."""
#     print("Initializing DB.")
#     init_db()
#
#
# #####################################################
# # Debugging
#
# def debug(s):
#     """Prints a message to the screen (not web browser)
#     if FLASK_DEBUG is set."""
#     if app.config['DEBUG']:
#         print(s)
#
# def populate_db():
#     db = get_db()
#     with app.open_resource('populate.sql', mode='r') as f:
#         db.cursor().execute(f.read())
#     db.commit()
#
# ####################################################
# # Routes
#
# @app.route("/dump")
# def dump_entries():
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute('select id, date, title, content from entries order by date')
#     rows = cursor.fetchall()
#     output = ""
#     for r in rows:
#         debug(str(dict(r)))
#         output += str(dict(r))
#         output += "\n"
#     return "<pre>" + output + "</pre>"
#
# @app.cli.command('populate')
# def populate_db_command():
#     """Populates the database with sample data."""
#     print("Populating DB with sample data.")
#     populate_db()
#
#
# @app.route("/browse")
# def browse():
#     db = get_db()
#     cursor = db.cursor()
#     cursor.execute('select id, date, title, content from entries order by date')
#     rowlist = cursor.fetchall()
#     return render_template('browse.html', entries=rowlist)