from openai import OpenAI
# client = OpenAI()
import csv
import json

def clean_text(text):
    return text.replace('\n', ' ').strip()

def print_csv_rows_to_file(file_path, output_file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile, open(output_file_path, 'w', encoding='utf-8') as outfile:
        reader = csv.reader(csvfile)
        questions = next(reader)[1:]
        for answers in enumerate(reader, start=1):
            answers = [clean_text(answer) for answer in answers[1:]]
            combined_qa = [
                {"question": clean_text(question), "answer": answer}
                for question, answer in zip(questions, answers)
            ]
            json_output = json.dumps(combined_qa, ensure_ascii=False, indent=2)
            outfile.write(json_output + "\n\n")

def load_json_arrays_from_file(input_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        file_content = infile.read().strip()
        json_strings = file_content.split('\n\n')
        data = [json.loads(json_string) for json_string in json_strings if json_string]
    return data

def start_grading(system_prompt, user_prompt, output_file_path):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={"type": "json_object"},
        messages=[
          {"role": "system", "content": system_prompt},
          {"role": "user", "content": user_prompt},
        ],
        temperature=0
    )
    output_content = response.choices[0].message.content
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.write(output_content + "\n\n")
    return output_content

def get_grade_by_index(file_path, index):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data['answers'][index]['grade']
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_grades(file_path, output_file_path):
    grades = []
    for index in range(10):  # Assuming you want to go from 0 to 14
        grade = get_grade_by_index(file_path, index)
        if grade is not None:
            grades.append(grade)
    with open(output_file_path, 'a') as file:
        file.write(f"{grades}\n")

def read_grades_from_file(file_path):
    grades = []
    with open(file_path, 'r') as file:
        for line in file:
            # Convert the string representation of the list back into a list
            grades.append(eval(line.strip()))
    return grades

def transpose_and_write_grades(input_file_path, output_file_path):
    grades = read_grades_from_file(input_file_path)
    # Transpose the list of lists
    transposed_grades = list(zip(*grades))
    with open(output_file_path, 'w') as file:
        for grade_list in transposed_grades:
            # Convert each tuple back to a list before writing
            file.write(f"{list(grade_list)}\n")
    print(f"Transposed grades written to {output_file_path}")
