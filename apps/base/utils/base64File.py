from drf_extra_fields.fields import Base64FileField
from apps.base.exceptions import HttpException

class PDFBase64File(Base64FileField):
    ALLOWED_TYPES = ['pdf','csv', 'xls', 'xlsx']

    def get_file_extension(self, filename, decoded_file):
        try:
            allowedExtensions = ['data:text/csv', 'data:application/pdf', 'data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
            for index, x in enumerate(allowedExtensions):
                if self.context['request'].data[f'{self.field_name}'].find(x) == 0:
                    match index:
                        case 0:
                            return 'csv'
                        case 1:
                            return 'pdf'
                        case 2:
                            return 'xlsx'
                else:
                    raise HttpException(400, 'formato invalido')
        except Exception as e:
            return 'pdf'