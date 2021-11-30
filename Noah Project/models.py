from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy.sql.functions import current_date
from sqlalchemy.sql.schema import ForeignKey
from . import db

class User(UserMixin, db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True) 
	email = db.Column(db.String(1000), unique=True)
	password = db.Column(db.String(1000))
	username = db.Column(db.String(1000), unique=True)
	firstname = db.Column(db.String(1000))
	lastname = db.Column(db.String(1000))
	birthday = db.Column(db.String(20), nullable=True)
	major = db.Column(db.String(255), nullable=True)#major
	grad_year = db.Column(db.Integer, nullable=True)#constaint
	profile_picture = db.Column(db.BLOB, nullable=True)
	user_bio = db.Column(db.String(255), nullable=True)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

# ASK ABOUT THIS
# class post_permission( db.Model):
# 	post_permissionID = db.Column(db.Integer ,primary_key = True)
# 	setting = db.Column(db.String(60), nullable=False)
# 	setting_description = db.Column(db.String(140), nullable=False)
# 	created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */

class School(db.Model):
	schoolID = db.Column(db.Integer, primary_key = True)
	school_name = db.Column(db.String(60), unique=True, nullable=False)
	school_description = db.Column(db.String(140), nullable=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

# class major( db.Model):
# 	majorID = db.Column(db.Integer, primary_key = True)
# 	schoolID = db.Column(db.Integer, ForeignKey(school.schoolID))#school ForeignKey('main_table.id')
# 	major_name = db.Column(db.String(60), unique=True, nullable=False)
# 	major_description = db.Column(db.String(140), nullable=False)
# 	created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */

class Direct_Message(db.Model):
	message_ID = db.Column(db.Integer, primary_key = True)
	senderID = db.Column(db.String(20), ForeignKey(User.username))#user_info
	recipientID = db.Column(db.String(20), ForeignKey(User.username))#user_info
	content = db.Column(db.String(140), nullable= False)
	read = db.Column(db. Boolean, default=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

class Post(db.Model):
	postID = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), ForeignKey(User.username))
	image = db.Column(db.String(255), nullable=False)
	caption = db.Column(db.String(140), nullable=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

# class biographical_information( db.Model):
# 	biographical_informationID = db.Column(db.Integer, primary_key = True)
# 	username = db.Column(db.String(1000), ForeignKey(User.username))
	# birthdate = db.Column(db. DateTime, unique=True, nullable=True)
	# major_ID = db.Column(db.Integer, ForeignKey(User.username), nullable=True)#major
	# grad_year = db.Column(db.Integer, nullable=True)#constaint
	# user_bio = db.Column(db.String(140), nullable=True)
	# created_date = db.Column(db.DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */

class Group_Category(db.Model):
	categoryID = db.Column(db.Integer, primary_key = True)
	category_name = db.Column(db.String(60), unique=True, nullable=False)
	category_description = db.Column(db.String(140), nullable=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

class Group_Role(db.Model):
	group_roleID = db.Column(db.Integer, primary_key = True)
	role_name = db.Column(db.String(60), unique=True, nullable=False)
	role_description = db.Column(db.String(140), nullable=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

class Group(db.Model):
	groupID = db.Column(db.Integer, primary_key = True)
	categoryID = db.Column(db.Integer, ForeignKey(Group_Category.categoryID))
	group_name = db.Column(db.String(20), nullable=False)
	group_description = db.Column(db.String(140), nullable=False)
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

class Group_Post(db.Model):
	group_postedID = db.Column(db.Integer, primary_key = True)
	postID = db.Column(db.Integer, ForeignKey(Post.postID))#post
	groupID = db.Column(db.Integer, ForeignKey(Group.groupID))#group
	post_permissionID = db.Column(db.Integer)#post_permission
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())

class Group_Members( db.Model):
	group_inclusionID = db.Column(db.Integer, primary_key = True, unique=True)
	username = db.Column(db.String(20), ForeignKey(User.username))#post
	groupID = db.Column(db.Integer,ForeignKey(Group.groupID))#group
	group_roleID = db.Column(db.Integer,ForeignKey(Group_Role.group_roleID))#group_role
	created_date = db.Column(db.String(100), nullable=False, server_default=func.now())# /* Defaults to the date the row was created */
	updated_date = db.Column(db.String(100), onupdate=func.now())