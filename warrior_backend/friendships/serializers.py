from builtins import object
# from rest_framework import serializers

# class UserSerializer(object):
#     def __init__(self, user_body):
#         self.user_body = user_body

    # @property
    # def all_users(self):
    #     output = {'users': []}
    #     for user in self.user_body:
    #         user_details = {
    #             'username': user.username,
    #             'email': user.email,
    #             'password': user.password
    #         }
    #         output['users'].append(user_details)
    #     return output

#     @property
#     def user_detail(self):
#         return {
#             'username': self.user_body.username,
#             'email': self.user_body.email,
#             'password': self.user_body.password,
#         }

class RelationshipSerializer(object):
    def __init__(self, relationship_body):
        self.relationship_body = relationship_body

    @property
    def all_relationships(self):
        output = {'relationships': []}
        for relationship in self.relationship_body:
            relationship_details = {
                'user_one_id': relationship.user_one_id,
                'user_two_id': relationship.user_two_id,
                # 'user_id': relationship.user_id,
                'status': relationship.status,
                'action_user_id': relationship.action_user_id
            }
            output['relationships'].append(relationship_details)
        return output

    @property
    def relationship_detail(self):
        return {
            'user_one_id': self.relationship_body.user_one_id,
            'user_two_id': self.relationship_body.user_two_id,
            # 'user_id': self.relationship_body.user_id,
            'status': self.relationship_body.status,
            'action_user_id': self.relationship_body.action_user_id,
        }