from flask_restx import Namespace , Resource , fields







USER_FIELDS = {
      'uuid': fields.String(), 
      'first_name' : fields.String(required=True , description='First Name'),
      'last_name' : fields.String(required=True , description='Last Name'),
      'email' : fields.String(required=True , description='An email address'), 
      'created_at' : fields.DateTime()
   }

USER_REGISTRATION_FIELDS = {
      # 'first_name' : fields.String(required=True , description='First Name'),
      # 'last_name' : fields.String(required=True , description='Last Name'),
      'email' : fields.String(required=True , description='An email address'),
      'password' : fields.String(required=True , description='A password'),
   }

LOGIN_FIELDS =  {
      'email' : fields.String(required=True , description='User email address'),
      'password' : fields.String(required=True , description='User password'),
   }