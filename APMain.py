"""
Main program file for OUCI Automation Project

Aim:
Program for tracking enrolment and payment for OUCI programs.

Features:
- Payments
    - Registration
        - Include "Semester Registration" that includes all of a semester
    - Tuition
    - Program Speific Payments
        - i.e. Transportation for Afterschool
    - One-time payments
- Program Enrolment
    - Needs to be separated into registered, enrolled, and waiting
        - registered is signed up but no registration payment
        - enrolled is signed up and payed registration
        - waiting is when there is no space
- Data
    - Student Info:
        - Name
        - Address
        - Contact Info
        - DOB
        - Track Attendance
        - If student is a minor:
            - Parent info
            - School name
            - Grade
        - Do not delete student info when they leave
    - Mailing
        - Email list with tagged categories
        - Automatic Emails about payment and late fees
"""

