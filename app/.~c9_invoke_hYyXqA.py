import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text, Float
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name
        
#Admin list
class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
  

  
  #KCY
class PromotionDrinkMD(Model):
    __tablename__ = 'promo_drinks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    price = Column(Float,  nullable=False)
    
  
class HealthDrinkMD(Model):
    __tablename__ = 'health_drinks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    price = Column(Float,  nullable=False)  
    
class AlcoholicBeveragesMD(Model):
    __tablename__ = 'alcohol_drinks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    price = Column(Float,  nullable=False)
    
class Alldrinks(Model):
    __tablename__ = 'all_drinks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    alldrinks_cat_id = Column(Integer, ForeignKey('TypeOfProducts.id'), nullable=False)
    product_type = relationship("TypeOfProduct")
    
   #HIN try
class Food(Model):
    __tablename__ = 'Foods'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)

class Foodsnack(Model):
    __tablename__ = 'Food_snacks'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)
    
class FoodConfectionery(Model):
    __tablename__ = 'Food_Confectionerys'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)

    #Li try
class SeaFood(Model):
    __tablename__ = 'SeaFood'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    origin = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)
    
class Fish(Model):
    __tablename__ = 'Fish'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    origin = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)
    
class Meat(Model):
    __tablename__ = 'Meat'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    origin = Column(String(50), nullable=False)
    Price = Column(Integer,  nullable=False)

 #HMK
class AllShop(Model):
    __tablename__ = 'ShopPlace'
    id = Column(Integer, primary_key=True)
    shop_area = Column(String(25), nullable=False)
    shop_district = Column(String(25), nullable=False)
    shop_type = Column(Integer, ForeignKey('ShopTypes.id'), nullable=False)
    shop_category = relationship("ShopType")
    
class ShopType(Model):
    __tablename__ = 'ShopTypes'
    id = Column(Integer, primary_key=True)
    shoptype_name = Column(String(50), nullable=False)

class TypeOfProduct(Model):
    __tablename__ = 'TypeOfProducts'
    id = Column(Integer, primary_key=True)
    type_name = Column(String(50), nullable=False)
    
    
    
 