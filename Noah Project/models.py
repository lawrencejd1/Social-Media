from flask_login import UserMixin
from sqlalchemy.sql.functions import current_date
from sqlalchemy.sql.schema import ForeignKey, ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()
from . import db
meta.create_all(engine)
class User(UserMixin, db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True) 
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(1000))
	username = db.Column(db.String(1000), unique=True)
	firstname = db.Column(db.String(1000))
	lastname = db.Column(db.String(1000))
	created_date = db.Column(db. DateTime, nullable=False, default=current_date),#DEFAULT NOW() /* Defaults to the date the row was created */);

class post_permission( db.Model):
	post_permissionID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	setting = db.Column(db.String(60), nullable=False),
	setting_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class group_category( db.Model):
	categoryID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	category_name = db.Column(db.String(60), unique=True, nullable=False),
	category_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */
class group_role( db.Model):
	group_roleID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	role_name = db.Column(db.String(60), unique=True, nullable=False),
	role_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */
class school( db.Model):
	schoolID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	school_name = db.Column(db.String(60), unique=True, nullable=False),
	school_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */

class major( db.Model):
	majorID = db.Column(db.Integer, primary_key = True, auto_increment = True, ),
	schoolID = db.Column(db.Integer, ForeignKey(school.schoolID)),#school ForeignKey('main_table.id')
	major_name = db.Column(db.String(60), unique=True, nullable=False),
	major_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class direct_message( db.Model):
	message_ID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	senderID = db.Column(db.String(20),ForeignKey(User.username)),#user_info
	recipientID = db.Column(db.String(20),ForeignKey(User.username)),#user_info
	content = db.Column(db.String(140), nullable= False),
	read = db.Column(db. Boolean, default=False)

class group_info( db.Model):
	groupID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	categoryID = db.Column(db.Integer,ForeignKey(group_category.categoryID)),
	group_name = db.Column(db.String(20), nullable=False),
	group_description = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class post( db.Model):
	postID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	username = db.Column(db.String(20),ForeignKey(User.username)),
	content = db.Column(db.String(20), nullable=False),
	caption = db.Column(db.String(140), nullable=False),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class group_posted( db.Model):
	group_postedID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	postID = db.Column(db.Integer,ForeignKey(post.postID)),#post
	groupID = db.Column(db.Integer,ForeignKey(group_info.groupID)),#group
	post_permissionID = db.Column(db.Integer),#post_permission
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class group_inclusion( db.Model):
	group_inclusionID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	username = db.Column(db.String(20),ForeignKey(User.username)),#post
	groupID = db.Column(db.Integer,ForeignKey(group_info.groupID)),#group
	group_roleID = db.Column(db.Integer,ForeignKey(group_role.group_roleID)),#group_role
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */

class biographical_information( db.Model):
	biographical_informationID = db.Column(db.Integer, primary_key = True, auto_increment = True),
	username = db.Column(db.String(20),ForeignKey(User.username), auto_increment = True),
	birthdate = db.Column(db. DateTime, unique=True, nullable=True),
	major_ID = db.Column(db.Integer,ForeignKey(User.username), nullable=True),#major
	grad_year = db.Column(db.Integer, nullable=True),#constaint
	user_bio = db.Column(db.String(140), nullable=True),
	created_date = db.Column(db.DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */