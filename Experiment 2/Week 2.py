#!/usr/bin/python
#-*- coding: utf-8 -*-

class Employee(AdminEmployee):
    def __init__(self):
        self.SNo = None
        self.name = None
        self.email = None
        self.Counter = None

    def Hired(self):
        pass

    def Getname(self):
        pass

class AdminEmployee(Employee):
    def __init__(self):
        self.Name = None
        self.id = None
        self.access level = None

    def adduser(self):
        pass

    def RemoveUser(self):
        pass

class ResearchAssociate(Employee):
    def __init__(self):
        self.fieldofstudy = None

class Course:
    def __init__(self):
        self.name = None
        self.id = None
        self.HRs = None

    def Getenrolledstudnts(self):
        pass

class Faculty:
    def __init__(self):
        self.name = None

    def changecourses(self):
        pass

class Institute:
    def __init__(self):
        self.Name = None
        self.Address = None

    def ChangePolicies(self):
        pass

    def Operation2(self):
        pass

class Lecturer(ResearchAssociate):
    def __init__(self):
        self.name = None
        self.IDNo = None

    def TakeAttendence(self):
        pass

    def GiveAssignments(self):
        pass

class Participation:
    def __init__(self):
        self.hrs = None

class Project:
    def __init__(self):
        self.name = None
        self.start = None
        self.End = None

    def submitproject(self):
        pass