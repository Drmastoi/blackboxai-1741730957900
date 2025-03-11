import pdfkit

def generate_report(data):
    html_content = f"""
    <html>
    <head>
        <title>MEDCO Compliant Report</title>
    </head>
    <body>
        <h1>MEDCO Compliant Report</h1>
        <h2>Patient Information</h2>
        <p>Name: {data['name']}</p>
        <p>Date of Birth: {data['dob']}</p>
        <p>Gender: {data['gender']}</p>
        <p>Address: {data['address']}</p>
        <p>Phone Number: {data['phone']}</p>
        <p>Email: {data['email']}</p>

        <h2>Medical History</h2>
        <p>Allergies: {data['allergies']}</p>
        <p>Surgeries: {data['surgeries']}</p>
        <p>Current Medications: {data['medications']}</p>

        <h2>Current Health Status</h2>
        <p>Primary Concern: {data['concern']}</p>
        <p>Duration of Concern: {data['duration']}</p>
        <p>Pain Level: {data['pain_level']}</p>

        <h2>Lifestyle Information</h2>
        <p>Smoking: {data['smoking']}</p>
        <p>Alcohol Consumption: {data['alcohol']}</p>
        <p>Exercise Frequency: {data['exercise']}</p>

        <h2>Additional Comments</h2>
        <p>{data['comments']}</p>
    </body>
    </html>
    """
    pdfkit.from_string(html_content, 'medco_report.pdf')

# Example data to generate the report
data = {
    'name': 'John Doe',
    'dob': '01/01/1980',
    'gender': 'Male',
    'address': '123 Main St, Anytown, USA',
    'phone': '123-456-7890',
    'email': 'john.doe@example.com',
    'allergies': 'None',
    'surgeries': 'Appendectomy',
    'medications': 'None',
    'concern': 'Chest Pain',
    'duration': '2 weeks',
    'pain_level': '7',
    'smoking': 'No',
    'alcohol': 'Occasionally',
    'exercise': '3 times a week',
    'comments': 'No additional comments.'
}

generate_report(data)
