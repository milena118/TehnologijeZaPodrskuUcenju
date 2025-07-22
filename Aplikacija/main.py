from logic import start_grading, print_csv_rows_to_file, load_json_arrays_from_file, write_grades, transpose_and_write_grades
import json

# Used to create json from csv
# print_csv_rows_to_file('Tehnologije za podršku učenju.csv', 'answers_to_grade.txt')

json_output_example={
  "answers": [
    {
      "answer": "With Moore's machine the output is determined only after the state is changed while with Mealy's output changes with input changes",
      "grade": 8,
      "explanation": "The answer provides a clear and accurate differentiation between Moore's and Mealy's machines. However, it could be improved by providing a more detailed explanation and real-world examples of their applications."
    },
    {
      "answer": "Wider range of number that can be represented and zeeo is represented unambiguously",
      "grade": 4,
      "explanation": "The answer correctly mentions the wider range of numbers that can be represented using two's complement. However, it lacks clarity and explanation of the second reason. Real-world scenarios could be provided to illustrate the superiority of two's complement over one's complement."
    },
    {
      "answer": "I don't know",
      "grade": 0,
      "explanation": "No answer provided. The grade is zero."
    },
    {
      "answer": "ASCII is used to represent characters, it can have 7 or extended ASCII has 8 bits",
      "grade": 7,
      "explanation": "The answer correctly identifies the purpose of ASCII codes and the number of bits used to represent them. However, it could be improved by providing more details about the extended ASCII and its significance in modern computing."
    },
    {
      "answer": "Data transfer - move data Arithmetic - arithmetic operations Logic  instructions - logic operations Transfer control - manage program flow Comparison inst - compare valeus Bit manipulation - modify bits Load and store - read and write memory",
      "grade": 6,
      "explanation": "The answer provides a basic understanding of the categories of processor commands but lacks clarity and detail in explaining each category. Real-world examples of instructions in each category could enhance the explanation."
    },
    {
      "answer": "Instruction register has the address of the current instruction and counter reg has the address of the next instruction",
      "grade": 9,
      "explanation": "The answer clearly explains the purpose of the instruction register and the counter register. It could be further improved by providing real-world examples of how these registers are used in processor operations."
    },
    {
      "answer": "Can't remember",
      "grade": 0,
      "explanation": "No answer provided. The grade is zero."
    },
    {
      "answer": "1000 0111 0011",
      "grade": 2,
      "explanation": "The answer attempts to represent the number 873 in BCD, but it is incorrect. The explanation lacks clarity and understanding of the BCD system. Real-world examples of BCD representation could help in understanding its significance."
    },
    {
      "answer": "Bus connects the components of processor. Memory bus, data bus an control bus.",
      "grade": 7,
      "explanation": "The answer provides a basic understanding of the purpose of a bus and mentions some of the signals transmitted through the bus. However, it could be improved by explaining the specific role of each type of bus and providing real-world examples of bus operations."
    },
    {
      "answer": "www.cs.elfak.ni.ac.rs/II_godina/spisak_studenata.html",
      "grade": 10,
      "explanation": "The answer correctly provides the URL address for the given page, including the domain, directory, and page name. It is accurate and complete."
    }
  ]
}

# Answers in json that will be graded
answers_to_grade = load_json_arrays_from_file('answers_to_grade.txt')

system_prompt_one = f"""You are participating in a comprehensive test covering various computer science fundamentals. Your task is to grade answers to series of questions. The questions may cover topics such as programming, algorithms, databases, and networking. For each question, you will be provided with an answer. Provide your grade on a scale from 0 to 10 in JSON format for each pair of question and answer. Use the variable 'answer' to indicate what is the answer you are grading 'grade' to indicate the grade and 'explanation' to provide an explanation with at least 20 words like in the example. Identify any knowledge gaps and propose real-world scenarios for clarity. Do not punish syntax errors if the answer can be deducted. If no answer is provided, inform ’No answer provided’, and give a grade of zero.
Example of the expected output:
{json.dumps(json_output_example)}
"""

# Grading with first prompt
# for index, user_prompt in enumerate(answers_to_grade, start=1):
#     output_file_path = f"grading_output_1_{index}.txt"
#     start_grading(system_prompt_one, json.dumps(user_prompt), output_file_path)

expert_answers = load_json_arrays_from_file('expert_answers.txt')

system_prompt_two = f"""You are tasked with grading exams using the highest standards possible. Consider the
following question and the answer provided by an expert. For each question, you will be provided with an answer. Now, evaluate the student’s answers. Provide your grade on a scale from 0 to 10 in JSON format for each pair of question and answer. Use the variable 'answer' to indicate what is the answer you are grading 'grade' to indicate the grade and 'explanation' to provide an explanation with at least 20 words like in the example. Do not punish syntax errors if the answer can be deducted. If no answer is provided, indicate 'No answer provided' and assign a grade of zero.
Identify knowledge gaps and suggest real-world examples to minimize these gaps.
Example of the expected output:
{json.dumps(json_output_example)}
"""

# Grading with first prompt
# for index, user_prompt in enumerate(answers_to_grade, start=1):
#     user_prompt_two = f"Questions and correct answers provided by experts: {json.dumps(expert_answers)}\nQuestions and answers to grade: {json.dumps(user_prompt)}"
#     output_file_path = f"grading_output_2_{index}.txt"
#     start_grading(system_prompt_two, user_prompt_two, output_file_path)

# Getting grades formatted as an array for every student and by every question
for j in range(1, 3):
  for i in range(1, 16):
      input_file = f'grading_output_{j}_{i}.txt'
      write_grades(input_file, f'grades_by_students_{j}.txt')
  transpose_and_write_grades(f'grades_by_students_{j}.txt', f'grades_by_questions_{j}.txt')