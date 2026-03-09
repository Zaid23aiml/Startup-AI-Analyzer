from graph.workflow import app

idea = input("Enter your startup idea: ")

result = app.invoke({
    "idea": idea
})

print("\n===== STARTUP REPORT =====\n")
print(result["report"])