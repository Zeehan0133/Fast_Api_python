from typing import Optional
from fastapi import FastAPI , Path
from pydantic import BaseModel #It is a validation and parsing library which maps your data to a Python class.

app=FastAPI()

students = {
    1:{
        "name" : "Rohit",
        "age" : 23,
        "institution" : "Kodnest"
    }
}

class Student(BaseModel):
    name : str
    age : int
    institution : str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age : Optional[int] = None
    institution: Optional[str] = None


@app.get("/")
def index():
    return {"name" :"Zeehan khan",
              "institute": "BridgeLabz"}

@app.get("/get-students/{student_id}")
def get_student(student_id : int = Path(None,description="The ID of the student you want to view",gt=0, lt=3 )):
    return students[student_id] 

@app.get("/get-by-name")
def get_student(name: str = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"data" :" Not found"}

@app.get("/get-by-name/{student_id}")
def get_student(*,student_id : int, name: str = None,test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"data" :" Not found"}

@app.post("/create-student/{student_id}")
def create_student(student_id : int, student: Student):
    if student_id in students:
        return {"Error ": "Student  Exists"}

    students[student_id]= student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id : int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student Does not exist"}
    
    if student.name != None:
        students[student_id].name = student.name
    
    if student.age != None:
        students[student_id].age = student.age

    if student.institution != None:
        students[student_id].institution = student.institution
    
    return students[student_id]

@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error" : "Student does not exist"}
    
    del students[student_id]
    return {"Message" : "Student deleted successfully"}
