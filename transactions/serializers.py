from rest_framework import serializers

from transactions.models import Transaction


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


# JSON da request:
# {
#     "products": [  ==> essa tem que fazer na mão
#         {
#             "id": "uuid",
#             "quantity": 1
#         },
#     ],
#     "payment": {    ==> acredito que o django consiga fazer essa validação sozinho
#         "id": "uuid"
#     }
# }
