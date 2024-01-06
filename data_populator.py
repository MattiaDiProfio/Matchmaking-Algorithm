# Import built-in libraries
from faker import Faker
import random
import csv

# Create instance of Faker class
fake = Faker()

# Define general keywords
suffixes = [ "Internship", "Placement", "Opportunity" ]
medical_jobs = [ "Registered Nurse", 
                "Physician", 
                "Medical Laboratory Technician", 
                "Pharmacist", 
                "Medical Assistant", 
                "Surgeon", 
                "Radiologic Technologist", 
                "Physical Therapist", 
                "Dental Hygienist", 
                "Emergency Medical Technician (EMT)" 
            ]

populator_data = {
    "candidates" : {
        # Generate 2500 random full-names
        "fullname" : [ fake.name() for _ in range(1000) ],
        "degree" : [ 
            "Doctor of Medicine (M.D.)", 
            "Doctor of Osteopathic Medicine (D.O.)", 
            "Doctor of Dental Medicine (D.M.D.)", 
            "Doctor of Dental Surgery (D.D.S.)", 
            "Doctor of Veterinary Medicine (D.V.M.)", 
            "Doctor of Pharmacy (Pharm.D.)", 
            "Doctor of Nursing Practice (D.N.P.)", 
            "Doctor of Physical Therapy (D.P.T.)", 
            "Doctor of Optometry (O.D.)", 
            "Doctor of Podiatric Medicine (D.P.M.)", 
            "Doctor of Chiropractic (D.C.)", 
            "Master of Public Health (M.P.H.)", 
            "Master of Health Administration (M.H.A.)", 
            "Bachelor of Science in Nursing (B.S.N.)", 
            "Bachelor of Science in Biomedical Science (B.S.)" 
            ],
        "experience" : [ "surgery", "dentistry", "nursing", None ,"nutrition", "physiotherapy", "immunology" ]
    },
    "jobs" : {
        # Generate random placements titles 
        "title" : [ f"{position} {random.choice(suffixes)}" for position in medical_jobs ], 
        "company" : [ fake.company() for _ in range(100)], 
        "field" : [ "surgery", "dentistry", "nursing", "nutrition", "physiotherapy", "immunology" ]
    }
}

if __name__ == "__main__":

    # Populate the candidates dataset
    with open("candidates.csv", 'w', newline='') as f:
        writer = csv.writer(f)

        # create and write a candidate entry for each name
        for name in populator_data["candidates"]["fullname"]:
            # obtain attributes from above objects
            course = populator_data["candidates"]["degree"][random.randint(0, 100) % 15]
            score = random.randint(50, 100)
            experience = populator_data["candidates"]["experience"][random.randint(0, 100) % 7]
            study_mode = ["online", "campus", None][random.randint(0, 100) % 3]
            study_pattern = ["PT", "FT", None][random.randint(0, 100) % 3]

            candidate = [ name, course, score, experience, study_mode, study_pattern ]
            writer.writerow(candidate)

    # Populate the jobs dataset
    with open("jobs.csv", 'w', newline='') as f:
        writer = csv.writer(f)

        # create and write a candidate entry for each name
        for company in populator_data["jobs"]["company"]:

            # obtain attributes from above objects
            title = populator_data["jobs"]["title"][random.randint(0, 100) % 10]
            field = populator_data["jobs"]["field"][random.randint(0, 100) % 6]
            minscore = random.randint(70, 95)
            positions = random.randint(3, 10)

            job = [ title, company, field, minscore, positions ]
            writer.writerow(job) 