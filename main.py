import pandas as pd

def todo():
    list_todo = ["Eating", "Lessons", "Bath", "Homework"]
    print("------------------------------------")
    print(list_todo)
    print("------------------------------------")
    df_todo = []

    while True:
        df_input = input("What's on your mind? ")
        if df_input in list_todo:
            df_time = input(f"At what time do you want to {df_input}? ")
            df_todo.append([df_input, df_time])
            print("------")
            print("Noted")
            print("------")
        else:
            print("Task not in the list, please choose from the list.")
        
        again_input = input("Do you want to add more? (Yes/No) ").lower()
        if again_input != "yes":
            break

    df = pd.DataFrame(df_todo, columns=["Task", "Time"])
    return df

# Call the function and convert the DataFrame to HTML
df = todo()
html_table = df.to_html(index=False, classes="table table-striped")

# Save the HTML table to a file

with open("todo_table.html", "w") as file:
    file.write(html_table)
