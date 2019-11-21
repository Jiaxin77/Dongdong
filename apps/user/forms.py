from django import forms
from user.models import Enterprise

#表单页 用于提交审核信息

#
# class InfoForm(forms.od):
#     class Meta:
#         model = Enterprise
#         fields = ('icon',)
#         error_messages = {
#             'icon': {
#                 'invalid_image': '请上传正确格式的图片！'
#             }
#         }