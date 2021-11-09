from flask_login import UserMixin
from sqlalchemy.sql.functions import current_date
from sqlalchemy.sql.schema import ForeignKeyConstraint
from sqlalchemy.sql.sqltypes import Boolean, DateTime
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()
from . import db
meta.create_all(engine)
class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True) 
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(1000))
	username = db.Column(db.String(1000), unique=True)
	firstname = db.Column(db.String(1000))
	lastname = db.Column(db.String(1000))

user_info = Table (
    'user_info', meta,
	Column('username', String(20), primary_key = True),
	Column('first_name', String(100), nullable=False),
	Column('last_name', String(100), nullable=False),
	Column('email', String(60), nullable=False),#,/*constra(db.Integer,to contain @students.ccu.edu*/
	#CONSTRA(db.Integer,ccu_email CHECK (email LIKE '%students.ccu.edu'),
	Column('password', String(64), nullable=False),
	Column('public_or_private', Boolean),
	Column('created_date', DateTime, nullable=False, default=current_date),#DEFAULT NOW() /* Defaults to the date the row was created */);
)
post_permission = Table (
	'post_permission', meta,
	Column ('post_permissionID', Integer, primary_key = True, auto_increment = True),
	Column('setting', String(60), nullable=False),
	Column('setting_description', String(140), nullable=False),
	Column('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
 )
group_category= Table (
	'group_category', meta,
	Column ('categoryID', Integer, primary_key = True, auto_increment = True),
	Column ('category_name', String(60), unique=True, nullable=False),
	Column ('category_description', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */
)
group_role = Table  (
	'group_role', meta,
	Column ('group_roleID', Integer, primary_key = True, auto_increment = True),
	Column ('role_name', String(60), unique=True, nullable=False),
	Column ('role_description', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */
)
school = Table  (
    'school', meta,
	Column ('schoolID', Integer, primary_key = True, auto_increment = True),
	Column ('school_name', String(60), unique=True, nullable=False),
	Column ('school_description', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date)# /* Defaults to the date the row was created */
)
major = Table  (
    'major', meta,
	Column ('majorID', Integer, primary_key = True, auto_increment = True),
	Column ('schoolID', Integer, auto_increment = True),#school ForeignKey('main_table.id')
	Column ('major_name', String(60), unique=True, nullable=False),
	Column ('major_description', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['schoolID'],['school.schoolID'], onupdate="CASCADE", ondelete="CASCADE")
)
direct_message = Table(
	'dm' , meta,
	Column ('message_ID', Integer, primary_key = True, auto_increment = True),
	Column ('senderID', String(20)),#user_info
	Column ('recipientID', String(20)),#user_info
	Column ('content', String(140), nullable= False),
	Column ('read', Boolean, default=False),
	ForeignKeyConstraint(['senderID','recipientID'],['user_info.username','user_info.username'], onupdate="CASCADE", ondelete="CASCADE"),
	ForeignKeyConstraint(['recipientID'],['user_info.username'], onupdate="CASCADE", ondelete="CASCADE")

)
group_info = Table  (
	'group_info', meta,
	Column ('groupID', Integer, primary_key = True, auto_increment = True),
	Column ('categoryID', Integer),
	Column ('group_name', String(20), nullable=False),
	Column ('group_description', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['categoryID'],['group_category.categoryID'], onupdate="CASCADE", ondelete="CASCADE")
)
post = Table  (
	'post', meta,
	Column ('postID', Integer, primary_key = True, auto_increment = True),
	Column ('username', String(20)),
	Column ('content', String(20), nullable=False),
	Column ('caption', String(140), nullable=False),
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['username'],['user_info.username'], onupdate="CASCADE", ondelete="CASCADE")
)
group_posted = Table  (
	'group_posted', meta,
	Column ('group_postedID', Integer, primary_key = True, auto_increment = True),
	Column ('postID', Integer),#post
	Column ('groupID', Integer),#group
	Column ('post_permissionID', Integer),#post_permission
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['postID'],['post.postID']),
	ForeignKeyConstraint(['groupID'],['group_info.groupID']),
	ForeignKeyConstraint(['post_permissionID'],['post_permission.post_permissionID'])


)
group_inclusion = Table  (
	'group_inclusion', meta,
	Column ('group_inclusionID', Integer, primary_key = True, auto_increment = True),
	Column ('username', String(20)),#post
	Column ('groupID', Integer),#group
	Column ('group_roleID', Integer),#group_role
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['username'],['user_info.username'], onupdate="CASCADE", ondelete="CASCADE"),
	ForeignKeyConstraint(['groupID'],['group_info.groupID'], onupdate="CASCADE", ondelete="CASCADE"),
	ForeignKeyConstraint(['group_roleID'],['group_role.group_roleID'], onupdate="CASCADE", ondelete="CASCADE")

)
biographical_information = Table  (
    'biographical_information', meta,
	Column ('biographical_informationID', Integer, primary_key = True, auto_increment = True),
	Column ('username', String(20), auto_increment = True),
	Column ('birthdate', DateTime, unique=True, nullable=True),
	Column ('major_ID', Integer, nullable=True),#major
	Column ('grad_year', Integer, nullable=True),#constaint
	Column ('user_bio', String(140), nullable=True),
	Column ('created_date',DateTime, nullable=False, default=current_date),# /* Defaults to the date the row was created */
	ForeignKeyConstraint(['username'],['user_info.username'], onupdate="CASCADE", ondelete="CASCADE"),
	ForeignKeyConstraint(['major_ID'],['major.majorID'], onupdate="CASCADE", ondelete="CASCADE")
)