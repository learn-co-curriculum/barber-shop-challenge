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
        pass

    def get_clients_by_hair_cut(self,cut_style):
        pass
    
    def get_appointments_by_date(self,date):
        pass

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

    def __init__(self,fname,lname,phone,email):
        self.fname=fname
        self.lname=lname
        self.phone=phone
        self.email=email
        self.all.append(self)

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
        pass

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
    
    def __init__(self,client_id,barber_id,date,cut_style,price):
        self.client_id=client_id
        self.barber_id=barber_id
        self.date=date
        self.cut_style=cut_style
        self.price=price
        self.all.append(self)

    def __repr__(self):
        return f"<{type(self).__name__} id={self.id} client id={self.client_id} barber id={self.barber_id} date={self.date} cut style={self.cut_style} price={self.price}  />"


Barber.drop_table()
manuel=Barber("Manuel","Garcia","07-12-2023","779-343-3434")
manuel.save()
print(manuel)

print()

Client.drop_table()
bob=Client("Bob","Miller","343-343-3434","millerb@gmail.com")
bob.save()
print(bob)
steve=Client("Steve","Smith","993-333-4343","smiths@gmail.com")
steve.save()
print(steve)

# bob.book_appointment(manuel,"07-25-2023","spike",20)
# bob.book_appointment(manuel,"07-30-2023","regular",7)
# steve.book_appointment(manuel,"07-30-2023","spike",20)

# print(manuel.get_clients_by_hair_cut("spike"))
# print()
# print(manuel.get_appointments_by_date("07-30-2023"))