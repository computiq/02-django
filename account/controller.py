from ninja import Router, Schema

account_controller = Router()

'''
GET /resources?name=Layth&age=39   # query parameter
GET /resources/{id}   # path parameter
POST /resources
PUT /resources/{id}
DELETE /resources/{id}

# body
{} - json object
'''

data = [
    {'name': 'Layth', 'age': 39},
    {'name': 'Suhaib', 'age': 90},
]


class DataSchema(Schema):
    name: str
    age: int


@account_controller.get('')
def list_accounts(request, index: int):
    if index:
        return data[index]
    return data


@account_controller.get('{index}')
def retrieve_account(request, index: int):
    return data[index]


@account_controller.post('')
def create_account(request, data_in: DataSchema):
    return data_in.dict()
