
class recipe():

    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email

    def login(self):
        #check name and password fields
        #go to another page when click submit
        if request.method == 'POST':
            if request.data['name'] == str and request.data['password'] == str:
                return render_templates('recipe categories.html')
        else:
            print('Enter your name')
            return render_templates('signup.html')


    def register(self):
        if request.method == 'POST':
            if request.data['name'] == str and request.data['password'] == str and request.data['email'] == str:
                return render_templates('recipe categories.html')
        else:
            #return (Enter your name and password)
            print('Enter your name')
            return render_templates('signup.html')

    def register_view(self):
        return render_templates('individual recipes.html')

    def login_view(self):
        return render_templates('individual recipes.html')

    def recipe_view(self):
        return render_templates('create recipe.html')
        



