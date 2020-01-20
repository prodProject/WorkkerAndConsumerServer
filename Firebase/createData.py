from firebase import firebase

from Firebase import firebaseAddress
from Firebase.firebaseFileUploderAndDownloader import FirebaseFileUploaderAndDownloader

# firebase = firebase.FirebaseApplication("https://prod-project-c3a7b.firebaseio.com/",None)
class CreateData:
    create = firebaseAddress.Address.address

    data = {
        'name': 'xyz',
        'email': 'xyz@gmail.com',
        'phone': '31569715791'

    }
    result = create.patch("/prod-project-c3a7b/Test/demo", data)

    print(result)

