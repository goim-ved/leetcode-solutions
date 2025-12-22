import os

def generate_readme():
    py_dir = "python"
    cpp_dir = "cpp"
    
    py_files = [f for f in os.listdir(py_dir) if f.endswith('.py')] if os.path.exists(py_dir) else []
    cpp_files = [f for f in os.listdir(cpp_dir) if f.endswith('.cpp')] if os.path.exists(cpp_dir) else []

    problems = {}

    for f in py_files:
        name = os.path.splitext(f)[0]
        if name not in problems: problems[name] = {'py': False, 'cpp': False}
        problems[name]['py'] = True

    for f in cpp_files:
        name = os.path.splitext(f)[0]
        if name not in problems: problems[name] = {'py': False, 'cpp': False}
        problems[name]['cpp'] = True

    sorted_problems = sorted(problems.keys())

    content = "# 🧠 My LeetCode Solutions\n\n"
    content += f"**Total Solved:** {len(sorted_problems)}\n\n"
    content += "| Problem | Python | C++ |\n"
    content += "| :--- | :---: | :---: |\n"

    for name in sorted_problems:
        display_name = name 
        
        py_mark = f"[✅]({py_dir}/{name}.py)" if problems[name]['py'] else "❌"
        cpp_mark = f"[✅]({cpp_dir}/{name}.cpp)" if problems[name]['cpp'] else "❌"
        
        content += f"| {display_name} | {py_mark} | {cpp_mark} |\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":
    generate_readme()