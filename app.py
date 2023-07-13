class Barber:

    all=[]
    
    def __init__(self,fname,lname,date_hired,phone):
        self.fname=fname
        self.lname=lname
        self.date_hired=date_hired
        self.phone=phone
        self.all.append(self)
        self.id=len(Barber.all)

    @property
    def fname(self):
        return self._fname
    
    @fname.setter
    def fname(self,fname):
        if(type(fname)!=str):
            raise ValueError("First name must be a string")
        self._fname=fname

    @property
    def lname(self):
        return self._lname
    
    @lname.setter
    def lname(self,lname):
        if(type(lname)!=str):
            raise ValueError("Last name must be a string")
        self._lname=lname

    def get_appointments(self):
        return [appointment for appointment in Appointment.all if appointment.barber_id==self.id]

    def get_clients_by_hair_cut(self,cut_style):
        client_ids=[appointment.client_id for appointment in Appointment.all if cut_style==appointment.cut_style]
        clients=[]
        for client_id in client_ids:
            clients.append(Client.get_client_by_id(client_id))
        return clients
    
    def get_appointments_by_date(self,date):
        return [appointment for appointment in self.get_appointments() if date==appointment.date]

    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} first name={self.fname} last name={self.lname} date hired={self.date_hired} phone={self.phone} />"

class Client:
    
    all=[]

    def __init__(self,fname,lname,phone,email):
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.email=email
        self.all.append(self)
        self.id=len(Client.all)

    def book_appointment(self,barber,date,cut_style,price):
        Appointment(self.id,barber.id,date,cut_style,price)

    @classmethod
    def get_client_by_id(cls,id):
        for client in cls.all:
            if(client.id==id):
                return client
    
    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} first name={self.fname} last name={self.lname} phone={self.phone} email={self.email}  />"

class Appointment:

    all=[]
    
    def __init__(self,client_id,barber_id,date,cut_style,price):
        self.client_id=client_id
        self.barber_id=barber_id
        self.date=date
        self.cut_style=cut_style
        self.price=price
        self.all.append(self)
        self.id=len(Appointment.all)

    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} client id={self.client_id} barber id={self.barber_id} date={self.date} cut style={self.cut_style} price={self.price}  />"



manuel=Barber("Manuel","Garcia","07-12-2023","779-343-3434")
bob=Client("Bob","Miller","343-343-3434","millerb@gmail.com")
steve=Client("Steve","Smith","993-333-4343","smiths@gmail.com")

bob.book_appointment(manuel,"07-25-2023","spike",20)
bob.book_appointment(manuel,"07-30-2023","regular",7)
steve.book_appointment(manuel,"07-30-2023","spike",20)
print(manuel.get_clients_by_hair_cut("spike"))
print()
print(manuel.get_appointments_by_date("07-30-2023"))

