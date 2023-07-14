import sqlite3
DATABASE_URL="app.db"

class Barber:

    all=[]

    @classmethod
    def drop_table(cls):
        query="drop table if exists barbers;"
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)

    @classmethod
    def create_table(cls):
        query="""
                CREATE TABLE if not exists barbers(
                id integer primary key,
                fname text not null,
                lname text not null,
                date_hired text not null,
                phone text not null
                );
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)
        conn.close()
    
    def __init__(self,fname,lname,date_hired,phone,id=None):
        self.fname=fname
        self.lname=lname
        self.date_hired=date_hired
        self.phone=phone
        self.id=id
        self.all.append(self)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(id!=None and type(id)!=int):
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

    def save(self):
        Barber.create_table()
        query="""
                INSERT INTO barbers(fname,lname,date_hired,phone) values(?,?,?,?);
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        result=cursor.execute(query,(self.fname,self.lname,self.date_hired,self.phone))
        conn.commit()
        self.id=result.lastrowid

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
        query=f"""
                select * from appointments where barber_id=={self.id};
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query).fetchall()
        print(results)
        appointments=[]
        for result in results:
            appointment=Appointment(result[1],result[2],result[3],result[4],result[5],result[0])
            appointments.append(appointment)
        return appointments


    def get_clients_by_hair_cut(self,cut_style):
        query=f"""
                select distinct clients.id,clients.fname,clients.lname,clients.phone,clients.email from clients inner join appointments on clients.id==appointments.client_id and appointments.cut_style==? and appointments.barber_id=={self.id};
            """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query,(cut_style,)).fetchall()
        clients=[]
        for result in results:
            client=Client(result[1],result[2],result[3],result[4],result[0])
            clients.append(client)
        return clients

    
    def get_appointments_by_date(self,date):
        query=f"""
                select * from appointments where appointments.date==? and appointments.barber_id=={self.id};
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query,(date,)).fetchall()
        appointments=[]
        for result in results:
            appointment=Appointment(result[1],result[2],result[3],result[4],result[5],result[0])
            appointments.append(appointment)
        return appointments


    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} first name={self.fname} last name={self.lname} date hired={self.date_hired} phone={self.phone} />"

class Client:
    
    all=[]

    @classmethod
    def drop_table(cls):
        query="drop table if exists clients;"
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)

    @classmethod
    def create_table(cls):
        query="""
        CREATE TABLE if not exists clients(
            id integer primary key,
            fname text not null,
            lname text not null,
            phone text not null,
            email text not null
            );
        """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)

    def __init__(self,fname,lname,phone,email,id=None):
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.email=email
        self.id=id
        self.all.append(self)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(id!=None and type(id)!=int):
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

    def save(self):
        Client.create_table()
        query="""
                INSERT INTO clients(fname,lname,phone,email) values(?,?,?,?);
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        result=cursor.execute(query,(self.fname,self.lname,self.phone,self.email))
        conn.commit()
        self.id=result.lastrowid

    def book_appointment(self,barber,date,cut_style,price):
        Appointment.create_table()
        query="""
                Insert into appointments(client_id,barber_id,date,cut_style,price) values(?,?,?,?,?);
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query,(self.id,barber.id,date,cut_style,price))
        conn.commit()

    def get_appointments(self):
        query=f"""
                select * from appointments where appointments.client_id=={self.id};
            """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query).fetchall()
        appointments=[]
        for result in results:
            appointment=Appointment(result[1],result[2],result[3],result[4],result[5],result[0])
            appointments.append(appointment)
        return appointments
    
    def get_barbers(self):
        query=f"""
                select distinct barbers.id,barbers.fname,barbers.lname,barbers.date_hired,barbers.phone from barbers inner join appointments on barbers.id==appointments.barber_id and appointments.client_id=={self.id};
             """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query).fetchall()
        barbers=[]
        for result in results:
            barber=Barber(result[1],result[2],result[3],result[4],result[0])
            barbers.append(barber)
        return barbers

    @classmethod
    def get_client_by_id(cls,id):
        pass
    
    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} first name={self.fname} last name={self.lname} phone={self.phone} email={self.email}  />"

class Appointment:

    all=[]

    @classmethod
    def drop_table(cls):
        query="drop table if exists appointments;"
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)

    @classmethod
    def create_table(cls):
        query="""
        CREATE TABLE if not exists appointments(
            id integer primary key,
            client_id integer not null,
            barber_id integer not null,
            date text not null,
            cut_style text,
            price real not null,
            foreign key(client_id) references clients(id),
            foreign key(barber_id) references barbers(id)
            );
        """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        cursor.execute(query)
    
    def __init__(self,client_id,barber_id,date,cut_style,price,id=None):
        self.client_id=client_id
        self.barber_id=barber_id
        self.date=date
        self.cut_style=cut_style
        self.price=price
        self.id=id
        self.all.append(self)

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id):
        if(id!=None and type(id)!=int):
            raise ValueError("Id must be an integer")
        self._id=id

    @property
    def client_id(self):
        return self._client_id
    
    @client_id.setter
    def id(self,client_id):
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
        query="""
                select distinct barbers.id,barbers.fname,barbers.lname,barbers.date_hired,barbers.phone from barbers inner join appointments where barbers.id==appointments.barber_id;
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query).fetchall()
        print(results)
        barbers=[]
        for result in results:
            barber=Barber(result[1],result[2],result[3],result[4],result[0])
            barbers.append(barber)
        return barbers
    
    @classmethod
    def get_clients_with_appointments(cls):
        query="""
                select distinct clients.id,clients.fname,clients.lname,clients.phone,clients.email from clients inner join appointments where clients.id==appointments.client_id;
                """
        conn=sqlite3.connect(DATABASE_URL)
        cursor=conn.cursor()
        results=cursor.execute(query).fetchall()
        print(results)
        clients=[]
        for result in results:
            client=Client(result[1],result[2],result[3],result[4],result[0])
            clients.append(client)
        return clients



    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} client id={self.client_id} barber id={self.barber_id} date={self.date} cut style={self.cut_style} price={self.price}  />"


Barber.drop_table()
manuel=Barber("Manuel","Garcia","07-12-2023","779-343-3434")
manuel.save()
mike=Barber("Manuel","Garcia","07-12-2023","779-343-3434")
mike.save()

Client.drop_table()
bob=Client("Bob","Miller","343-343-3434","millerb@gmail.com")
bob.save()
steve=Client("Steve","Wonder","993-333-4343","smiths@gmail.com")
steve.save()

Appointment.drop_table()
bob.book_appointment(manuel,"07-25-2023","spike",20)
bob.book_appointment(manuel,"07-30-2023","spike",7)
steve.book_appointment(steve,"07-30-2023","spike",20)

print(Appointment.get_barbers_with_appointments())
print()
print(Appointment.get_clients_with_appointments())
# print(manuel.get_clients_by_hair_cut("spike"))
# print()
# print(manuel.get_appointments_by_date("07-30-2023"))