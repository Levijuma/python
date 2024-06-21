class Cars:
    def __init__(self, model, yearofmanufacture, type, colour):
        self.model = model
        self.yearofmanufacture = yearofmanufacture
        self.type = type
        self.colour = colour

    def display(self):
        print(f"My dream car is {self.model}, manufactured in {self.yearofmanufacture}, being a {self.type} type,{self.colour} in colour")


ca_rs = Cars('toyota', '2019', 'hunchback', 'red')
ca_rs.display()
ca_rs2 = Cars('volkswagen', '2017', 'golf', 'black')
ca_rs2.display()
ca_rs3 = Cars('porsche', '2014', 'tubrbo', 'white')
ca_rs3.display()
