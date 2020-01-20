from firebase import firebase

from Firebase import firebaseAddress


class ViewData:
    view = firebaseAddress.Address.address
    def viewData(self,data):
        data = '-Lyti4Og3LDziPJytkx1'
        result = self.view.get('/prod-project-c3a7b/Test/',data)
        print(result)
        return result

view = firebaseAddress.Address.address
result = view.get('/prod-project-c3a7b/Test/','demo')
print(result)