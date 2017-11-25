#
#
# # from sqlalchemy.schema import UniqueConstraint
# from sqlalchemy import Table, Column, Integer, String, VARCHAR, LargeBinary, UnicodeText
#
from swimteam_server.extensions import DB
# from flask_easy_model import get_model
# #
# #
# # Model = get_model(DB)
#
#
# # class ServiceType(DB.Model):
# #
# #     __tablename__ = "service_types"
# #
# #     id = DB.Column(DB.Integer, primary_key=True)
# #     name = DB.Column(DB.String(128), nullable=False, unique=True) # computer friendly: mini, full_interior, full_detail, full_detail_w_compound
# #     display_name = DB.Column(DB.String(128), nullable=False) # Mini, Full Interior, etc
# #     description = DB.Column(DB.Text(), nullable=False) # example for mini: "Wash with vacuum, windows inside and out, tire shine, ..."
# #     available_services_ref = DB.relationship('AvailableService', backref='ServiceType', lazy='joined')
# #
# #     def __init__(self, name, display_name, description):
# #         self.name = name
# #         self.display_name = display_name
# #         self.description = description
#
#
class User(DB.Model):

    __tablename__ = "users"

    id = DB.Column(DB.Integer, primary_key=True)
    email = DB.Column(DB.String(250), nullable=False, unique=True)
    password = DB.Column(DB.String(250), nullable=False)
