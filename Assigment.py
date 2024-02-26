from enum import Enum

class Gender (Enum):
    female = 1
    male = 2

class Passenger :
# a code constructor to initalize the attributes Specified.
    def __init__(self, firstName, lastName, gender, dateofbirth , email, phonenumber,passportnumber,IDnumber):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.dateofbirth = dateofbirth
        self.email = email
        self.phonenumber=phonenumber
        self.passportnumber=passportnumber
        self.IDnumber=IDnumber
# appyling a f string in the string represntion of passnger to display info
    def __str__(self):
        body = f"""
        First Name : {self.firstName}
        Last Name: {self.lastName}
        Gender :{self.gender}
        Date of birth : {self.dateofbirth}
        Email : {self.email}
        Phone Number :{self.phonenumber}
        Passport Number :{self.passportnumber}
        ID number : {self.IDnumber}
"""
        return body
# setter and getter for first name
        def setfirstName(self,firstName):
            self.firstName = firstName
        def getfirstName(self):
            return self.firstName
#setter and getter for last name
        def setLastName(self,lastName):
            self.lastName = lastName
        def getLastName(self):
            return self.lastName
# setter and getter for gender
        def setGender(self,gender):
            self.gender = gender
        def getGender(self):
             return self.gender
# setter and getter for date of birth
        def setDateofbirth(self,dateofbirth):
            self.dateofbirth = dateofbirth
        def getDateofbirth(self):
             return self.dateofbirth
# setter and getter for email
        def setEmail(self,email):
            self.email = email
        def getEmail(self):
             return self.email
# setter and getter for phone number
        def setphonenumber(self,phonenumber):
            self.phonenumber = phonenumber
        def getphonenumber(self):
             return self.phonenumber
#setter and getter for passport number
        def setpassportnumber(self,passportnumber):
            self.passportnumber = passportnumber
        def getpassportnumber(self):
             return self.passportnumber
#setter and getter for id number
        def setIDnumber(self,IDnumber):
            self.passportnumber = IDnumber
        def getIDnumber(self):
             return self.IDnumber

class Payment :
# a code constructor to initalize the attributes Specified.
    def __init__ (self,cardtype, cardnumber, expirydate,cvv,billingaddress) :
     self.cardtype=cardtype
     self.cardnumber = cardnumber
     self.expirydate = expirydate
     self.cvv = cvv
     self.billingaddress = billingaddress

# appyling a f string in the string represntion of payment to display info
    def __str__(self):
         body = f"""
        Card Type : {self.cardtype}
        Card Number: {self.cardnumber}
        Expiry Date :{self.expirydate}
        CVV : {self.cvv}
        Billing Address : {self.billingaddress} 
     """
         return body
# setter and getter for card type
    def setcardType(self,cardtype):
        self.cardtype = cardtype
    def getcardType(self):
        return self.cardtype
# setter and getter for card number
    def setcardnumber(self,cardnumber):
        self.cardnumber = cardnumber
    def getcardNumber(self):
        return self.cardnumber
# setter and getter fpr expiry date
    def setexpiryDate(self,expirydate):
        self.expirydate = expirydate
    def getexpiryDate(self):
        return self.expirydate
#setter and getter for cvv
    def setcvv(self, cvv):
        self.cvv = cvv
    def getcvv(self):
        return self.cvv
# setter and getter for billing address
    def setbillingaddress(self, billingaddress):
        self.billingaddress = billingaddress
    def getbillingaddress(self):
        return self.billingaddress

class Airmiles :
# a code constructor to initalize the attributes Specified.
    def __init__(self, memberID, points, membershipStatus, airline , Redeempoints):
        self.memberID = memberID
        self.points = points
        self.membershipStatus = membershipStatus
        self.airline = airline
        self.Redeempoints=Redeempoints
# appyling a f string in the string represntion of passnger to display info
    def __str__(self):
        body = f""" 
        Member ID :{self.memberID}
        Points : {self.points}
        Membership status : {self.membershipStatus}
        Airline : {self.airline}
        Points wished to redeem : {self.Redeempoints}

"""
        return body
 # Setter and getter for memberID
    def setmemberID(self, memberID):
        self.memberID = memberID
    def getmemberID(self):
        return self.memberID

 # Setter and getter for points
    def setpoints(self,points):
        self.points = points
    def getPoints(self):
        return self.points

# Setter and getter  for membershipStatus
    def setmembershipStatus(self,membershipStatus):
        self.membershipStatus = membershipStatus
    def getmembershipStatus(self):
        return self.membershipStatus

# Setter and getter for airline
    def setairline(self,airline):
        self.airline = airlinee
    def getairline(self):
        return self.airline

# Setter and getter for redeempoints
    def setRedeempoints(self,Redeempoints):
        self.Redeempoints = Redeempoints
    def getRedeempoints(self):
        return self.Redeempoints

class Booking :
    def __init__ (self, departureAirport ,destinationAirport , travelDate ,numberOfPassengers , travel_time, gatenumber,seat ,flightnumber, bordingtill) :
        self.departureAirport=departureAirport
        self.destinationAirport= destinationAirport
        self.travelDate =travelDate
        self.numberOfPassengers = numberOfPassengers
        self. travel_time =travel_time
        self. gatenumber = gatenumber
        self.seat=seat
        self.flightnumber=flightnumber
        self.bordingtill=bordingtill

    # appyling a f string in the string represntion of passnger to display info
    def __str__(self):
        body = f""" 
        Departure from :{self.departureAirport}
        Destination : {self.destinationAirport}
        Travel Date : {self.travelDate}
        Number of passengers: {self.numberOfPassengers}
        Time of travel : {self.travel_time}
        Bording closes : {self.bordingtill}
        Gate number : {self.gatenumber}
        Assigned Seat : {self.seat}
        Flight Number : {self.flightnumber}
        
"""
        return body
# Setter abd getter  for departure Airport
    def setdepartureairport(self, departureAirport):
        self.departureAirport = departureAirport
    def getdepartureairport(self):
        return self.departureAirport

# Setter and getter for destination Airport
    def setdestinationairport(self, destinationAirport):
        self.destinationAirport = destinationAirport
    def getDestinationAirport(self):
        return self.destinationAirport

# Setter and getter for travel Date
    def settraveldate(self, travelDate):
        self.travelDate = travelDate
    def gettraveldate(self):
        return self.travelDate

# Setter and getter for numberOfPassengers
    def setnumberOfPassengers(self, numberOfPassengers):
        self.numberOfPassengers = numberOfPassengers
    def getnumberOfPassengers(self):
        return self.numberOfPassengers

# Setter and getter for travelTime
    def settravel_time(self, travel_time):
        self.travel_time = travel_time
    def gettravel_time(self):
        return self.travel_time

# Setter and getter for gateNumber
    def setgatenumber(self, gatenumber):
        self.gatenumber = gatenumber
    def getgatenumber(self):
        return self.gatenumber

# Setter and getter for seat
    def setseat(self, seat):
        self.seat = seat
    def getseat(self):
        return self.seat

# Setter and getter  for flightNumber
    def setflightnumber(self, flightNumber):
        self.flightNumber = flightNumber
    def getflightnumber(self):
        return self.flightNumber

# Setter and getter  for bording till
    def setbordingtill(self,bordingtill):
        self.bordingtill=bordingtill
    def getbordingtill(self):
        return self.bordingtill

    def passenger (self):
        pass

# assigning the class passenger with an object
asigment_person=Passenger(firstName="James",lastName="Smith",gender=2, dateofbirth= "1975 -10 - 17",
                          email="jamessmith.1975@hotmail.com",phonenumber="(312)-767-6527", passportnumber="j9752683657"
                          ,IDnumber="46287-75453-67")
# assigning the class payment with an object
asigment_person1=Payment(cardtype="Amex",cardnumber="7835-8752-8653",expirydate="2026-7-14",
                         cvv="765",billingaddress=" New Lenox,street45, apatement")
# assigning the class airmiles with an object
asigment_person2=Airmiles(memberID="635-748-765", points=" 12,906", membershipStatus=" gold status",
                          airline="National Airlines",Redeempoints= "1,500")
# assigning the class Booking with an object
asigment_person3 = Booking(departureAirport=" Chicago ORD", destinationAirport= "New York JFK",
                            travelDate= "2020-12-6" , numberOfPassengers="1",travel_time="11:20", gatenumber= "03"
                            ,seat="09A",flightnumber="NA4321", bordingtill="11:40")


print(asigment_person)
print(asigment_person1 )
print(asigment_person2 )
print(asigment_person3 )
