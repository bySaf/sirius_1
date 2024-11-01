import openai

# Установите API ключ OpenAI
openai.api_key = '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'

def read_task():
    # Чтение условия задачи из файла input.txt
    try:
        with open('input.txt', 'r', encoding='utf-8') as file:
            task_content = file.read().strip()
        return task_content
    except FileNotFoundError:
        print("Файл input.txt не найден.")
        return None

def generate_solution(task_content):
    # Запрос к GPT-4-turbo для генерации решения задачи
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant who writes code solutions for computer science problems."},
                {"role": "user", "content": task_content}
            ],
            max_tokens=500,  # Можно увеличить, если требуется более длинный ответ
            temperature=0.2  # Снизить температуру для более точного и прямого ответа
        )
        solution = response['choices'][0]['message']['content']
        return solution
    except openai.error.OpenAIError as e:
        print(f"Произошла ошибка при запросе к OpenAI API: {e}")
        return None

def write_solution(solution):
    # Запись решения в файл output.txt
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(solution)

def main():
    task_content = read_task()
    if task_content:
        print("Задача загружена из input.txt")
        solution = generate_solution(task_content)
        if solution:
            write_solution(solution)
            print("Решение записано в output.txt")
        else:
            print("Не удалось сгенерировать решение.")
    else:
        print("Не удалось прочитать условие задачи.")

if __name__ == "__main__":
    main()
