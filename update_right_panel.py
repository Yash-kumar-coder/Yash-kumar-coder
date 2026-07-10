import re
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Column where the values start (approx)
# User's spacing puts values at around character index 32
# "yash@kumar" is 10 chars.

def generate_line(y, key, value, id_prefix=None, nested=False, is_header=False):
    if is_header:
        # e.g. <tspan x="390" y="30">yash@kumar</tspan> -—————————————————————————————————————————————-—-
        # "yash@kumar" has 10 chars. The total length of header is around 60 chars.
        hyphens = "—" * (60 - len(key) - 3)
        return f'<tspan x="390" y="{y}">{key}</tspan> -{hyphens}-—-'
    
    if key == "":
        return f'<tspan x="390" y="{y}" class="cc">. </tspan>'
    
    # Calculate dots needed to align values to ~column 32
    # e.g. "OS" -> 2 chars. "Languages.Programming" -> 21 chars.
    key_length = len(key)
    dot_count = 32 - key_length - 3 # "-3" for ". " and ":"
    dots = "." * max(1, dot_count)
    
    # Process key parts for colors (e.g. "Languages.Programming")
    parts = key.split('.')
    formatted_key = f'.</tspan><tspan class="key">'.join(parts)
    
    dots_id = f' id="{id_prefix}_dots"' if id_prefix else ''
    value_id = f' id="{id_prefix}"' if id_prefix else ''
    
    return f'<tspan x="390" y="{y}" class="cc">. </tspan><tspan class="key">{formatted_key}</tspan>:<tspan class="cc"{dots_id}> {dots} </tspan><tspan class="value"{value_id}>{value}</tspan>'

def generate_right_panel():
    lines = [
        {"y": 30, "k": "yash@kumar", "v": "", "h": True},
        {"y": 50, "k": "OS", "v": "Windows 11"},
        {"y": 70, "k": "Uptime", "v": "18 years, 11 months", "id": "age_data"},
        {"y": 90, "k": "Host", "v": "Independent Developer"},
        {"y": 110, "k": "Kernel", "v": "React &amp; Firebase Developer"},
        {"y": 130, "k": "IDE", "v": "VS Code, Cursor AI"},
        {"y": 150, "k": "", "v": ""},
        {"y": 170, "k": "Languages.Programming", "v": "JavaScript, HTML, CSS"},
        {"y": 190, "k": "Languages.Frameworks", "v": "React, Tailwind CSS"},
        {"y": 210, "k": "Languages.Backend", "v": "Firebase, Node.js (Learning)"},
        {"y": 230, "k": "Languages.Real", "v": "English, Hindi"},
        {"y": 250, "k": "", "v": ""},
        {"y": 270, "k": "Hobbies.Software", "v": "Startup Building, Open Source"},
        {"y": 290, "k": "Hobbies.Hardware", "v": "Raspberry Pi, PC Customization"},
        {"y": 330, "k": "- Contact", "v": "", "h": True},
        {"y": 350, "k": "Email.Personal", "v": "yashkumar62011@gmail.com"},
        {"y": 370, "k": "GitHub", "v": "Yash-kumar-coder"},
        {"y": 390, "k": "LinkedIn", "v": "yash-gupta-30a066331"},
    ]
    
    xml = '<text x="390" y="30" fill="#24292f">\n'
    for item in lines:
        is_header = item.get("h", False)
        prefix = item.get("id")
        line_xml = generate_line(item["y"], item["k"], item["v"], prefix, is_header=is_header)
        xml += line_xml + '\n'
    xml += '</text>'
    return xml

def update_svg(filepath):
    content = read_file(filepath)
    
    # We replace the second <text> block
    fill_color = "#24292f" if "light" in filepath else "#c9d1d9"
    new_panel = generate_right_panel()
    
    # Inject correct fill color for dark mode
    new_panel = new_panel.replace('fill="#24292f"', f'fill="{fill_color}"')
    
    # Restore height to 530px since we removed lines
    content = re.sub(r'height="\d+px"', 'height="530px"', content)
    
    # Regex to replace from <text x="390"...> to </text>
    content = re.sub(r'<text x="390" y="30" fill=".*?">.*?</text>', new_panel, content, flags=re.DOTALL)
    
    write_file(filepath, content)

if __name__ == "__main__":
    update_svg('c:\\Users\\Admin\\Desktop\\Yash-kumar-coder\\light_mode.svg')
    update_svg('c:\\Users\\Admin\\Desktop\\Yash-kumar-coder\\dark_mode.svg')
    print("Updated right panel.")
