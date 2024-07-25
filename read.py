# Read the HTML template
with open("index.html", "r") as file:
    html_template = file.read()

# Read the HTML table
with open("todo_table.html", "r") as file:
    html_table = file.read()

# Insert the HTML table into the template
html_content = html_template.replace("{{ table }}", html_table)

# Save the final HTML file
with open("final_todo_list.html", "w") as file:
    file.write(html_content)

print("HTML file generated successfully.")
