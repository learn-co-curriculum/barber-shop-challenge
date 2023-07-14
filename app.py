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
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(type(id)!=int):
            raise ValueError("Id must be an integer")
        self._id=id
    
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

    @property
    def date_hired(self):
        return self._date_hired
    
    @date_hired.setter
    def date_hired(self,date_hired):
        if(type(date_hired)!=str):
            raise ValueError("Date hired must be a string")
        self._date_hired=date_hired

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,phone):
        if(type(phone)!=str):
            raise ValueError("Phone must be a string")
        self._phone=phone

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

    @classmethod
    def get_barber_by_id(cls,id):
        for barber in cls.all:
            if(barber.id==id):
                return barber
    
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

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(type(id)!=int):
            raise ValueError("Id must be an integer")
        self._id=id

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

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self,phone):
        if(type(phone)!=str):
            raise ValueError("Phone must be a string")
        self._phone=phone

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self,email):
        if(type(email)!=str):
            raise ValueError("Email must be a string")
        self._email=email

    def book_appointment(self,barber,date,cut_style,price):
        Appointment(self.id,barber.id,date,cut_style,price)

    def get_appointments(self):
        return [appointment for appointment in Appointment.all if appointment.client_id==self.id]
    
    def get_barbers(self):
        appointments=self.get_appointments()
        barber_ids=[appointment.barber_id for appointment in appointments]
        barbers=[]
        for barber_id in barber_ids:
            barbers.append(Barber.get_barber_by_id(barber_id))
        return list(set(barbers))

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

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(type(id)!=int):
            raise ValueError("Id must be an integer")
        self._id=id

    @property
    def client_id(self):
        return self._client_id
    
    @client_id.setter
    def client_id(self,client_id):
        if(type(client_id)!=int):
            raise ValueError("Client id must be an integer")
        self._client_id=client_id

    @property
    def barber_id(self):
        return self._barber_id
    
    @barber_id.setter
    def barber_id(self,barber_id):
        if(type(barber_id)!=int):
            raise ValueError("Barber id must be an integer")
        self._barber_id=barber_id

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self,date):
        if(type(date)!=str):
            raise ValueError("Date must be a string")
        self._date=date

    @property
    def cut_style(self):
        return self._cut_style
    
    @cut_style.setter
    def cut_style(self,cut_style):
        if(type(cut_style)!=str):
            raise ValueError("Cut style must be a string")
        self._cut_style=cut_style

    @classmethod
    def get_barbers_with_appointments(cls):
        barber_ids=[appointment.barber_id for appointment in cls.all]
        barbers=[]
        for barber_id in barber_ids:
            barbers.append(Barber.get_barber_by_id(barber_id))
        return list(set(barbers))
    
    @classmethod
    def get_clients_with_appointments(cls):
        client_ids=[appointment.client_id for appointment in cls.all]
        clients=[]
        for client_id in client_ids:
            clients.append(Client.get_client_by_id(client_id))
        return list(set(clients))

    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} client id={self.client_id} barber id={self.barber_id} date={self.date} cut style={self.cut_style} price={self.price}  />"



manuel=Barber("Manuel","Garcia","07-12-2023","779-343-3434")
bob=Client("Bob","Miller","343-343-3434","millerb@gmail.com")
steve=Client("Steve","Smith","993-333-4343","smiths@gmail.com")

bob.book_appointment(manuel,"07-25-2023","spike",20)
bob.book_appointment(manuel,"07-30-2023","regular",7)
#steve.book_appointment(manuel,"07-30-2023","spike",20)

print()
print(Appointment.get_barbers_with_appointments())
print(Appointment.get_clients_with_appointments())

