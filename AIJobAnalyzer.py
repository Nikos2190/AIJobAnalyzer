from openai import OpenAI

def job():

    job_text = []

    while True:
        job_description = input("Enter job descriptions with enter and "
                                "finish with typing end: ")
        job_description = job_description.strip()
        while job_description == "" :
            print('Give a job description please')
            job_description = input("Enter job descriptions with enter and "
                                    "finish with typing end: ")
            job_description = job_description.strip()

        if job_description.lower() == 'end':
            break
        job_text.append(job_description)

    job_text  = '\n'.join(job_text)
    return job_text

work = job()
client = OpenAI()
response =  client.responses.create(model = 'gpt-6-luna',
                                    instructions = ( "Analyze the provided job description and "
                                                     "identify the job title, "
    "main responsibilities, required skills, and required qualifications. "
    "Present the result clearly and concisely."),
                                    input = work,
                                    max_output_tokens = 600,
                                    reasoning = {'effort': 'none'},
                                    temperature = 0.2)

answer = response.output_text
print(answer)