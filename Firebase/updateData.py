from firebase import firebase

from Firebase import firebaseAddress, viewData


class UpdateData:
    Update=firebaseAddress.Address.address
    id='-Lyti4Og3LDziPJytkx1'
    data=viewData.ViewData.viewData(data=None)

    print(data)

    query = '/prod-project-c3a7b/Test/' + id

    gainname=(data.pop('name'))

    updatedName = 'gaurang'

    data = {
        'name': 'xyz',
        'email': 'xyz@gmail.com',
        'phone': '31569715791'

    }

    print(query)
    print(Update.put(query,''+gainname+'',''+updatedName+''))
    print("value update")